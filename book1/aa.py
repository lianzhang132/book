class Auther(models.Model):
    nid = models.AutoField(primary_key=True)
    name= models.CharField(max_length=32)
    age=models.IntegerField()

    authorinfo=models.OneToOneField(to="Auther_info",on_delete=models.CASCADE)
    def __str__(self):
        return (self.name)

class Auther_info(models.Model):
    nid = models.AutoField(primary_key=True)
    birthday = models.DateField()
    age = models.IntegerField()
    telephone =models.BigIntegerField()
    addr=models.CharField(max_length=86)
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
