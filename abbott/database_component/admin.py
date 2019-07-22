from django.contrib import admin

# Register your models here.
from .models import TransLog
from .models import TransSurvey
admin.site.register(TransLog)
admin.site.register(TransSurvey)