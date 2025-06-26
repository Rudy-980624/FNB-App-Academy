from django.test import TestCase
from django.urls import reverse
from .models import Survey, Question, Answer
from django.contrib.auth.models import User

# Create your tests here.

class SurveyModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.survey = Survey.objects.create(
            title='Test Survey',
            description='This is a test survey.',
            created_by=self.user
        )
        self.question = Question.objects.create(
            survey=self.survey,
            text='What is your favorite color?',
            question_type='text',
            is_required=True,
            order=1
        )

    def test_survey_creation(self):
        self.assertEqual(self.survey.title, 'Test Survey')
        self.assertEqual(self.survey.description, 'This is a test survey.')
        self.assertEqual(self.survey.created_by, self.user)

    def test_question_creation(self):
        self.assertEqual(self.question.text, 'What is your favorite color?')
        self.assertEqual(self.question.question_type, 'text')
        self.assertTrue(self.question.is_required)
        
    def test_survey_str(self):
        self.assertEqual(str(self.survey), 'Test Survey')
    def test_question_str(self):
        self.assertEqual(str(self.question), f"{self.survey.title} - {self.question.text[:50]}")
    def test_get_absolute_url(self):
        self.assertEqual(self.survey.get_absolute_url(), reverse('surveys:survey_detail', args=[str(self.survey.id)]))
    def test_question_ordering(self):
        question2 = Question.objects.create(
            survey=self.survey,
            text='What is your favorite animal?',
            question_type='text',
            is_required=True,
            order=2
        )
        questions = self.survey.questions.all()
        self.assertEqual(list(questions), [self.question, question2])
        
class SurveyViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        self.survey = Survey.objects.create(
            title='Test Survey',
            description='This is a test survey.',
            created_by=self.user
        )

    def test_survey_list_view(self):
        response = self.client.get(reverse('surveys:survey_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'surveys/survey_list.html')
        self.assertContains(response, 'Test Survey')

    def test_survey_detail_view(self):
        response = self.client.get(reverse('surveys:survey_detail', args=[self.survey.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'surveys/survey_detail.html')
        self.assertContains(response, 'Test Survey')
        
    def test_survey_create_view(self):
        response = self.client.get(reverse('surveys:survey_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'surveys/survey_form.html')
        
        data = {
            'title': 'New Survey',
            'description': 'This is a new survey.',
            'created_by': self.user.id
        }
        response = self.client.post(reverse('surveys:survey_create'), data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('surveys:survey_list'))
        self.assertTrue(Survey.objects.filter(title='New Survey').exists())
    def test_survey_update_view(self):
        response = self.client.get(reverse('surveys:survey_update', args=[self.survey.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'surveys/survey_form.html')
        
        data = {
            'title': 'Updated Survey',
            'description': 'This is an updated survey.',
            'created_by': self.user.id
        }
        response = self.client.post(reverse('surveys:survey_update', args=[self.survey.id]), data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('surveys:survey_detail', args=[self.survey.id]))
        self.survey.refresh_from_db()
        self.assertEqual(self.survey.title, 'Updated Survey')
    def test_survey_delete_view(self):
        response = self.client.get(reverse('surveys:survey_delete', args=[self.survey.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'surveys/survey_confirm_delete.html')
        response = self.client.post(reverse('surveys:survey_delete', args=[self.survey.id]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('surveys:survey_list'))
        self.assertFalse(Survey.objects.filter(id=self.survey.id).exists())
        
    def test_user_survey_list_view(self):
        response = self.client.get(reverse('surveys:user_survey_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'surveys/user_survey_list.html')
        self.assertContains(response, 'Test Survey')
        
    def test_survey_response_view(self):
        response = self.client.get(reverse('surveys:survey_response', args=[self.survey.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'surveys/survey_response.html')
        self.assertContains(response, 'Test Survey')
        
        data = {
            'question_1': 'Blue'
        }
        response = self.client.post(reverse('surveys:survey_response', args=[self.survey.id]), data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('surveys:survey_detail', args=[self.survey.id]))
        self.assertTrue(Answer.objects.filter(question=self.question, response__respondent=self.user).exists())
        
    def test_survey_response_list_view(self):
        response = self.client.get(reverse('surveys:survey_response_list', args=[self.survey.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'surveys/survey_response_list.html')
        self.assertContains(response, 'Test Survey')
        
        # Check if the response is listed
        self.assertTrue(Answer.objects.filter(question=self.question, response__survey=self.survey).exists())
    def test_survey_response_detail_view(self):
        response = self.client.get(reverse('surveys:survey_response_detail', args=[self.survey.id, self.user.id]))
        self.assertEqual(response.status_code, 200)
        
class SurveyResponseModelTests(TestCase):   
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.survey = Survey.objects.create(
            title='Test Survey',
            description='This is a test survey.',
            created_by=self.user
        )
        self.question = Question.objects.create(
            survey=self.survey,
            text='What is your favorite color?',
            question_type='text',
            is_required=True,
            order=1
        )
        self.response = Response.objects.create(
            survey=self.survey,
            respondent=self.user
        )
        self.answer = Answer.objects.create(
            question=self.question,
            response=self.response,
            text='Blue'
        )

    def test_response_creation(self):
        self.assertEqual(self.response.survey, self.survey)
        self.assertEqual(self.response.respondent, self.user)

    def test_answer_creation(self):
        self.assertEqual(self.answer.question, self.question)
        self.assertEqual(self.answer.response, self.response)
        self.assertEqual(self.answer.text, 'Blue')