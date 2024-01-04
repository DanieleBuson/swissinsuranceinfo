from django.contrib import admin
from .models import Faq, TestConnection

# Register your models here.
admin.site.register(Faq)
admin.site.register(TestConnection)