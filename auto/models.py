from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Car(models.Model):
    title_car = models.CharField(max_length=100)
    owner_car = models.CharField(max_length=100)
    catergories = models.ManyToManyField(Category, null=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.title_car}-{self.owner_car}: {', '.join(i.name for i in self.catergories.all())}'

class NumberCar(models.Model):
    select_car = models.OneToOneField(Car, on_delete=models.CASCADE)
    nummber = models.CharField(max_length=100, default='0_KG____')
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.select_car}-{self.nummber}'

class ReviewCar(models.Model):
    choice_car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='review')
    MARK = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    )
    mark = models.CharField(max_length=100, choices=MARK)
    text = models.TextField(blank=True)
    created_at = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.choice_car}-{self.mark}'