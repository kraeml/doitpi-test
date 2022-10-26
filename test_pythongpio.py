def test_passwd_file(host):
    passwd = host.file("/etc/passwd")
    assert passwd.contains("root")
    assert passwd.user == "root"
    assert passwd.group == "root"
    assert passwd.mode == 0o644

import pytest

@pytest.mark.parametrize("name,version", [
    ("python3-pip", "0"),
    ("python3-venv", "0"),
    ("python3-pigpio", "0"),
    ("pigpiod", "0"), 
    ("pigpio", "0"),
    ("i2c-tools", "0"),
    ("python3-smbus", "0"),
    ("git", "0"),
    ("virtualenv", "0")
])
def test_packages(host, name, version):
    pkg = host.package(name)
    assert pkg.is_installed

