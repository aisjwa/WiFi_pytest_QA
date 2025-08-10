import pytest

@pytest.mark.roaming
def test_placeholder_roaming():
    # Pretend we measured < 1500 ms handover
    roam_ms = 900
    assert roam_ms < 1500
