from django.shortcuts import render, redirect, get_object_or_404 # Import necessary functions for rendering views and handling redirects
from django.urls import reverse_lazy # Import reverse_lazy for URL resolution
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin  # Import mixins for user authentication and permissions
from django.contrib.auth.decorators import login_required  # Import decorator for login-required views
from django.contrib import messages # Import messages framework for user notifications
from django.http import JsonResponse  # Import JsonResponse for returning JSON data
from django.db.models import Count  # Import Count for aggregating data in queries

from .models import Survey, Question, Choice, Response, Answer  # Import models from the current app
from .forms import SurveyForm, QuestionForm, ChoiceForm, ResponseForm  # Import forms for handling user input

# Create your views here.

class SurveyListView(ListView):
    models = Survey  # Specify the model to use for this view
    template_name = 'surveys/survey_list.html'  # Specify the template to render
    context_object_name = 'surveys'  # Name of the context variable to use in the template
    
    def get_queryset(self):
        return Survey.objects.filter(is_active=True)
    
# def survey_list_view(request):
#    active_surveys = Survey.objects.filter(is_active=True)  # Fetch active surveys from the database
#    context = {'surveys': active_surveys}  # Prepare context for the template
#    return render(request, 'surveys/survey_list.html', context)  # Render the template with the context

class UserSurveyListView(LoginRequiredMixin, ListView):
    model = Survey  # Specify the model to use for this view
    template_name = 'surveys/user_survey_list.html'  # Specify the template to render
    context_object_name = 'surveys'  # Name of the context variable to use in the template
    
    def get_queryset(self):
        return Survey.objects.filter(created_by=self.request.user)  # Filter surveys created by the logged-in user 
