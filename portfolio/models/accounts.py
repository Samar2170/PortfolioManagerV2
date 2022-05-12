from django.db import models
from django.contrib.auth.models import User
from abc import ABC

class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account_code = models.CharField(max_length=100, unique=True)



class BankAccount(Account):
    balance = models.FloatField(default=0)
    account_no = models.CharField(max_length=100, unique=True)
    bank_name = models.CharField(max_length=100)
    bank_code = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        self.account_code = self.user.username + '_' + self.account_no
        super().save(*args, **kwargs)


class DematAccount(Account):
    balance = models.FloatField(default=0)
    account_no = models.CharField(max_length=100, unique=True)
    broker = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        self.account_code = self.user.username + '_' + self.account_no
        super().save(*args, **kwargs)
        
class GeneralAccount(Account):
    account_no = models.CharField(max_length=100, unique=True)

    def save(self, *args, **kwargs):
        self.account_code = self.user.username + '_' + self.account_no
        super().save(*args, **kwargs)


def fetch_account(account_code):
    try:
        account = BankAccount.objects.get(account_code=account_code)
        return account
    except BankAccount.DoesNotExist:
        try:
            account = DematAccount.objects.get(account_code=account_code)
            return account
        except DematAccount.DoesNotExist:
            try:
                account = GeneralAccount.objects.get(account_code=account_code)
                return account
            except GeneralAccount.DoesNotExist:
                return None
