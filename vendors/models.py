from django.db import models

from django.contrib.auth.models import User

class Vendor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=50, unique=True)
    on_time_delivery_rate = models.FloatField(default=0)
    quality_rating_avg = models.FloatField(default=0)
    average_response_time = models.FloatField(default=0)
    fulfillment_rate = models.FloatField(default=0)


    def update_performance_metrics(self):
        completed_pos = self.purchaseorder_set.filter(status='completed')
        total_completed_pos = completed_pos.count()
        if total_completed_pos > 0:
            self.on_time_delivery_rate = (completed_pos.filter(delivery_date__lte=models.F('acknowledgment_date')).count() / total_completed_pos) * 100
            self.quality_rating_avg = completed_pos.aggregate(models.Avg('quality_rating'))['quality_rating__avg']
            self.average_response_time = completed_pos.aggregate(models.Avg(models.ExpressionWrapper(models.F('acknowledgment_date') - models.F('issue_date'), output_field=models.DurationField())))['acknowledgment_date__avg'].total_seconds()
            self.fulfillment_rate = (completed_pos.filter(issue_date__isnull=False, acknowledgment_date__isnull=False).count() / total_completed_pos) * 100
        else:
            self.on_time_delivery_rate = 0
            self.quality_rating_avg = 0
            self.average_response_time = 0
            self.fulfillment_rate = 0
        self.save()

    def __str__(self):
        return self.name

class PurchaseOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    po_number = models.CharField(max_length=50, unique=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=20)
    quality_rating = models.FloatField(null=True, blank=True)
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.po_number


class HistoricalPerformance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()

    def __str__(self):
        return f"{self.vendor} - {self.date}"
