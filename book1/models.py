from django.db import models



# Create your models here.
class Auther(models.Model):
    nid = models.AutoField(primary_key=True)
    name= models.CharField(max_length=32)

    authorinfo=models.OneToOneField(to="Auther_info",on_delete=models.CASCADE)
    def __str__(self):
        return (self.name)

class Auther_info(models.Model):
    nid = models.AutoField(primary_key=True)
    birthday = models.DateField(default="null")
    age = models.IntegerField(default="null")
    telephone =models.BigIntegerField(default="null")
    addr=models.CharField(max_length=86,default="null")
    salary = models.IntegerField(default=0)
    cost= models.IntegerField(default=0)

class Public_info(models.Model):
    nid = models.AutoField(primary_key=True)
    name=models.CharField(max_length=32)
    city=models.CharField(max_length=32)
    email=models.CharField(max_length=32)
    def __str__(self):
        return (self.name)

class Book(models.Model):
    nid = models.AutoField(primary_key=True)
    title= models.CharField(max_length=32)
    pub_date=models.DateField()
    price = models.DecimalField(max_digits=8,decimal_places=2)

#一对多
    public=models.ForeignKey(to="Public_info",to_field="nid",on_delete=models.CASCADE)
#多对多
    authers=models.ManyToManyField(to="Auther")


    def __str__(self):
        return (self.title)
class Person(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField( max_length=32)
    pwd=models.CharField( max_length=66)
    def __str__(self):
        return self.username