from django.db import models
import os
import datetime
# Create your models here.


def filepath(request,filename):
    old_filename=filename
    timeNow=datetime.datetime.now().strftime('%y%m%d%H%M%S')
    filename="%s%s",(timeNow,old_filename)
    print(filename)
    return os.path.join('uploads/',filename)

class Item(models.Model):
    food_name=models.TextField(max_length=191)
    food_price=models.IntegerField()
    food_image=models.ImageField(upload_to=filepath,null=True,blank=True)