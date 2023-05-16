from django.shortcuts import render
from examen.models import Examen, Pregunta, Respuesta


def aplicacion(request):
    examen_activo = Examen.objects.filter(activo=True).first()
    examen = examen_activo.nombre if examen_activo else None
    preguntas = Pregunta.objects.filter(examen=examen_activo) if examen_activo else []
    respuestas = Respuesta.objects.filter(pregunta__in=preguntas) if preguntas else []
    contexto = {
        'examen': examen,
        'preguntas': preguntas,
        'respuestas': respuestas,
    }
    return render(request, 'examen/aplicacion_examen.html', contexto)