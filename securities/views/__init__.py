## view all securities
## view one security
## check if security exists
## search for securities




from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from util.pagination import ViewPaginatorMixin

class APIViewWithPermission(APIView):
    permission_classes = [AllowAny]

class BaseSecurities(ViewPaginatorMixin,APIViewWithPermission):
    Securities_Model=None
    def get(self,request,*args,**kwargs):
        page_no = request.GET.get('page', 1)
        securities = self.Securities_Model.objects.all()
        data = list(securities.values())
        return Response({"securities":self.paginate(data,page_no,50)})
    
class BaseSecurity(APIViewWithPermission):
    Securities_Model=None
    def get(self,request,*args,**kwargs):
        name =  request.GET.get('name','')
        symbol = request.GET.get('symbol','')
        if name != '':
            security = self.Securities_Model.objects.filter(name=name)
        elif symbol != '':
            security = self.Securities_Model.objects.filter(symbol=symbol)
        else:
            return Response({"error": "Please provide name or symbol"})
        if len(security) == 0:
            return Response({"error": "Security not found"})
        return Response({"security":list(security.values())})

class BaseSearchSecurities(ViewPaginatorMixin,APIViewWithPermission):
    Securities_Model=None
    def get(self,request,*args,**kwargs):
        name =  request.GET.get('name','')
        symbol = request.GET.get('symbol','')
        page_no = request.GET.get('page',1)
        if name != '':
            securities = self.Securities_Model.objects.filter(name__icontains=name)
        elif symbol != '':
            securities = self.Securities_Model.objects.filter(symbol__icontains=symbol)
        else:
            return Response({"error": "Please provide name or symbol"})
        data = list(securities.values())
        return Response({"securities":self.paginate(data,page_no,50)})




