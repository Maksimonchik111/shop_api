from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    @property
    def products_count(self):
        product_list = self.products.all()
        return len(product_list)


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', null=True)

    def __str__(self):
        return self.title



class Review(models.Model):
    stars = models.PositiveIntegerField(choices=((i,i) for i in range(1,6)), null=True)
    text = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews', null=True)

    def __str__(self):
        return f'{self.product} - {self.text}'

