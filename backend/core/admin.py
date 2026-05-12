from django.contrib import admin
from .models import Daibunrui, Chubunrui, Shobunrui


@admin.register(Daibunrui)
class DaibunruiAdmin(admin.ModelAdmin):
    fields = ("code", "name")
    list_display = ["code", "name"]

    search_fields = ["code", "name"]
    ordering = ["code"]


@admin.register(Chubunrui)
class ChubunruiAdmin(admin.ModelAdmin):
    fields = ("code", "name", "daibunrui")
    list_display = ["code", "name", "daibunrui"]

    list_filter = ["daibunrui"]
    search_fields = ["code", "name"]
    ordering = ["code"]


@admin.register(Shobunrui)
class ShobunruiAdmin(admin.ModelAdmin):
    fields = ("code", "name", "chubunrui")
    list_display = ["code", "name", "chubunrui"]

    list_filter = ["chubunrui"]
    search_fields = ["code", "name"]
    ordering = ["code"]
