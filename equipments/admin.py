from django.contrib import admin
from .models import Equipment


class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('date_of_use', 'CR_number', 'cal_due_date', 'temperature', 'pin_size',
                    'part_number', 'lot_number', 'inspector', 'correction_remark', 'history_record', 'remark')


admin.site.register(Equipment, EquipmentAdmin)
