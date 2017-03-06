from django.shortcuts import render
from django.views.generic import DetailView
from .models import Project


# Create your views here.
class ProjectdetailView(DetailView):
    model = Project
