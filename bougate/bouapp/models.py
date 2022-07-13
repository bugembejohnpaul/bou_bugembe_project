from django.db import models


# Create your models here.
class Item(models.Model):
    item_name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    serialno = models.CharField(max_length=20)
    registered_by = models.CharField(max_length=50)
    create_date = models.DateTimeField('date published')
    updated_by = models.CharField(max_length=50)


class Person(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=50)
    organisation = models.CharField(max_length=20)
    department = models.CharField(max_length=50)
    telphone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    created_by = models.CharField(max_length=50)
    create_date = models.DateTimeField('date published')
    updated_by = models.CharField(max_length=50)

