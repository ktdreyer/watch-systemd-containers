project deprecated: see podman-auto-update instead
==================================================
It's been several years since I wrote this, and there are many better options
now. For example, see
https://docs.podman.io/en/latest/markdown/podman-auto-update.1.html

watch systemd containers
========================

This tool does a couple things:

1. Look at all the running containers with ``docker ps``.

2. Run ``docker pull`` on each running container's image.

3. If ``docker pull`` found updates, then check if there is an
   equivalently-named active systemd service for this container, and restart
   it.

Similar to https://github.com/v2tec/watchtower, with far fewer features and
uses systemd to restart containers instead of ``docker`` directly.

Ansible
-------

To configure this as part of an Ansible role:

.. code-block:: yaml

    - git:
        repo: https://github.com/ktdreyer/watch-systemd-containers
        dest: /srv/watch-systemd-containers

    - cron:
        name: watch systemd containers
        minute: 0
        hour: 12
        user: root
        job: "PYTHONPATH=/srv/watch-systemd-containers /srv/watch-systemd-containers/bin/watch-systemd-containers"
        cron_file: ansible_watch-containers
