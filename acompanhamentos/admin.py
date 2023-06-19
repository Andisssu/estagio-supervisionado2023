from django.contrib import admin
from .models import Acompanhamentos, AcompanhamentoDisciplinas, AcompanhamentoInterpretes, AcompanhamentoMonitores, AcompanhamentoTutores
# Register your models here.

class AcompanhamentosAdmin(admin.ModelAdmin):
    list_display = ('aco_semestre', 'aco_inicio', 'aco_fim', 'aco_aluno_pcd')
    list_display_links = ('aco_semestre',)
    list_filter = ('aco_semestre', 'aco_aluno_pcd')
    list_per_page = 8
    search_fields = ('aco_semestre', 'aco_aluno_pcd')
    list_editable = ('aco_fim',)

class AcompanhamentoDisciplinasAdmin(admin.ModelAdmin):
    list_display = ('AsDis_disciplina', 'AsDis_acompanhamento')
    list_display_links = ('AsDis_acompanhamento',)
    list_filter = ('AsDis_disciplina', 'AsDis_acompanhamento')
    list_per_page = 8
    search_fields = ('AsDis_disciplina__dis_nome', 'AsDis_acompanhamento__aco_aluno_pcd__alu_nome')
    list_editable = ('AsDis_disciplina',)

class AcompanhamentoInterpretesAdmin(admin.ModelAdmin):
    list_display = ('AsInt_inicio', 'AsInt_fim', 'AsInt_interprete', 'AsInt_acompanhamento')
    list_display_links = ('AsInt_acompanhamento',)
    list_filter = ('AsInt_interprete', 'AsInt_acompanhamento')
    list_per_page = 8
    search_fields = ('AsInt_interprete', 'AsInt_acompanhamento')
    list_editable = ('AsInt_interprete',)

class AcompanhamentoMonitoresAdmin(admin.ModelAdmin):
    list_display = ('AsMon_inicio', 'AsMon_fim', 'AsMon_monitor', 'AsMon_acompanhamento')
    list_display_links = ('AsMon_acompanhamento',)
    list_filter = ('AsMon_monitor', 'AsMon_acompanhamento')
    list_per_page = 8
    search_fields = ('AsMon_monitor', 'AsMon_acompanhamento')
    list_editable = ('AsMon_monitor',)

class AcompanhamentoTutoresAdmin(admin.ModelAdmin):
    list_display = ('AsTut_inicio', 'AsTut_fim', 'AsTut_tutor', 'AsTut_acompanhamento')
    list_display_links = ('AsTut_acompanhamento',)
    list_filter = ('AsTut_tutor', 'AsTut_acompanhamento')
    list_per_page = 8
    search_fields = ('AsTut_tutor', 'AsTut_acompanhamento')
    list_editable = ('AsTut_tutor',)

admin.site.register(Acompanhamentos, AcompanhamentosAdmin)
admin.site.register(AcompanhamentoDisciplinas, AcompanhamentoDisciplinasAdmin)
admin.site.register(AcompanhamentoInterpretes, AcompanhamentoInterpretesAdmin)
admin.site.register(AcompanhamentoMonitores, AcompanhamentoMonitoresAdmin)
admin.site.register(AcompanhamentoTutores, AcompanhamentoTutoresAdmin)
