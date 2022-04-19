from taskTrackerApp.libraries.library import *
from taskTrackerApp.models import *
from taskTrackerApp.schemas.schemas import TaskEditorSchema

class TrackerServiceHandler(ABC):
    def __init__(self, request):
        self.request = request
        self.error_msg = None
        self.failure = False
        self.request_data = request.data
        self.success_response = None
        self.failed_response = None
        self.error_response = None
        self.is_request_valid = False
        self.response_data = {}

    def handle_request(self,_lineup_fns):
        for _fn in _lineup_fns:
            if hasattr(self, _fn):
                method = getattr(self,_fn)()
                if method !=1:
                    self.failure=True
                if self.failure:
                    self.failed_method = method.__name__
                    print("Method {} failed!".format(_fn))
                    break
            else:
                print("Method {} undefined!".format(_fn))
                self.failure = True
                break
        _response = self.build_response()
        return _response

    def build_response(self):
        print("Building response object")
        if self.is_request_valid:
            self.error_response = JsonResponse(
                status=400, data={"status": "fail", "error": self.error_msg}
            )
            return self.error_response
        if self.failure:
            self.failed_response = JsonResponse(
                status=500, data={"status": "error", "error_message": "server error"}
            )
            return self.failed_response
        if self.response_data.get("msg") == "Forbidden":
            self.success_response = JsonResponse(status=403, data=self.response_data)
        else:
            self.success_response = JsonResponse(status=200, data=self.response_data)
        print("BUILD RESPONSE SUCCESSFULL !!!!!!!!!!!!!!!!!")
        return self.success_response

class CreateTeamHandler(TrackerServiceHandler):
    def __init__(self,request):
        super().__init__(request)
        self.teamName=self.request_data.get("team_name")
        self.userIdList=json.loads(self.request_data.get("user_ids"))
    
    def create_team(self):
        try:
            generatedTeamId = int(str(Team.objects.all().last())) + 1
        except:
            generatedTeamId=100
        try:
            Team.objects.all().get(name=self.teamName)
        except:
            team = Team(name=self.teamName,teamId=generatedTeamId)
            team.save()
        for id in self.userIdList:
            memberName=Members.objects.get(userId=id)
            if len(TeamMembers.objects.filter(member=memberName)) == 0:
                members = TeamMembers(member=memberName,team_id=int(str(Team.objects.all().get(name=self.teamName))))
                members.save()
        self.response_data = {"success": True,"msg":"Team created successfully"}
        return 1

class TeamAvailabilityHandler(TrackerServiceHandler):
    def __init__(self,request,id):
        super().__init__(request)
        self.teamId=id
    
    def availability(self):
        members=TeamMembers.objects.filter(team_id=self.teamId)
        mylist=[]
        for user in members:
            mydict={}
            details = Members.objects.get(member=user)
            value=details.availability
            mydict[str(user)] = value
            mylist.append(mydict)
        self.response_data = {"success": True,"data":mylist}
        return 1

class CreateTaskHandler(TrackerServiceHandler):
    def __init__(self,request):
        super().__init__(request)
        self.task_name=self.request_data.get("task_name")
        self.priority=self.request_data.get("priority")
        self.start_date=self.request_data.get("start_date")
        self.end_date=self.request_data.get("end_date")
        self.team_member=self.request_data.get("team_member")
        self.status = self.request_data.get("status")
        
    def create_task(self):
        try:
            verifyTask=Task.objects.get(task_name=self.task_name)
            generatedTaskId = int(str(verifyTask.task_id))
        except:
            try:
                generatedTaskId=int(str(Task.objects.all().last())) + 1
            except:
                generatedTaskId=1
        try:
            details = Members.objects.get(member=self.team_member)
            value=details.availability
        except:
            value=False
        if value == True:
            task = Task(task_name=self.task_name,task_id=generatedTaskId,priority=self.priority,start_date=self.start_date,end_date=self.end_date,team_member=self.team_member,status=self.status)
            task.save()
            details = Members.objects.get(member=self.team_member)
            details.availability=False
            details.save()
            self.response_data={"success": True ,"msg":"Task created successfully"}
        else:
            self.response_data={"success": False ,"msg":"team member is not available"}
        return 1

class TaskEditorHandler(TrackerServiceHandler):
    def __init__(self,request,task_id,field,check):
        super().__init__(request)
        self.task_id = task_id
        self.field = field
        self.allFields = TaskEditorSchema.fields
        self.status=TaskEditorSchema.statusItems
        self.check=check

    def edit_task(self):
        field_requirement=False
        for f in self.allFields:
            if f == str(self.field) and str(self.field) in self.allFields:
                field_requirement=True
                if f == "status":
                    if self.request_data.get(str(f)) in self.status:
                        date=datetime.datetime.now().date()
                        Task.objects.filter(task_id=self.task_id).update(status=(self.request_data.get(str(f))))
                        Task.objects.filter(task_id=self.task_id).update(updated_on=date)
                        self.response_data={"success": True ,"msg":"Task updated successfully"}
                    else:
                        self.response_data={"success": False ,"msg":"Incorrect parameters"}
                elif self.check:
                    if f == "task_name":
                        Task.objects.filter(task_id=self.task_id).update(task_name=(self.request_data.get(str(f))))
                        self.response_data={"success": True ,"msg":"Task updated successfully"}
                    elif f == "priority":
                        Task.objects.filter(task_id=self.task_id).update(priority=(self.request_data.get(str(f))))
                        self.response_data={"success": True ,"msg":"Task updated successfully"}
                    elif f == "start_date":
                        Task.objects.filter(task_id=self.task_id).update(start_date=(self.request_data.get(str(f))))
                        self.response_data={"success": True ,"msg":"Task updated successfully"}
                    elif f == "end_date":
                        Task.objects.filter(task_id=self.task_id).update(end_date=(self.request_data.get(str(f))))
                        self.response_data={"success": True ,"msg":"Task updated successfully"}
                    elif f == "task_id":
                        Task.objects.filter(task_id=self.task_id).update(task_id=(self.request_data.get(str(f))))
                        self.response_data={"success": True ,"msg":"Task updated successfully"}
                    elif f == "team_member":
                        Task.objects.filter(task_id=self.task_id).update(team_member=(self.request_data.get(str(f))))
                        self.response_data={"success": True ,"msg":"Task updated successfully"}
                else:
                    self.response_data={"success": False ,"msg":"Forbidden"}
        if field_requirement:
            pass
        else:
            self.response_data={"success": False ,"msg":"Incorrect parameters"}
        return 1

class TaskUpdatesHandler(TrackerServiceHandler):
    def __init__(self,request,year,month,day):
        super().__init__(request)
        self.date = datetime.datetime(int(year),int(month),int(day)).date()

    def updates(self):
        mydict={}
        mylist=[]
        for i in Task.objects.all():
            if i.updated_on == self.date:
                mydict={}
                mydict["name"]=i.task_name
                mydict["team_member"]=i.team_member
                mydict["status"]=i.status
                mylist.append(mydict)
        self.response_data = {"success": True,"data":mylist}
        return 1