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
