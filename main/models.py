from django.db import models
from django.contrib.auth.models import User


class library(models.Model):
    uid=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    published_date=models.DateField()
    added_by=models.ForeignKey(User,on_delete=models.CASCADE)
    is_borrowed=models.BooleanField(default=False)
    borrow_date=models.DateTimeField(null=True,blank=True)
    borrowed_by=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True,related_name="borrow")



    def __str__(self):
        return self.title
    

    