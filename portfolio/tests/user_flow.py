from django.contrib.auth.models import User
from portfolio.models.accounts import GeneralAccount
import time

def test_generic_account_creation():
    """
    Test the generic account creation.
    """
    # Create a new account.
    user = User.objects.create_user(
        username="test_user",
        email="",
        password="test_password"
    )
    time.sleep(10)
    accounts = GeneralAccount.objects.get(user=user)
    assert accounts is not None

#### Completed


