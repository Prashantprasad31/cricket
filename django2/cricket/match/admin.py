from django.contrib import admin
from match.models import Match

# Register your models here.
class MatchAdmin(admin.ModelAdmin):
    list_display=['id','name','score','strikerate']

admin.site.register(Match,MatchAdmin)
