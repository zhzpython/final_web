from django.db import models

class User(models.Model):
    name = models.CharField(max_length=20, null=True)
    phone = models.CharField(max_length=20, null=True)
    email = models.CharField(max_length=40, null=True)
    password = models.CharField(max_length=40, null=True)

class info(models.Model):
    name=models.CharField(max_length=20, null=True)
    gender=models.CharField(max_length=20, null=True)
    age=models.CharField(max_length=20, null=True)
    position=models.CharField(max_length=80, null=True)
    city=models.CharField(max_length=80, null=True)
    salary=models.CharField(max_length=20, null=True)
    edu=models.CharField(max_length=20, null=True)
    work_experience=models.CharField(max_length=20, null=True)


class ip_info(models.Model):
    ip=models.CharField(max_length=20,null=True)
    apply_time=models.FloatField(null=True)
    flag=models.CharField(max_length=10,null=True)
    forbid_time=models.FloatField(null=True)



