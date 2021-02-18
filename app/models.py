from django.db import models
import os

# Create your models here.


def path_and_rename(instance,filename):
	upload_to = 'images/'
	ext = filename.split('.')[-1] #demo.jpg    jpg
	image_name = 'Demo2.'+ext
	return os.path.join(upload_to,image_name)



class student(models.Model):
	profile_image = models.ImageField(null=True,blank=True,upload_to=path_and_rename)
	roll = models.IntegerField()
	name = models.CharField(max_length=50)
	per = models.DecimalField(max_digits=4,decimal_places=2)
