from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=150, db_index=True, verbose_name="Назва")
    photo = models.ImageField("Фото",upload_to='photos/&Y/%m/&d/')
    price = models.IntegerField(db_index=True, verbose_name="Ціна")
    category = models.ForeignKey('Category',on_delete=models.PROTECT, null=True, blank=True )


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Одежа'
        verbose_name_plural = "Одежі"


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name="Назва")


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = "Катерогії"
