def test_passwd_file(host):
    passwd = host.file("/etc/passwd")
    assert passwd.contains("root")
    assert passwd.user == "root"
    assert passwd.group == "root"
    assert passwd.mode == 0o644

import pytest

@pytest.mark.parametrize("name,version", [
    ("python3", "3"),
    ("screen", "0"),
    ("tree", "0"),
    ("git", "0"), 
    ("vim", "0"),
    ("nmap", "0"),
    ("build-essential", "0"),
    ("rclone", "0"),
    ("ssh-import-id", "0"),
    ("dphys-swapfile", "20100506"),
    ("etckeeper", "1"),
    ("avahi-utils", "0.8"),
    ("git-flow", "1")
])
def test_packages(host, name, version):
    pkg = host.package(name)
    assert pkg.is_installed

