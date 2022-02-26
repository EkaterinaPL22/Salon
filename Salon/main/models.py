from django.db import models


class Client(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)
    phone = models.CharField(max_length=40)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Order(models.Model):
    id_order = models.AutoField(primary_key=True)
    id_user = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    procedures = models.ManyToManyField('Procedure')

    def __str__(self):
        return self.id_user


class Procedure(models.Model):
    id_procedure = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=40)
    price = models.IntegerField()

    def __str__(self):
        return self.name