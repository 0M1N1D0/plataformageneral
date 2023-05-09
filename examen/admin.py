from django.contrib import admin
from .models import Examen, Pregunta, Respuesta, Resultado
from django import forms


class ExamenAdmin(admin.ModelAdmin):
    list_display = ("nombre", "calificacion_minima", "observaciones")
    search_fields = ("nombre", "calificacion_minima", "observaciones")
    list_per_page = 10
    ordering = ("nombre",)

admin.site.register(Examen, ExamenAdmin)


class PreguntaAdmin(admin.ModelAdmin):
    list_display = ("enunciado", "examen")
    search_fields = ("enunciado", "examen__nombre")
    list_filter = ("examen",)
    list_per_page = 10
    ordering = ("examen",)

admin.site.register(Pregunta, PreguntaAdmin)


# **************************************************************
# This class is used to display the examen field in the form
class RespuestaForm(forms.ModelForm):
    examen = forms.ModelChoiceField(queryset=Examen.objects.all(), label="Examen")

    class Meta:
        model = Respuesta
        fields = "__all__"
# **************************************************************


class RespuestaAdmin(admin.ModelAdmin):
    form = RespuestaForm
    list_display = ("pregunta", "respuesta", "es_correcta", "get_examen")
    search_fields = ("pregunta__enunciado", "respuesta")
    list_filter = ("pregunta", "pregunta__examen")
    list_per_page = 10
    ordering = ("pregunta",)

    # ************************************************************** 
    # This method is used to display the examen field in the list_display
    def get_examen(self, obj):
        return obj.pregunta.examen

    get_examen.short_description = "Examen"
    # **************************************************************

admin.site.register(Respuesta, RespuestaAdmin)


class ResultadoAdmin(admin.ModelAdmin):
    list_display = ("usuario", "examen", "calificacion", "fecha_aplicacion")
    search_fields = ("usuario__username", "examen__nombre", "calificacion", "fecha_aplicacion")
    list_filter = ("usuario", "examen", "fecha_aplicacion")
    list_per_page = 10
    ordering = ("usuario",)

admin.site.register(Resultado, ResultadoAdmin)
