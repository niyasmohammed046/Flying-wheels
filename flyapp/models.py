from django.db import models


class bikedata(models.Model):
    Bikename=(models.CharField(max_length=20,null=True,blank=True))
    Company=(models.CharField(max_length=20,null=True,blank=True))
    Price=(models.IntegerField(null=True,blank=True))
    Description=(models.CharField(max_length=400,null=True,blank=True))
    Image=(models.ImageField(upload_to='profile',null=True,blank=True))
    PCategory=(models.CharField(max_length=20,null=True,blank=True))

class bikecategory(models.Model):
    Category=(models.CharField(max_length=20,null=True,blank=True))
    CatDescription=(models.CharField(max_length=400,null=True,blank=True))
    CatImage=(models.ImageField(upload_to='profile',null=True,blank=True))
    
class admindb(models.Model):
    Name=(models.CharField(max_length=20,null=True,blank=True))
    Email=(models.CharField(max_length=20,null=True,blank=True))
    Mobile=(models.IntegerField(null=True,blank=True))
    Password=(models.CharField(max_length=20,null=True,blank=True))