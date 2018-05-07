from __future__ import unicode_literals 
from django.db import models 

class User(models.Model):
  first_name = models.CharField(max_length = 255)
  last_name = models.CharField(max_length = 255)
  email = models.CharField(max_length = 255)
  age = models.IntegerField()
  created_at = models.DateTimeField(auto_now_add = True)
  updated_at = models.DateTimeField(auto_now = True)

  def __repr__(self):
    return " first_name: {}, last_name: {}, email: {}, age: {}, created_at: {}, updated_at: {} ".format(self.first_name,self.last_name,self.email,self.age,self.created_at,self.updated_at)

    