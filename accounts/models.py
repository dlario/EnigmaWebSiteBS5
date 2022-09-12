from django.db import models
from django.db.models import BigAutoField

from django.contrib.auth.models import User


class Person(models.Model):
    server_bt_id = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, default="")
    middle_name = models.CharField(max_length=255, default="")
    last_name = models.CharField(max_length=255, default="")

    def __str__(self):
        return self.first_name + " " + self.last_name


class ContactInformation(models.Model):
    description = models.CharField(max_length=255, default="")
    contact_type = models.CharField(max_length=255, default="")
    contact = models.CharField(max_length=255, default="")
    preferred = models.BooleanField()
    person = models.ForeignKey(Person, on_delete=models.CASCADE)


# Create your models here.
class Company(models.Model):
    server_bt_id = models.IntegerField()
    company_name = models.CharField(max_length=255, default="")
    city = models.CharField(max_length=255, default="Grande Prairie")
    province = models.CharField(max_length=255, default="Alberta")
    address = models.CharField(max_length=255, default="")
    box_number = models.CharField(max_length=255, default="")
    postal_code = models.CharField(max_length=255, default="")

    def __str__(self):
        return self.company_name + " (" + self.city + ")"


class CompanyPerson(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    role = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    # companyadmin = models.BooleanField(default=0)

    def __str__(self):
        return self.person.__str__() + ": " + self.role
