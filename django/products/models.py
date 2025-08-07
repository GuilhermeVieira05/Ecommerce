from django.db import models

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

class Product(models.Model):
    id          = models.AutoField(primary_key=True)
    name        = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(blank=True, null=True)
    category    = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='product_category')
    price       = models.DecimalField(max_digits=10, decimal_places=2)
    stock       = models.PositiveIntegerField()
    is_active   = models.BooleanField(default=True)
    image       = models.ImageField(upload_to='products/', null=True, blank=True)

    def __str__(self):
        
        return self.name

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'