from django.db import models

class Cards(models.Model):
    class Meta:
        verbose_name = 'Cards'
        verbose_name_plural = 'Cards'
    heading = models.CharField(max_length=50)
    text = models.TextField(max_length=700)
    category = models.ForeignKey('Category', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.heading
class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Category'
    name = models.CharField(max_length=70)
    def __str__(self):
        return self.name


class Fargona(models.Model):
    class Meta:
        verbose_name = 'Fargona'
        verbose_name_plural = 'Fargona'
    viloyat = models.CharField(max_length=50)
    viloyat_haqida = models.TextField(max_length=8700)
    odamlar_soni = models.IntegerField()
    ortacha_yosh = models.IntegerField()
    tumanlar_soni = models.IntegerField()
    image = models.ImageField(null=True)

    def __str__(self):
        return self.viloyat


class Foot(models.Model):
    class Meta:
        verbose_name = 'Foot'
        verbose_name_plural = 'Foot'

    head = models.CharField(max_length=70)
    def __str__(self):
        return self.head