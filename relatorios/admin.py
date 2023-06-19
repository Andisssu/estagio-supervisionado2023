from django.contrib import admin
from .models import RelatoriosMon, RelatoriosTut
# Register your models here.

class RelatoriosMonAdmin(admin.ModelAdmin):
    list_display = ('relM_titulo', 'relM_data', 'relM_arquivo', "relM_monitoria")
    list_display_links = ('relM_titulo',)
    list_filter = ('relM_titulo', 'relM_data')
    list_per_page = 8
    search_fields = ('relM_titulo',)
    list_editable = ('relM_arquivo',)

class RelatoriosTutAdmin(admin.ModelAdmin):
    list_display = ('relT_titulo', 'relT_data', 'relT_arquivo', "relT_tutoria")
    list_display_links = ('relT_titulo',)
    list_filter = ('relT_titulo', 'relT_data')
    list_per_page = 8
    search_fields = ('relT_titulo',)
    list_editable = ('relT_arquivo',)

admin.site.register(RelatoriosMon, RelatoriosMonAdmin)
admin.site.register(RelatoriosTut, RelatoriosTutAdmin)
