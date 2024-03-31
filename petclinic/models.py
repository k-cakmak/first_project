from django.db import models

# Create your models here.
class Owner(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, null=True)
    phone = models.CharField(max_length=20)
    gender = models.CharField(max_length=1, choices={"F":"Female", "M":"Male"}, null=True)

    def __str__(self):
        return f"{self.name} {self.last_name}"


class Pet(models.Model):
    name = models.CharField(max_length=50)
    birth = models.DateField(null=True)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"