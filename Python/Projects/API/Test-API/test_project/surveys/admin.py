from django.contrib import admin
from .models import Survey, Question, Choice, Response, Answer  # Import models to register them in the admin site

# Register your models here.

class ChoiceInLine(admin.TabularInline):
    model = Choice  # Specify the model to use for this inline
    extra = 1  # Number of empty forms to display for adding new choices
    
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('survey', 'text', 'question_type', 'is_required', 'order')  # Fields to display in the admin list view
    list_filter = ('survey', 'question_type')  # Fields to filter by in the admin list view
    search_fields = ('text',)  # Fields to search by in the admin list view
    inlines = [ChoiceInLine]  # Inline model for choices associated with questions
    
class SurveyAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_by', 'created_at', 'is_active')  # Fields to display in the admin list view
    list_filter = ('is_active', 'created_by')  # Fields to filter by in
    search_fields = ('title', 'description')  # Fields to search by in the admin list view
    
class AnswerInLine(admin.TabularInline):
    model = Answer  # Specify the model to use for this inline
    extra = 1  # Number of empty forms to display for adding new answers
    readonly_fields = ('question', 'text_answer', 'choice_answer')  # Fields to display as read-only in the inline form
    can_delete = False  # Disable the ability to delete answers in the inline form
    
class ResponseAdmin(admin.ModelAdmin):
    inlines = [AnswerInLine]  # Inline model for answers associated with responses
    list_display = ('survey', 'respondent', 'created_at')  # Fields to display in the admin list view
    list_filter = ('survey', 'created_at')  # Fields to filter by in the admin list view
    search_fields = ('survey__title', 'respondent__username')  # Fields to search by in the admin list view
    
admin.site.register(Survey, SurveyAdmin)  # Register the Survey model with the admin site
admin.site.register(Question, QuestionAdmin)  # Register the Question model with the admin site
admin.site.register(Response, ResponseAdmin)  # Register the Response model with the admin site

