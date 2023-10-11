from django.db import models


class Equipment(models.Model):
    date_of_use = models.DateField(auto_now_add=True)
    CR_number = models.CharField(max_length=50)
    cal_due_date = models.DateField()
    temperature = models.FloatField()
    pin_size = models.CharField(max_length=100)
    part_number = models.CharField(max_length=100)
    lot_number = models.CharField(max_length=100)
    inspector = models.CharField(max_length=100)
    correction_remark = models.CharField(max_length=1255, blank=True)
    history_record = models.CharField(max_length=1255, blank=True)
    remark = models.CharField(max_length=1255, blank=True)