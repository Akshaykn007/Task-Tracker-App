# -*- coding: utf-8 -*-

__author__ = "Akshay K N"
__copyright__ = "Copyright 2022 Frejun."
__title__ = "Task-Tracker-APP"
__version__ = "0.0"

from django.shortcuts import render
from requests import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from taskTrackerApp.schemas import CreateTeamSchema,TeamAvailabilitySchema,CreateTaskSchema,TaskEditorSchema,TaskUpdatesSchema
from taskTrackerApp.worker import CreateTeamHandler,TeamAvailabilityHandler,CreateTaskHandler,TaskEditorHandler,TaskUpdatesHandler
from taskTrackerApp.libraries.library import *
from taskTrackerApp.worker.email_sender import *

class PingAPI(APIView):
    def get(self,request):
        return JsonResponse({
            'data': 'pong'
        })

class CreateTeam(APIView):
    permission_classes = [IsAuthenticated,]
    def post(self,request):
        handler = CreateTeamHandler(request)
        response = handler.handle_request(CreateTeamSchema._lin_function)
        return response

class TeamAvailability(APIView):
    permission_classes = [IsAuthenticated,]
    def get(self,request):
        id = request.query_params.get('team_id')
        handler = TeamAvailabilityHandler(request,int(id))
        response = handler.handle_request(TeamAvailabilitySchema._lin_function)
        return response
        
class CreateTask(APIView):
    permission_classes = [IsAuthenticated,]
    def post(self,request):
        handler = CreateTaskHandler(request)
        response = handler.handle_request(CreateTaskSchema._lin_function)
        return response
        
class TaskEditor(APIView):
    def patch(self,request,task_id,field):
        try:
            user=User.objects.get(username=request.data["username"])
            if str(user) == request.data["username"] and user.check_password(request.data["password"]):
                check=1
            else:
                check=0
        except:
            check=1
        handler = TaskEditorHandler(request,task_id,field,check)
        response = handler.handle_request(TaskEditorSchema._lin_function)
        return response

class TaskUpdates(APIView):
    permission_classes = [IsAuthenticated,]
    def get(self,request,year,month,day):
        handler = TaskUpdatesHandler(request,year,month,day)
        response = handler.handle_request(TaskUpdatesSchema._lin_function)
        # send_mail('Status Report For The Day', 'Hi sir plz check the report for the day', 'unknown@gmail.com', emailList,fail_silently=False)
        return response

