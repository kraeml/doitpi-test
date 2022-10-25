def test_passwd_file(host):
    passwd = host.file("/etc/passwd")
    assert passwd.contains("root")
    assert passwd.user == "root"
    assert passwd.group == "root"
    assert passwd.mode == 0o644

import pytest

@pytest.mark.parametrize("name,version", [
    ("screen", "0"),
    ("tree", "0"),
    ("git", "0"), 
    ("vim", "0"),
    ("nmap", "0"),
    ("build-essential", "0"),
    ("ssh-import-id", "0"),
    ("dphys-swapfile", "20100506"),
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
    ("python3-testinfra", "0")
])
def test_packages(host, name, version):
    pkg = host.package(name)
    assert pkg.is_installed

