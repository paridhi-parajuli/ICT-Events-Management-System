from django.db import models
from django.utils import timezone
import datetime
from multiselectfield import MultiSelectField

ict_room_list=(
	(1,'lecture 1'),(2,'lecture2'),(3,'lecture3') ,(4,'lecture4'))

class Event(models.Model):
	
    event_name = models.CharField(max_length=200)
    event_date = models.DateField('event date')
    start_time=models.TimeField(null=True,help_text="24hrs format hh:mm:ss")
    end_time=models.TimeField(null=True,help_text="24hrs format hh:mm:ss")
    event_registry_date=models.DateTimeField(auto_now_add=True)
    event_rooms=MultiSelectField(choices=ict_room_list)
    event_organizers=models.CharField(null=True,max_length=100)
    contact=models.BigIntegerField(null=True)
    description=models.TextField(max_length=200,default='none')



    
        
   


    def __str__(self):
    	return self.event_name



