from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.fields import IntegerField
from django_mysql.models import ListTextField
from multiselectfield import MultiSelectField

class Event(models.Model):
    EventName        = models.CharField(max_length=256)
    EventDescription = models.CharField(max_length=256)
    EventLocation    = models.CharField(max_length=256)
    EventCategory    = MultiSelectField(max_length=26, choices=[  ('Reading', 'Reading'), ('Cycling', 'Cycling'),
                                                                  ('Hiking','Hiking'), ('Drawing', 'Drawing'),('Photography', 'Photography'),
                                                                  ('Swimming','Swimming'),('Sleeping','Sleeping'),('Sports','Sports'),('Gaming','Gaming')])
    EventStartTime  = models.DateTimeField()
    EventCreator    = models.ForeignKey(get_user_model(),on_delete=models.CASCADE, null=True)
    EventParticipants = ListTextField(  base_field=IntegerField(),
                                        size=50,  null=True) 