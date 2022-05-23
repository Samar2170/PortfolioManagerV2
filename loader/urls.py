from django.urls import path
from loader.views import UploadFDHoldings, UploadStockHoldings, UploadZeordhaHoldings

urlpatterns = [
    path('upload-stock-holdings/',UploadStockHoldings.as_view(),name='upload_stock_holdings'),
    path('upload-fd-holdings/',UploadFDHoldings.as_view(),name='upload_fd_holdings'),
    path('upload-zerodha-holdings/',UploadZeordhaHoldings.as_view(),name='upload_zerodha_holdings'),
#     path('upload-listed-ncd-holdings/',UploadListedNCDHoldings.as_view(),name='upload_listed_ncd_holdings'),
#     path('upload-mf-holdings/',UploadMFHoldings.as_view(),name='upload_mf_holdings'),
]
