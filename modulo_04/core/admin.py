from django.contrib import admin
from .models import Tarefa


class TarefaAdmin(admin.ModelAdmin):
    # Colunas da listagem
    list_display = ("titulo", "user", "concluida", "criada_em")

    # Barra lateral de filtros
    list_filter = ("concluida", "user", "criada_em")

    # Barra de busca
    search_fields = ("titulo", "user__username")

    # Organização do formulário de edição
    fieldsets = (
        ("Informações Principais", {
            "fields": ("user", "titulo")
        }),
        ("Status da Tarefa", {
            "fields": ("concluida", "criada_em")
        }),
    )

    # Campos somente leitura
    readonly_fields = ("criada_em",)

    # Coluna customizada (email do usuário)
    @admin.display(description="Email do Usuário")
    def get_user_email(self, obj):
        return obj.user.email


# Registro no Admin
admin.site.register(Tarefa, TarefaAdmin)
