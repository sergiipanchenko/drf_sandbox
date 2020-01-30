from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=128)
    price = models.FloatField(default=0.00)


    def save(self, *args, **kwargs):
        super(Product, self).save(*args, **kwargs)

        HistoryProductPrice.objects.create(
            product=self,
            price=self.price
        )

    def __str__(self):
        return self.name


class HistoryProductPrice(models.Model):
    product = models.ForeignKey(Product, related_name='history_price',on_delete=models.CASCADE)

    price = models.FloatField(default=0.00)
    date = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        unique_together = ('product', )

