import pytest
import pwd

BASE_USER = pwd.getpwuid(1000)
ROOT_USER = pwd.getpwuid(0)

def test_user_file(host):
    # First Boot Skript ermitteln
    file = host.file("/firstboot.sh")
    assert file.exists
    #assert file.mode == 0o760
    assert file.uid == 0
    assert file.contains("#SOME COMMANDS YOU WANT TO EXECUTE")

    file = host.file(BASE_USER.pw_dir + "/workspace/doitpi-test/.venv")
    assert file.exists
    assert file.is_directory
    assert file.uid == BASE_USER.pw_gid

@pytest.mark.parametrize("directory, pre_dir, user_uid", [
    ("bin", BASE_USER.pw_dir, BASE_USER.pw_uid),
    (".config/codeserver", BASE_USER.pw_dir, BASE_USER.pw_uid),
    ("workspace", BASE_USER.pw_dir, BASE_USER.pw_uid),
    (".borgmatic/", BASE_USER.pw_dir, BASE_USER.pw_uid),
    (".ansible/roles/deluxebrain.python", BASE_USER.pw_dir, BASE_USER.pw_uid),
    (".ansible/roles/m4rcu5nl.zerotier-one", BASE_USER.pw_dir, BASE_USER.pw_uid),
    ("workspace/doitpi-test/.venv", BASE_USER.pw_dir, BASE_USER.pw_uid)
])

def test_user_dir(host, directory, pre_dir, user_uid):
    file = host.file(pre_dir + "/" + directory)
    assert file.exists
    assert file.is_directory
    assert file.uid == user_uid
@pytest.mark.parametrize("file, pre_dir, user_uid", [
    ("firstboot.service", "/etc/systemd/system", ROOT_USER.pw_uid),
    (".envrc", BASE_USER.pw_dir + "/.borgmatic", BASE_USER.pw_uid)
])

def test_file(host, file, pre_dir, user_uid):
    file = host.file(pre_dir + "/" + file)
    assert file.exists
    #assert file.contains("layout pyenv 3.12.2")
    assert file.uid == user_uid

    