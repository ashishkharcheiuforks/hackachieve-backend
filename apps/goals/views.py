from django.views.decorators.csrf import csrf_exempt

from apps.boards.models import Board
from apps.columns.models import Column
from apps.columns_goals.models import Column_goal
from apps.goals.models import Goal
from hackachieve.classes.Validator import *
from hackachieve.classes.API import *

# for protected views
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny

import json
from django.core import serializers

from django.http import JsonResponse
from django.forms.models import model_to_dict


# Create your views here.
@csrf_exempt
@api_view(['post'])
@permission_classes((IsAuthenticated,))
def create(request):
    json_data = API.json_get_data(request)

    user = User.objects.get(pk=API.getUserByToken(request))

    # Empty fields valitation =========================== #
    check_user_fields = Validator.are_request_fields_valid(json_data)

    # Check is theres no empty fields
    if check_user_fields is not True:
        return API.json_response({
            "status": "error",
            "message": "Error while trying to create your goal. The following fields are empty: {}".format(
                check_user_fields),
            "type": "danger"
        })

    # if all fields are set to create our board

    if User.check_user_exists(user.id) is False:
        return API.error_user_doesnt_exists()

    # check if column exists
    if Column.check_exists(json_data['column_id']) is False:
        return API.error_goal_inexistent_column()

    # check if theres a column with the same name for this user

    if Goal.check_goal(user.id, json_data['title']) is True:
        return API.error_goal_already_exists()

    # if not, create it
    new_goal = Goal(
        user=User.objects.get(pk=user.id),
        title=json_data['title'],
        description=json_data['description'],
        duration_hrs=0,
        deadline=json_data['deadline'],
        column=Column.objects.get(pk=json_data['column_id']),
        column_day=json_data['column_day'],
        priority=json_data['priority']
    )
    new_goal.save()

    return API.json_response({
        "status": "success",
        "message": "Your new goal was created successfully!",
        "type": "success"
    })


@csrf_exempt
@api_view(['delete'])
@permission_classes((IsAuthenticated,))
def delete(request, goal_id):
    user = User.objects.get(pk=API.getUserByToken(request))

    try:
        goal = Goal.objects.get(id=goal_id, user_id=user.id)
    except Exception as e:  # and more generic exception handling on bottom
        return API.json_response({
            "status": "error",
            "message": "Error while trying to delete the goal",
            "type": "error"
        })

    c = goal.delete()

    if c:
        return API.json_response({
            "status": "success",
            "message": "Your goal was deleted!",
            "type": "success"
        })


@csrf_exempt
@api_view(['post'])
@permission_classes((IsAuthenticated,))
def attach_to_column(request, goal_id, column_id):
    json_data = API.json_get_data(request)
    print(json_data)
    user = User.objects.get(pk=API.getUserByToken(request))

    # User exists check
    if User.check_user_exists(user.id) is False:
        return API.error_user_doesnt_exists()

    # check if column exists
    if Column.check_exists(column_id) is False:
        return API.error_goal_inexistent_column()

    # column_goal = Column_goal.attach()

    return
