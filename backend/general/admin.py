from django.contrib import admin
from .models import Interview


class InterviewAdmin(admin.ModelAdmin):
    model = Interview


admin.site.register(Interview, InterviewAdmin)
