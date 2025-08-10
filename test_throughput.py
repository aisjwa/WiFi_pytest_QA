import pytest

@pytest.mark.throughput
def test_placeholder_throughput():
    # Placeholder metric to demonstrate structure
    down_mbps = 35  # pretend result from lab run
    assert down_mbps >= 20
