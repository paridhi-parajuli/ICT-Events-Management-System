from django.contrib import admin
from .models import Event
from django.contrib.auth.models import Group
from django import forms
from django.contrib.auth.models import User




class EventForm(forms.ModelForm):
    
    class Meta:
        model = Event 
        fields= ('event_name','event_date','event_rooms','start_time','end_time','event_organizers','contact','description')  
    

    def clean (self):
        cleaned_data = super (EventForm, self).clean()
        event_name = cleaned_data.get ('event_name')
        end_time = cleaned_data.get ('end_time') 
        event_date = cleaned_data.get ('event_date')
        start_time = cleaned_data.get('start_time')
        #event_duration = cleaned_data.get ('event_duration')
        event_rooms = cleaned_data.get ('event_rooms')
        required = Event.objects.filter (event_date = event_date)
        if self.instance.pk:
            print("We are updating", self.instance)
            required = required.exclude(pk = self.instance.pk)
        else:
            print ("This is required",required)
        #print ("Events in this date and time",required)
        print ("This is required",required)
        required = required.exclude (start_time__gt= start_time, start_time__gte= end_time)
        required = required.exclude (end_time__lte= start_time, end_time__lt= end_time)
        for event in required:
            find = False
            for room in event_rooms:
                if str(room) in event.event_rooms:
                    print ("Event with this rooms in given date and time",event )
                    raise forms.ValidationError("Event with this room in ths Event Date and Time ALready Exists")
                    find = True
                    break
                else:
                    continue
                if find:
                    break
        return cleaned_data



class EventAdmin(admin.ModelAdmin):
	list_display=('event_name','event_date','start_time','end_time','event_rooms','event_organizers','contact','description','event_registry_date')
	search_fields=['event_date','event_name','event_organizers']
	list_filter=('event_date','event_registry_date')
	form=EventForm

	




admin.site.site_header='ICT Event Management Administration'
admin.site.register(Event,EventAdmin)
admin.site.unregister(Group)
admin.site.unregister(User)
admin.site.index_title = "Events\' database"
admin.site.site_title = "ICT Events"
