from django.db import models

class Drone(models.Model):
    nome = models.CharField(max_length=120)
    marca = models.CharField(max_length=50)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    autonomia_minutos = models.IntegerField(help_text="Tempo de voo em minutos")
    alcance_km = models.FloatField(help_text="Alcance máximo em quilômetros")
    estoque = models.PositiveIntegerField(default=0)
    imagem = models.ImageField(upload_to='drones/')
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.marca} {self.nome}"


class Pedido(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    endereco = models.CharField(max_length=250)
    cidade = models.CharField(max_length=100)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pedido #{self.id} - {self.nome}"