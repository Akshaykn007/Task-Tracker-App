import json
import random
import datetime
from abc import ABC
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from django.core.mail import send_mail