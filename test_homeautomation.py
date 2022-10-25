def test_passwd_file(host):
    passwd = host.file("/etc/passwd")
    assert passwd.contains("root")
    assert passwd.user == "root"
    assert passwd.group == "root"
    assert passwd.mode == 0o644

import pytest

@pytest.mark.parametrize("name,version", [
    ("git", "0"), 
    ("vim", "0")
])
def test_packages(host, name, version):
    pkg = host.package(name)
    assert pkg.is_installed

