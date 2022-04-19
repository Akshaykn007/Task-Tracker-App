class CreateTeamSchema:
    _required_fields = {"createTeamFields": ()}
    _lin_function = ["create_team"]

class TeamAvailabilitySchema:
    _required_fields = {"availabilityFields": ()}
    _lin_function = ["availability"]

class CreateTaskSchema:
    _required_fields = {"createTaskFields": ()}
    _lin_function = ["create_task"]

class TaskEditorSchema:
    _required_fields = {"TaskEditFields": ()}
    _lin_function = ["edit_task"]
    fields=["task_name","task_id","priority","start_date","end_date","team_member","status"]
    statusItems=["Assigned","In progress","under","review","done"]

class TaskUpdatesSchema:
    _required_fields = {"taskUpdatesFields": ()}
    _lin_function = ["updates"]