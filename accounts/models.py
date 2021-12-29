from django.contrib.auth.models import AbstractUser
from django.db import models
from multiselectfield import MultiSelectField

class CustomUser(AbstractUser):
    gender        = models.CharField(max_length=26,choices=[('Male', 'Male'), ('Female', 'Female')],default='Male')
    phonenumber   = models.IntegerField(null=True)
    profilePicture= models.ImageField(upload_to ='ProfilePictures/', default='ProfilePictures/default.jpg')
    interests     = MultiSelectField(max_length=26,null=True, choices=[  ('Reading', 'Reading'), ('Cycling', 'Cycling'),
                                                          ('Hiking','Hiking'), ('Drawing', 'Drawing'),('Photography', 'Photography'),
                                                               ('Swimming','Swimming'),('Sleeping','Sleeping'),('Sports','Sports'),('Gaming','Gaming')])

    def __str__(self):
        return self.email