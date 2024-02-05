from django.db                      import models
from django.db.models.signals       import post_save
from django.contrib.auth.models     import User
from django.contrib.auth            import authenticate, login, logout
from django.shortcuts               import render, redirect



# Create your models here.

