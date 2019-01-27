from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Casino
from .models import Bonus
admin.site.register(Casino)
admin.site.register(Bonus)