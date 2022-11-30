from django.contrib import admin

# Register your models here.
from .models import Scores


class ScoresAdmin(admin.ModelAdmin):
    list_display = ('user', 'result')
    search_fields = ['user__email', 'user__username', 'user__first_name', 'user__last_name', 'result']


admin.site.register(Scores, ScoresAdmin)
