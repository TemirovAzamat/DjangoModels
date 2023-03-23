from django.db import models as m


class User(m.Model):
    email = m.CharField(max_length=30)
    password = m.CharField(max_length=25)

    def __str__(self):
        return self.email


class Client(m.Model):
    name = m.CharField(max_length=20)
    card_number = m.IntegerField()
    user = m.OneToOneField(User, on_delete=m.CASCADE)

    def __str__(self):
        return self.name


class Worker(m.Model):
    name = m.CharField(max_length=20)
    position = m.CharField(max_length=20)
    user = m.OneToOneField(User, on_delete=m.CASCADE)

    def __str__(self):
        return self.name


class Ingredient(m.Model):
    name = m.CharField(max_length=20)
    extra_price = m.IntegerField()

    def __str__(self):
        return self.name


class Food(m.Model):
    name = m.CharField(max_length=20)
    start_price = m.IntegerField()
    relation = m.ManyToManyField(Ingredient, related_name='foods', through='Order')

    def __str__(self):
        return self.name


class Order(m.Model):
    food = m.ForeignKey(Food, on_delete=m.CASCADE)
    ingredient = m.ForeignKey(Ingredient, on_delete=m.CASCADE)
    client = m.ForeignKey(Client, on_delete=m.CASCADE)
    worker = m.ForeignKey(Worker, on_delete=m.CASCADE)
    order_date_time = m.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.client} - {self.worker}, {self.food} - {self.ingredient}, {self.order_date_time}'
