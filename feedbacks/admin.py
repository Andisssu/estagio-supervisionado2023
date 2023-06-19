from django.contrib import admin
from .models import Feedbacks
# Register your models here.

class FeedbacksAdmin(admin.ModelAdmin):
    list_display = ('fee_titulo', 'fee_descricao', 'fee_data', 'fee_arquivo', 'fee_acompanhamento')
    list_display_links = ('fee_titulo',)
    list_filter = ('fee_titulo', 'fee_data')
    list_per_page = 8
    search_fields = ('fee_titulo',)
    list_editable = ('fee_descricao', 'fee_arquivo')

admin.site.register(Feedbacks, FeedbacksAdmin)
