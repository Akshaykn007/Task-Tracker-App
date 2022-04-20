from __future__ import absolute_import, unicode_literals
from django.contrib.auth.models import User
from taskTrackerApp.models import *
from taskTrackerApp.libraries.library import *
from celery import shared_task
import datetime,time



@shared_task(name="sending_email")
def email_send():
    #at the end of the day send this mail to team leaders
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
    print("hello")
    try:
        send_mail('Status Report For The Day', 'Hi sir plz check the report for the day', 'unknown@gmail.com', emailList,fail_silently=False)
        send_mail('Deadline closing!!!!!!', 'Hi team, plz finish the task as early as possible!', 'unknown@gmail.com', deadlineEmailList,fail_silently=False)
    except:
        pass
    # time.sleep(60)
    return True
