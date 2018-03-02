from django.contrib import admin
from .models import Enquete, Resposta

# admin.site.register(Enquete)


class RespostaInline(admin.StackedInline):
    model = Resposta
    extra = 3


class EnqueteAdmin(admin.ModelAdmin):
    inlines = [
        RespostaInline
    ]

    list_filter = ('ativa',)
    search_fields = ('texto',)
    list_display = ('texto', 'ativa')


admin.site.register(Enquete, EnqueteAdmin)
