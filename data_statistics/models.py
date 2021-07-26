from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Location(models.Model):
    continent = models.CharField(max_length=128)
    country = models.CharField(max_length=128)
    province = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    companies = models.ManyToManyField(Company)

    def __str__(self):
        return f"{self.continent} - {self.country}"


class Employee(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    age = models.IntegerField()
    job_title = models.CharField(max_length=128)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='employees')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='employees')

    def __str__(self):
        return f"{self.first_name} - {self.last_name}"
