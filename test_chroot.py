import pytest

def test_user_file(host):
    user = host.user()
    # Test nicht als root laufen lassen
    assert user.name == "root"
    

    # First Boot Skript ermitteln
    file = host.file("/firstboot.sh")
    assert file.exists
    assert file.mode == 0o760
    assert file.uid == 0
    assert file.contains("#SOME COMMANDS YOU WANT TO EXECUTE")

    file = host.file("/home/pi/workspace/doitpi-test/.venv")
    assert file.exists
    assert file.is_directory
    assert file.uid == 1000

@pytest.mark.parametrize("directory, pre_dir", [
    ("bin", "/home/pi"),
    ("notebooks", "/home/pi"),
    (".borgmatic", "/home/pi")
])

def test_user_file(host, directory, pre_dir):
    file = host.file(pre_dir + "/" + directory)
    assert file.exists
    assert file.is_directory
    assert file.uid == 1000

    