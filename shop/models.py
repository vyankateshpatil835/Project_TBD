from django.db import models

# Create your models here.
class product(models.Model):
    product_Id = models.AutoField
    product_name = models.CharField(20)
    product_des = models.CharField(300)
    pub_Date = models.DateField