from django.db import models

# Create your models here.
# CarCompany and CEO ONE BY ONE RELETIONSHIP 

class CarCompany(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class CEO(models.Model):
    ceo_name = models.CharField(max_length=100)
    company = models.OneToOneField(CarCompany, on_delete=models.CASCADE)
    def __str__(self):
        return self.ceo_name

# one to many relationship with one car company
class CarModel(models.Model):
    model_name = models.CharField(max_length=100)
    company = models.ForeignKey(CarCompany, on_delete=models.CASCADE)
    def __str__(self):
        return self.model_name

# many to many relationship with one car model -- determined which car model is use which fuel
class FuelType (models.Model):
    fuel_type_name = models.CharField(max_length=100)
    used_car_model = models.ManyToManyField(CarModel)
    def __str__(self):
        return self.fuel_type_name
