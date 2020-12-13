from django.db import models

# Create your models here.

class UserData(models.Model):
	user_name		=	models.CharField(max_length=50, blank=False, null=False) 
	password 		=	models.CharField(max_length=50, blank=False, null=False)
	id_proof_file 	=	models.FileField(upload_to='uploads/', blank=False, null=False)
	
	def __str__(self):
		return self.user_name
	
