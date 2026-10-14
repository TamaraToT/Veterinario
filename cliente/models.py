from django.db import models

class Cliente(models.Model):
    """Representa al dueño de la mascota"""
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    direccion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Mascota(models.Model):
    """Representa al animal que recibe la atención"""
    # Un cliente puede tener muchas mascotas (Relación Uno a Muchos)
    dueno = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='mascotas')
    nombre = models.CharField(max_length=50)
    especie = models.CharField(max_length=50) # Ejemplo: Perro, Gato
    raza = models.CharField(max_length=50, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} ({self.dueno.nombre})"


class Atencion(models.Model):
    """Representa la consulta médica o historial clínico"""
    # Una mascota puede tener muchas atenciones (Relación Uno a Muchos)
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE, related_name='atenciones')
    fecha = models.DateTimeField(auto_now_add=True)
    motivo = models.CharField(max_length=255) # Ejemplo: Control, Vacunación, Emergencia
    diagnostico = models.TextField()
    tratamiento = models.TextField()
    costo = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Atención de {self.mascota.nombre} - {self.fecha.strftime('%d/%m/%Y')}"

