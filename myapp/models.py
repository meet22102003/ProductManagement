from django.db import models
from django.utils.safestring import mark_safe

# Create your models here.

class producttable(models.Model):
    name = models.CharField(max_length=40)
    price = models.FloatField()
    description = models.TextField()
    proimage = models.ImageField(upload_to="photos")

    def product_photo(self):
        return mark_safe('<img src="{}" width="100/"/>'.format(self.proimage.url))
    product_photo.allow_tags = True

class registertable(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=40)
    gender = models.CharField(max_length=60)
    phone = models.BigIntegerField()
    address = models.TextField()
    role = models.CharField(max_length=30)
    profilepicture = models.ImageField(upload_to="photos")

    def profileimage_photo(self):
        return mark_safe('<img src="{}" width="100/"/>'.format(self.profilepicture.url))
    profileimage_photo.allow_tags = True

class carttable(models.Model):
    userid = models.ForeignKey(registertable,on_delete=models.CASCADE)
    productid = models.ForeignKey(producttable,on_delete=models.CASCADE)
    quantity = models.FloatField()
    totalamount = models.FloatField()
    cartstatus = models.IntegerField()
    orderid = models.IntegerField()


