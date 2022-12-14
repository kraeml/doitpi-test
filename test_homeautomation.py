import pytest

@pytest.mark.parametrize("directory, pre_dir", [
    ("raspberry-pi-home-automation", "workspace"),
    ("Getting-Started-with-ESPHome", "workspace"),
    ("IOTstack", "containers")
])
def test_user_file(host, directory, pre_dir):
    user = host.user()
    file = host.file(user.home + "/" + pre_dir+ "/" + directory)
    assert file.exists
    assert file.is_directory

@pytest.mark.parametrize("name,version", [
    ("git", "0"),
    ("vim", "0"),
    ("mosquitto-clients", "0")
])
def test_packages(host, name, version):
    pkg = host.package(name)
    assert pkg.is_installed
    if not version == "0":
        assert pkg.version.startswith(version)
