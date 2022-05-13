from portfolio.request_models.entries import StockTrade
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from util.request_helpers import unwrap_query_dict

class APIViewWithPermission(APIView):
    permission_classes = (IsAuthenticated,)



class RegisterStockTrade(APIViewWithPermission):
    def post(self,request):
        requested_data = unwrap_query_dict(request.data)
        data = StockTrade(**requested_data)
        data=data.dict()
        
        return Response(data.dict())
