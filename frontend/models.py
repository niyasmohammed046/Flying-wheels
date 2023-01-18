from django.db import models

class Messagesdb(models.Model):
    Name=(models.CharField(max_length=20,null=True,blank=True))
    Email=(models.CharField(max_length=20,null=True,blank=True))
    Subject=(models.CharField(max_length=20,null=True,blank=True))
    Textarea=(models.CharField(max_length=200,null=True,blank=True))

class emailsubscription(models.Model):
    Emailsub=(models.CharField(max_length=20,null=True,blank=True))

class Registersave(models.Model):
    Username=(models.CharField(max_length=20,null=True,blank=True))
    Email=(models.CharField(max_length=20,null=True,blank=True))
    Password=(models.CharField(max_length=20,null=True,blank=True))
    Password1=(models.CharField(max_length=20,null=True,blank=True))

