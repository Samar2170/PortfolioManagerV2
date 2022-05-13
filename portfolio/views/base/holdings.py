from portfolio.views import APIViewWithPermission
from rest_framework.response import Response
from util.request_helpers import unwrap_query_dict

class BaseHoldings(APIViewWithPermission):
    Holdings_Model = None
    Serializer_Class = None
    
    def get(self,request):
        data = self.Holdings_Model.objects.filter(account__user=request.user)
        serializer = self.Serializer_Class(data,many=True)
        return Response(serializer.data)

