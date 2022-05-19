from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from loader.request_models import StockHoldingRequest


class APIViewWithPermission(APIView):
    permission_classes = [IsAuthenticated]


class UploadStockHoldings(APIViewWithPermission):
    def post(self, request):

        return Response({"message": "Upload stock holdings"})