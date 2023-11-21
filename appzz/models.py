from django.db import models

# Create your models here.
# used to create and manage tables


class studentsinfo(models.Model):
    stu_id = models.IntegerField()
    stu_f_name = models.CharField(max_length=30)
    stu_l_name = models.CharField(max_length=30)
    phone_number = models.IntegerField()
    stu_message = models.TextField()













