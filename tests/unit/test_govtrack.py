import pytest


def test_bill(gt):
    """Verify the request for retrieving a bill."""
    gt.bill(id=76416)
    gt.api.session.get.assert_called_once_with(
        'https://www.govtrack.us/api/v2/bill/76416'
    )
