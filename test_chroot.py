import pytest

def test_user_file(host):
    user = host.user()
    # Test nicht als root laufen lassen
    assert user.name == "root"
    

    # Benutzerverzeichnis ermitteln
    file = host.file("/firstboot.sh")
    assert file.exists
    assert file.is_executable
    assert file.is_uid == 0
    assert file.contains("#SOME COMMANDS YOU WANT TO EXECUTE")

    