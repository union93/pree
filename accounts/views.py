from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import UserFrom, LoginForm
from .models import User


