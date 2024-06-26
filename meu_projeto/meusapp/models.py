from django.db import models

# Create your models here.
class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    imagem = models.ImageField(upload_to='imagens/', null=True, blank=True)

    def _str_(self):
        return self.nome
        
    class Meta:
        app_label = 'meusapp'