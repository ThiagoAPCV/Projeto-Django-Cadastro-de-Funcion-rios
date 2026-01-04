from django.db import models

class Funcionario(models.Model):
    """
    Model que representa um funcionário da empresa.
    Cada atributo vira uma coluna no banco de dados.
    """

    nome = models.CharField(
        max_length=100,
        verbose_name="Nome"
    )

    sobrenome = models.CharField(
        max_length=100,
        verbose_name="Sobrenome"
    )

    remuneracao = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Remuneração"
    )

    tempo_de_servico = models.IntegerField(
        verbose_name="Tempo de Serviço (anos)"
    )

    cpf = models.CharField(
        max_length=11,
        verbose_name="CPF"
    )

    def __str__(self):
        # Forma como o objeto aparece no admin
        return f"{self.nome} {self.sobrenome}"