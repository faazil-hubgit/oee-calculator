from django.contrib import admin

# Register your models here.
from django.contrib import admin

from.models import machines
admin.site.register(machines)

from.models import product_log
admin.site.register(product_log)

from.models import oee
admin.site.register(oee)