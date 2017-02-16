import json
from docker import Client
import subprocess


# Only docker-py v1.10 is currently supported. Need to add support for v2.
cli = Client()


def had_update(repository):
    """
    Use "docker pull" to get the latest tag for a repo.

    Return True if we downloaded a new image, False otherwise.
    """
    for line in cli.pull(repository=repository, tag='latest', stream=True):
        data = json.loads(line)
        if 'Status: Downloaded newer image' in data.get('status', ''):
            return True
    return False


def restart_service(name):
    """
    If a systemd service "name" is running, restart it.

    Do nothing otherwise.
    """
    is_active_cmd = ['systemctl' '-q' 'is-active', name]
    if subprocess.call(is_active_cmd) != 0:
        return
    restart_cmd = ['systemctl', 'restart', name]
    subprocess.check_call(restart_cmd)


def main():
    running = cli.containers()
    images = set([c['Image'] for c in running])
    updated = filter(had_update, images)

    for container in running:
        name = container['Names'][0]
        if name.startswith('/'):
            name = name[1:]
        image = container['Image']
        if image in updated:
            print('Container %s image %s had an update' % (name, image))
            restart_service(name)
