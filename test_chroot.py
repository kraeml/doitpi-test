import pytest

def test_user_file(host):
    user = host.user()
    # Test nicht als root laufen lassen
    assert user.name == "root"
    

    # Benutzerverzeichnis ermitteln
    file = host.file("/firstboot.sh")
    assert file.exists
    assert file.mode == 0o775
    assert file.uid == 0
    assert file.contains("#SOME COMMANDS YOU WANT TO EXECUTE")

    