from django.contrib import admin
from .models import board_members, corp_members, resources, sponsors, pages

admin.site.register(board_members)
admin.site.register(corp_members)
admin.site.register(resources)
admin.site.register(sponsors)
admin.site.register(pages)


