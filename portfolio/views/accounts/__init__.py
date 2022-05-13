from rest_framework.viewsets import ViewSet
from rest_framework.permissions import IsAuthenticated
from portfolio.models.accounts import BankAccount,DematAccount,GeneralAccount
from portfolio.serializers.accounts import GeneralAccountSerializer,BankAccountSerializer,DematAccountSerializer
from rest_framework.response import Response
from portfolio.request_models.accounts import BankAccountRequest,DematAccountRequest
from util.request_helpers import unwrap_query_dict

class BankAccountViewSet(ViewSet):
    permission_classes = [IsAuthenticated]
    def list(self, request):
        user=request.user
        serializer = BankAccountSerializer(BankAccount.objects.filter(user=user), many=True)
        return Response(serializer.data)
    
    def create(self,request):
        requested_data = unwrap_query_dict(request.data)
        data = BankAccountRequest(**requested_data)
        BankAccount.objects.create(user=request.user,**data.dict())
        return Response({"message":"Bank Account Created"})


class DematAccountViewSet(ViewSet):
    permission_classes = [IsAuthenticated]
    def list(self, request):
        user=request.user
        serializer = DematAccountSerializer(DematAccount.objects.filter(user=user), many=True)
        return Response(serializer.data)
    
    def create(self,request):
        requested_data = unwrap_query_dict(request.data)
        data = DematAccountRequest(**requested_data)
        DematAccount.objects.create(user=request.user,**data.dict())
        return Response({"message":"Demat Account Created"})



class GeneralAccountViewSet(ViewSet):
    permission_classes = [IsAuthenticated]
    def list(self, request):
        user=request.user
        serializer = GeneralAccountSerializer(GeneralAccount.objects.filter(user=user), many=True)
        return Response(serializer.data)
    

