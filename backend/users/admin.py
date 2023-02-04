from django.contrib import admin
from .models import Nugget


class Manager(admin.ModelAdmin):
    model = Nugget


admin.site.register(Nugget, Manager)
