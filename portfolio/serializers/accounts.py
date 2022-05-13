from rest_framework.serializers import ModelSerializer
from portfolio.models.accounts import GeneralAccount,BankAccount,DematAccount


class BankAccountSerializer(ModelSerializer):
    class Meta:
        model = BankAccount
        fields = ('account_code','account_no','balance','bank_name','bank_code')

class GeneralAccountSerializer(ModelSerializer):
    class Meta:
        model = GeneralAccount
        fields = ('account_code','account_no')

class DematAccountSerializer(ModelSerializer):
    class Meta:
        model = DematAccount
        fields = ('account_code','account_no','broker')
        