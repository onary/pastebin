from django.contrib import admin
from django.conf import settings

from paste.models import Paste

class PasteAdmin(admin.ModelAdmin):
	list_display = ("__unicode__", "expiration", "syntax", )

admin.site.register(Paste, PasteAdmin)