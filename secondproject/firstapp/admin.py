from django.contrib import admin
from firstapp.models import Website, Topic, AccessRecord
# Register your models here.

admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(Website)
