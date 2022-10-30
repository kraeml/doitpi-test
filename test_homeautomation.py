import pytest

@pytest.mark.parametrize("directory", [
    ("raspberry-pi-home-automation"),
    ("Getting-Started-with-ESPHome"),
    ("IOTstack")
])
def test_user_file(host, directory, pre_dir = "workspace"):
    user = host.user()
    file = host.file(user.home + "/" + pre_dir+ "/" + directory)
    assert file.exists
    assert file.is_directory

@pytest.mark.parametrize("name,version", [
    ("git", "0"),
    ("vim", "0")
])
def test_packages(host, name, version):
    pkg = host.package(name)
    assert pkg.is_installed
    if not version == "0":
        assert pkg.version.startswith(version)
