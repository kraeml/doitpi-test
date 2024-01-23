import pytest

@pytest.mark.parametrize("directory", [
    ("bin"),
    ("notebooks"),
    ("workspace"),
    ("workspace/Blockly-gPIo")
])
def test_user_file(host, directory):
    user = host.user()
    file = host.file(user.home + "/" + directory)
    assert file.exists
    assert file.is_directory

def test_boot_config(host):
    file = host.file("/boot/config.txt")
    assert file.exists
    assert file.is_file
    assert file.contains("^dtparam=i2c_arm=on$")
    assert file.contains("^dtparam=i2c_vc=on$")

@pytest.mark.parametrize("serial_interface,return_code", [
    ("get_i2c", "0"),
    ("get_spi", "0")
])
def test_serial(host, serial_interface, return_code):
    cmd = host.check_output("raspi-config nonint " + serial_interface)
    assert return_code in cmd

@pytest.mark.parametrize("service_name", [
    ("bluetooth"),
])
def test_services(host, service_name):
    # Services eingerichtet
    service = host.service(service_name)
    assert service.is_running
    assert service.is_enabled

def test_jupyter(host):
    # Services eingerichtet
    jupyter = host.service("jupyter")
    assert not jupyter.is_running
    assert not jupyter.is_enabled
    assert "--notebook-dir" in jupyter.systemd_properties["ExecStart"]
    assert "--ServerApp.ip=0.0.0.0" in jupyter.systemd_properties["ExecStart"]

@pytest.mark.parametrize("name,version", [
    ("python3-pip", "0"),
    ("python3-venv", "0"),
    ("python3-pigpio", "0"),
    ("pigpiod", "0"),
    ("pigpio", "0"),
    ("i2c-tools", "0"),
    ("python3-smbus", "0"),
    ("git", "0"),
    ("virtualenv", "0"),
    ("bluetooth", "0"),
    ("pi-bluetooth", "0"),
    ("bluez", "0")
])
def test_packages(host, name, version):
    pkg = host.package(name)
    assert pkg.is_installed
    if not version == "0":
        assert pkg.version.startswith(version)
