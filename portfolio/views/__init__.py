from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

class APIViewWithPermission(APIView):
    permission_classes = (IsAuthenticated,)