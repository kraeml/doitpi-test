import pytest

def test_user_file(host):
    user = host.user()
    # Test nicht als root laufen lassen
    assert user.name != "root"
    # Der Benutzer soll nicht pi heißen
    assert user.name != "pi"

    # Benutzerverzeichnis ermitteln
    file = host.file(user.home)
    assert file.exists
    assert file.is_directory

    # Dateien und Inhalte feststellen
    file = host.file(user.home + "/.config/code-server/config.yaml")
    assert file.exists
    assert file.is_file
    assert file.contains("bind-addr: 0.0.0.0:8080")

    file = host.file(user.home + "/bin")
    assert file.exists
    assert file.is_directory

    file = host.file(user.home + "/workspace")
    assert file.exists
    assert file.is_directory

def test_etc_files(host):
    # Konfigdateien mit Inhalt feststellen
    file = host.file("/etc/dhcp/dhclient.conf")
    assert file.exists
    assert file.is_file
    assert file.contains("retry 20;")

def test_boot_files(host):
    # Booteinstellungen überprüfen
    file = host.file("/boot/config.txt")
    assert file.exists
    assert file.is_file
    assert file.contains("^do_boot_wait=1")
    assert not file.contains("^do_boot_wait=0")

def test_commands(host):
    # Boot wait ausgeschaltet
    assert host.run_test("raspi-config nonint get_boot_wait")
    assert "1" in host.check_output("raspi-config nonint get_boot_wait")
    
    # Locale installiet und auf de_DE gestzt
    cmd = host.check_output("locale -a")
    assert "de_DE.utf8" in cmd
    assert "en_GB.utf8" in cmd
    assert "en_US.utf8" in cmd
    assert "fr_FR.utf8" in cmd
    assert "nl_NL.utf8" in cmd
    cmd = host.check_output("localectl status")
    assert "LANG=de_DE.UTF-8" in cmd
    assert "X11 Layout: de" in cmd

def test_services(host):
    # Services eingerichtet
    codeserver = host.service("codeserver")
    assert codeserver.is_running
    assert codeserver.is_enabled
    assert "--disable-telemetry" in codeserver.systemd_properties["ExecStart"]
    firstboot = host.service("firstboot")
    assert not firstboot.is_running
    assert not firstboot.is_enabled

# Pakete installiert
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
