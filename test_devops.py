import pytest

# ToDo Docker installiert, enabled und running
def test_services(host):
    # Services eingerichtet
    docker_service = host.service("docker")
    assert docker_service.is_running
    assert docker_service.is_enabled

def test_user_docker(host):
    assert "docker" in host.user().groups

def test_user_file(host):
    user = host.user()
    file = host.file(user.home + "/workspace")
    assert file.exists
    assert file.is_directory

def test_docker-compose_link(host):
    file = host.file("/usr/bin/docker-compose")
    assert file.exists
    assert file.is_symlink

@pytest.mark.parametrize("name,version", [
    ("screen", "0"),
    ("tree", "0"),
    ("git", "0"),
    ("vim", "0"),
    ("nmap", "0"),
    ("build-essential", "0"),
    ("ssh-import-id", "0"),
    ("tmux", "0"),
    ("ansible", "0"),
    ("yamllint", "0"),
    ("expect", "0"),
    ("nmap", "0"),
    ("net-tools", "0"),
    ("cmake", "0"),
    ("unzip", "0"),
    ("zip", "0"),
    ("lxc", "0"),
    ("lxc-templates", "0"),
    ("python3-testinfra", "0"),
    ("docker-ce", "0")
])
def test_packages(host, name, version):
    pkg = host.package(name)
    assert pkg.is_installed
    if not version == "0":
        assert pkg.version.startswith(version)
