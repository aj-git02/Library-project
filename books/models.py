from django.db import models

# Create your models here.
class Books(models.Model):
    Name = models.CharField(max_length=64)
    Description = models.CharField(max_length=10000)
    rating = models.IntegerField()

    def __str__(self):
        return f"{self.Name}"

class Borrow(models.Model):
    Issuer = models.CharField(max_length=10)
    Name = models.ForeignKey(Books,on_delete=models.CASCADE,related_name="issuers")

    def __str__(self):
        return f"{self.Issuer} has issued {self.Name}"