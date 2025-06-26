from django.db import models # This import is necessary for Django models
from djang0.contrib.auth.models import User # Importing User model from Django's auth system

# Create your models here.
class_UserProfile(models.Model): # Defining the UserProfile model
    user = models.OneToOneField(User, on_delete=models.CASCADE) # One-to-one relationship with the User model
    bio = models.TextField(blank=True, null=True) # Bio field for the user profile
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True) # Profile picture field, allows image uploads
    
    def __str__(self):
        return self.user.username # String representation of the UserProfile model, returns the username of the user

class Survey(models.Model): # Defining the Survey model
    title = models.CharField(max_length=200) # Title of the survey
    description = models.TextField() # Description of the survey
    created_by = models.ForeignKey(User, on_delete=models.CASCADE) # Foreign key to the User model, linking the survey to its creator
    created_at = models.DateTimeField(auto_now_add=True) # Automatically set the field to now when the object is first created
    updated_at = models.DateTimeField(auto_now=True) # Automatically set the field to now every time the object is saved
    is_active = models.BooleanField(default=True) # Indicates if the survey is active or not
    
    def __str__(self):
        return self.title # String representation of the Survey model, returns the title of the survey
    
    def get_absolute_url(self):
        return reverse('surveys:survey_detail', args=[str(self.id)]) # Returns the URL to access a specific survey detail page
    
    
class Question(models.Model):
        
    QUESTION_TYPES = [
        ('text', 'Text Answer'),
        ('single', 'Single Choice'),
        ('multiple', 'Multiple Choice'),
    ]
        
survey = models.ForeignKey(Survey, on_delete=models.CASCADE, related_name='questions') # Foreign key to the Survey model, linking the question to its survey
text = models.TextField() # Text of the question
question_type = models.CharField(max_length=20, choices=QUESTION_TYPES) # Type of the question, with predefined choices
is_required = models.BooleanField(default=True) # Indicates if the question is required to be answered
order = models.IntegerField(default=0) # Order of the question in the survey, useful for sorting

class Meta:
    ordering = ['order'] # Default ordering of questions by their order field
    
def __str__(self):
    return f"{self.survey.title} - {self.text[:50]}" # String representation of the Question model, returns the survey title and questiontext


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices') # Foreign key to the Question model, linking the choice to its question
    text = models.CharField(max_length=200) # Text of the choice
    value = models.CharField(max_length=100) # Value of the choice, can be used for storing specific data related to the choice
    
    def __str__(self):
        return self.text # String representation of the Choice model, returns the text of the choice
    
    
class Response(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, related_name='responses') # Foreign key to the Survey model, linking the response to its survey
    respondent = models.ForeignKey(User, on_delete=models.CASCADE, related_name='responses') # Foreign key to the User model, linking the response to its respondent
    created_at = models.DateTimeField(auto_now_add=True) # Automatically set the field to now when the response is created
    
    def __str__(self):
        return f"Response to {self.survey.title} by {self.respondent or 'Anonymous'}" # String representation of the Response model, returns the survey title and respondent username
    
class Answer(models.Model):
    response = models.ForeignKey(Response, on_delete=models.CASCADE, related_name='answers') # Foreign key to the Response model, linking the answer to its response
    question = models.ForeignKey(Question, on_delete=models.CASCADE,) # Foreign key to the Question model, linking the answer to its question
    text_answer = models.TextField(blank=True, null=True) # Text answer for text type questions
    choice_answer = models.ManyToManyField(Choice, blank=True) # Many-to-many field for storing multiple choice answers
    
    def __str__(self):
        return f"Answer to {self.question.text[:50]}" # String representation of the Answer model, returns the question text for which the answer is given