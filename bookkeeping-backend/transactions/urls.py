from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TransactionViewSet, upload_csv, monthly_summary

router = DefaultRouter()
router.register(r'transactions', TransactionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('upload-csv/', upload_csv),
    path('monthly_summary/', monthly_summary),  
    
]
