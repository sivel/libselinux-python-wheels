# libselinux-python-wheels
Ansible playbooks to build wheel files for libselinux-python

This is a super early POC

## Goals

This project aims to give people the ability to build python wheel files for libselinux-python to allow installation in virtual environments without using `--system-site-packages`

## Use

### Requirements

1. Have access to docker, either installed locally or available and configured via `DOCKER_` environment variables
2. Ansible >= 2.7

### Executing

```
$ ansible-playbook -i hosts -v python-selinux.yml
```

Wheel files will be downloaded into the `wheelhouse` directory.

## docker.pex?

To avoid needing to install the `docker` python library to work with the Ansible `docker_container` module, a PEX file with `docker` installed within is provided to work as the `ansible_python_interpreter` for `docker_container` tasks.

This file was created using:

```
$ pex -o docker.pex docker
```

To read more about PEX check out [https://pex.readthedocs.io/en/stable/](https://pex.readthedocs.io/en/stable/)
