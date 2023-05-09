from django.db import models
from perfil.models import CustomUser


class Examen(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombre del examen")  
    calificacion_minima = models.FloatField(verbose_name="Calificación mínima")
    observaciones = models.TextField(verbose_name="Observaciones")

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Examen"
        verbose_name_plural = "Exámenes"
        ordering = ["nombre"]


class Pregunta(models.Model):
    enunciado = models.TextField(verbose_name="Enunciado de la pregunta")
    examen = models.ForeignKey(Examen, on_delete=models.CASCADE, verbose_name="Examen", related_name="preguntas")

    def __str__(self):
        return self.enunciado
    
    class Meta:
        verbose_name = "Pregunta"
        verbose_name_plural = "Preguntas"
        ordering = ["enunciado"]


class Respuesta(models.Model):
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE, verbose_name="Pregunta", related_name="respuestas")
    respuesta = models.TextField(verbose_name="Respuesta")
    es_correcta = models.BooleanField(verbose_name="¿Es correcta?")

    def __str__(self):
        return self.respuesta
    
    class Meta:
        verbose_name = "Respuesta"
        verbose_name_plural = "Respuestas"
        ordering = ["respuesta"]


class Resultado(models.Model):
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="Usuario", related_name="resultados")
    examen = models.ForeignKey(Examen, on_delete=models.CASCADE, verbose_name="Examen", related_name="resultados")
    calificacion = models.FloatField(verbose_name="Calificación")
    fecha_aplicacion = models.DateField(verbose_name="Fecha de aplicación")

    def __str__(self):
        return str(self.examen)
    
    class Meta:
        verbose_name = "Resultado"
        verbose_name_plural = "Resultados"
        ordering = ["calificacion"]


class RespuestaUsuario(models.Model):
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="Usuario", related_name="respuestas")
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE, verbose_name="Pregunta", related_name="respuestas_usuario")
    respuesta_usuario = models.ForeignKey(Respuesta, on_delete=models.CASCADE, verbose_name="Respuesta", related_name="respuestas_usuario")

    def __str__(self):
        return str(self.respuesta)
    
    class Meta:
        verbose_name = "Respuesta del usuario"
        verbose_name_plural = "Respuestas del usuario"
        ordering = ["respuesta_usuario"]









