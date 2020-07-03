from django.db import models

class Person(models.Model):
  name = models.CharField(max_length = 30)
  card_num = models.CharField(max_length = 16)
  password = models.CharField(max_length = 100)
  cvc = models.IntegerField()

  #python manage.py makemigrations
  #python manage.py migrate



    