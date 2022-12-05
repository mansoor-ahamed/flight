from django.db import models



# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=50)
    phone=models.CharField(max_length=12)
    desc=models.TextField(max_length=300)

    def __str__(self):
        return self.name

class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title= models.CharField(max_length=50)
    content=models.TextField()
    author=models.CharField(max_length=50)
    timeStamp=models.DateTimeField(blank=True)

    def __int__(self):
        return self.title


class Flight(models.Model):

    roundtrip=models.CharField(max_length=50, blank=False)
    country=models.CharField(max_length=50)
    country1=models.CharField(max_length=50)
    dept=models.CharField(max_length=50)
    retu=models.CharField(max_length=50)
    adult=models.CharField(max_length=50)
    child=models.CharField(max_length=50)
    travel=models.CharField(max_length=50)

    def __int__(self):
        return self.id    