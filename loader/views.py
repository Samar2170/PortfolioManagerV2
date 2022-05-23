from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from loader.models import StockHoldingFile,FDHoldingFile
from portfolio.models.accounts import DematAccount
from loader.tasks import  parse_ot_fd_holding,  parse_ot_stock_holding, parse_ot_zerodha_file

class APIViewWithPermission(APIView):
    permission_classes = [IsAuthenticated]


class BaseUploadHoldings(APIViewWithPermission):
    Holding_Model=None
    def post(self,request,*args,**kwargs):
        files=request.FILES
        if len(files) != 1:
            return Response({"error": "Please upload a single file."})
        account_no = request.data.get('account_no')
        for _,file in files.items():
            formatt=file.name.split('.')[-1]
            account=DematAccount.objects.get(account_no=account_no)
            file_obj = self.Holding_Model(file_name=file.name,file_path=file,user=request.user,account=account,format=formatt)
            file_obj.save()
        self.call_after_save(file_obj.id)
        return Response({"success": "File uploaded successfully."})
    
    def call_after_save(self,file_id):
        pass


class UploadStockHoldings(BaseUploadHoldings):
    Holding_Model=StockHoldingFile

    def call_after_save(self,file_id):
        parse_ot_stock_holding.delay(file_id)

class UploadFDHoldings(BaseUploadHoldings):
    Holding_Model=FDHoldingFile

    def call_after_save(self,file_id):
        parse_ot_fd_holding.delay(file_id)



class UploadZeordhaHoldings(BaseUploadHoldings):
    Holding_Model=StockHoldingFile

    def call_after_save(self,file_id):
        parse_ot_zerodha_file.delay(file_id)

        