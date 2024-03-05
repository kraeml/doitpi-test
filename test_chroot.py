import pytest
import pwd

BASE_USER = pwd.getpwuid(1000)
ROOT_USER = pwd.getpwuid(0)

@pytest.mark.parametrize("file, pre_dir, user_uid, contains", [
    ("firstboot.service", "/etc/systemd/system", ROOT_USER.pw_uid, "ExecStart=/firstboot.sh"),
    ("firstboot.sh", "", ROOT_USER.pw_uid, "#SOME COMMANDS YOU WANT TO EXECUTE")
])
def test_user_file(host, file, pre_dir, user_uid, contains):
    # First Boot Skript ermitteln
    filesystem = host.file("/filesystem")
    if filesystem.exists:
        file = host.file(pre_dir + "/" + file)
        assert file.exists
        #assert file.mode == 0o764
        assert file.uid == user_uid
        assert file.contains(contains)

@pytest.mark.parametrize("directory, pre_dir, user_uid", [
    ("bin", BASE_USER.pw_dir, BASE_USER.pw_uid),
    (".config/code-server", BASE_USER.pw_dir, BASE_USER.pw_uid),
    ("workspace", BASE_USER.pw_dir, BASE_USER.pw_uid),
    (".borgmatic/", BASE_USER.pw_dir, BASE_USER.pw_uid),
    (".pyenv/", BASE_USER.pw_dir, BASE_USER.pw_uid),
    (".borgmatic/backup", BASE_USER.pw_dir, BASE_USER.pw_uid),
    (".ansible/roles/deluxebrain.python", BASE_USER.pw_dir, BASE_USER.pw_uid),
    (".ansible/roles/m4rcu5nl.zerotier-one", BASE_USER.pw_dir, BASE_USER.pw_uid),
    ("workspace/doitpi-test/.venv", BASE_USER.pw_dir, BASE_USER.pw_uid)
])

def test_user_dir(host, directory, pre_dir, user_uid):
    file = host.file(pre_dir + "/" + directory)
    assert file.exists
    assert file.is_directory
    assert file.uid == user_uid

@pytest.mark.parametrize("file, pre_dir, user_uid, contains", [
    (".envrc", BASE_USER.pw_dir + "/.borgmatic", BASE_USER.pw_uid, "layout python3")
])
def test_file(host, file, pre_dir, user_uid, contains):
    file = host.file(pre_dir + "/" + file)
    assert file.exists
    assert file.contains(contains)
    assert file.uid == user_uid

    