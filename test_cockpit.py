import pytest

# ToDo Docker installiert, enabled und running
def test_services(host):
    # Services eingerichtet
    cockpit_service = host.service("cockpit")
    # assert cockpit_service.is_running
    assert cockpit_service.is_enabled
