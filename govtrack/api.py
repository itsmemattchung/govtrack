import requests
import bills.bill

session = requests.sessions.Session()


def build_url(*args, **kwargs):
    base_url = 'https://www.govtrack.us/api/v2'
    args = [str(arg).strip('/') for arg in args]
    parts = [base_url]
    parts.extend(args)
    url = '/'.join(parts)
    return url


def bill(**kwargs):
    """Retrieve a bill."""
    bill_id = kwargs.get('id')
    url = build_url('bill', bill_id)
    response = session.get(url)
    return bills.bill.Bill(response.json())
