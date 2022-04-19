from django.contrib.auth.models import User
from taskTrackerApp.models import *
from taskTrackerApp.libraries.library import *





def email_send(deadlineEmailList,emailList):
    
    #at the end of the day send this mail to team leaders
    send_mail('Status Report For The Day', 'Hi sir plz check the report for the day', 'a4akshaykn@gmail.com', emailList,fail_silently=False)
    send_mail('Status Report For The Day', 'Hi sir plz check the report for the day', 'a4akshaykn@gmail.com', deadlineEmailList,fail_silently=False)
    return True

emailList=[]
deadlineEmailList=[]
users=User.objects.all()
for i in users:
        emailList.append(i.email)
dateToday=datetime.datetime.now().date()
for things in Task.objects.all():
    if things.end_date < dateToday:
        for fields in Members.objects.all():
            if fields.member == things.team_member:
                deadlineEmailList.append(fields.email)
deadlineEmailList=deadlineEmailList+emailList
email_send(deadlineEmailList,emailList)