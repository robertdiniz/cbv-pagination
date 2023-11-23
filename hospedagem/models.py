from django.db import models

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField("Nome cliente", max_length=55)
    email = models.EmailField("Email")
    telefone = models.CharField("Telefone", max_length=15)
    endereco = models.TextField("Endereço")

    def __str__(self):
        return self.nome
    
class Quarto(models.Model):
    apartamento = models.IntegerField("Apartamento")
    valor = models.FloatField("Valor")

    def __str__(self):
        return f'{self.apartamento} - {self.valor}'

class Hospedagem(models.Model):
    data_entrada = models.DateField("Data entrada")
    data_saida = models.DateField("Data saída")
    valor = models.FloatField("Valor")
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    quarto = models.ForeignKey(Quarto, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.cliente.nome} - {self.quarto.apartamento}'

class Consumo(models.Model):
    nome = models.CharField("Nome consumo", max_length=55)
    data = models.DateField("Data")
    valor = models.FloatField("Valor")
    hospedagem = models.ForeignKey(Hospedagem, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

 