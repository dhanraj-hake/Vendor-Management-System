from django.urls import path
from .views import (
    VendorListCreateAPIView,
    VendorRetrieveUpdateDestroyAPIView,
    PurchaseOrderListCreateAPIView,
    PurchaseOrderRetrieveUpdateDestroyAPIView,
    HistoricalPerformanceListCreateAPIView,
    HistoricalPerformanceRetrieveUpdateDestroyAPIView,
    VendorPerformanceAPIView, 
    AcknowledgePurchaseOrderAPIView
)

urlpatterns = [
    path('vendors/', VendorListCreateAPIView.as_view(), name='vendor-list'),
    path('vendors/<int:pk>/', VendorRetrieveUpdateDestroyAPIView.as_view(), name='vendor-detail'),
    path('purchase_orders/', PurchaseOrderListCreateAPIView.as_view(), name='purchaseorder-list'),
    path('purchase_orders/<int:pk>/', PurchaseOrderRetrieveUpdateDestroyAPIView.as_view(), name='purchaseorder-detail'),
    path('historical_performance/', HistoricalPerformanceListCreateAPIView.as_view(), name='historicalperformance-list'),
    path('historical_performance/<int:pk>/', HistoricalPerformanceRetrieveUpdateDestroyAPIView.as_view(), name='historicalperformance-detail'),
    path('vendors/<int:vendor_id>/performance/', VendorPerformanceAPIView.as_view(), name='vendor_performance'),
    path('purchase_orders/<int:po_id>/acknowledge/', AcknowledgePurchaseOrderAPIView.as_view(), name='acknowledge_purchase_order'),
    
]
