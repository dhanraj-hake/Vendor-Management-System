from django.shortcuts import render
from rest_framework import generics
from .models import Vendor, PurchaseOrder, HistoricalPerformance
from .serializers import VendorSerializer, PurchaseOrderSerializer, HistoricalPerformanceSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

# Geting Venders list for authenticated user and create new Vender
class VendorListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = VendorSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Vendor.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# Get, Update, and Delete operations for a single Vendor for the authenticated user
class VendorRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = VendorSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Vendor.objects.filter(user=self.request.user)


# Get Vendors list for authenticated user and create new Vendor
class PurchaseOrderListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = PurchaseOrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return PurchaseOrder.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# Get, Update, and Delete operations for a single Purchase Order for the authenticated user
class PurchaseOrderRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PurchaseOrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return PurchaseOrder.objects.filter(user=self.request.user)


# Get Purchase Orders list for authenticated user and create new Purchase Order
class HistoricalPerformanceListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = HistoricalPerformanceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return HistoricalPerformance.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# Get, Update, and Delete operations for a single Historical Performance for the authenticated user
class HistoricalPerformanceRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = HistoricalPerformanceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return HistoricalPerformance.objects.filter(user=self.request.user)



# Get performance metrics for a specific vendor
class VendorPerformanceAPIView(APIView):
    def get(self, request, vendor_id):
        try:
            vendor = Vendor.objects.get(id=vendor_id)
        except Vendor.DoesNotExist:
            return Response({"error": "Vendor not found."}, status=status.HTTP_404_NOT_FOUND)

        performance_metrics = {
            "on_time_delivery_rate": vendor.on_time_delivery_rate,
            "quality_rating_avg": vendor.quality_rating_avg,
            "average_response_time": vendor.average_response_time,
            "fulfillment_rate": vendor.fulfillment_rate
        }
        return Response(performance_metrics)



# Acknowledge a purchase order and recalculate vendor performance metrics
class AcknowledgePurchaseOrderAPIView(APIView):
    def post(self, request, po_id):
        try:
            purchase_order = PurchaseOrder.objects.get(id=po_id)
        except PurchaseOrder.DoesNotExist:
            return Response({"error": "Purchase Order not found."}, status=status.HTTP_404_NOT_FOUND)


        purchase_order.acknowledgment_date = timezone.now()
        purchase_order.save()

        vendor = purchase_order.vendor
        vendor.update_performance_metrics()

        return Response({"message": "Purchase Order acknowledged successfully."}, status=status.HTTP_200_OK)