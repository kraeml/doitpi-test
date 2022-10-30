import pytest

@pytest.mark.parametrize("directory", [
    (".platformio"),
    (".platformio/penv/bin")
])
def test_user_file(host, directory):
    user = host.user()
    file = host.file(user.home + "/" + directory)
    assert file.exists
    assert file.is_directory

@pytest.mark.parametrize("file_name", [
    (".platformio/penv/bin/pio")
])
def test_user_commands(host, file_name):
    user = host.user()
    file = host.file(user.home + "/" + file_name)
    assert file.exists
    assert file.is_file
    assert file.mode == 0o775

def test_udev(host):
    file = host.file("/etc/udev/rules.d/99-platformio-udev.rules")
    assert file.exists
    assert file.is_file

def test_user_aliases(host):
    user = host.user()
    file = host.file(user.home + "/" + ".bash_aliases")
    assert file.exists
    assert file.is_file
    assert file.contains("alias pio=~/.platformio/penv/bin/pio")
    assert file.contains('alias pio_home="pio home --host=0.0.0.0 --no-open &"')
    assert file.contains("alias platformio=pio")

@pytest.mark.parametrize("name,version", [
    ("python3-venv", "0")
])
def test_packages(host, name, version):
    pkg = host.package(name)
    assert pkg.is_installed
    if not version == "0":
        assert pkg.version.startswith(version)
