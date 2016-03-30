import mock
import pytest
import govtrack


@pytest.fixture
def gt():
    """Returns govtrack instance with session mocked."""
    govtrack.api.session = mock.Mock()
    return govtrack
