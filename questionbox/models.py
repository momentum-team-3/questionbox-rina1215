from django.db import models
from django.conf import settings
#from users.models import users
#from django.contrib.auth import get_user_model
#from users.models import User
#from django.contrib.auth.models import AbstractUser # Custom user or Auth user


#Users can view questions and answers
#Registered users can ask questions
#Registered users can add answers to any questions
#The question's creator can mark answers as correct
#registered users can Delete questions and its answers attached to it get deleted too
# Registered users can "star" questions and answers they like//
#Questions have a title and a body. Allow your users to use [Markdown](https://en.wikipedia.org/wiki/Markdown) for authoring question bodies. [django-markdownify](https://pypi.org/project/django-markdownify/) can turn Markdown into HTML for you. Questions cannot be edited once they have been asked. A question can be deleted by its author. If it is deleted, all associated answers should also be deleted.

#Answers just have a body and are connected to a question. Answers can also use Markdown.

#Every question and every answer should be associated with a user. A user should be able to view all their questions on a user profile page.

#Users can search the site for questions. When they search, this should search the questions and all answers for them. This should use [PostgreSQL full-text search](https://docs.djangoproject.com/en/3.0/ref/contrib/postgres/search/).

## How much of this is JavaScript and Ajax?

#"Starring" questions and answers and marking answers as correct should happen via Ajax and you will need to build a view that handles JSON to do this.

#The rest of the application can be plain old Django views, although you can use JavaScript and Ajax if you want to enhance things. Answering a question is an excellent place to use Ajax if you get a chance.

## Making this project your own

#You should try something you don't already know how to do on your project. This could be a Python or JavaScript library you haven't used before or a feature of Django you haven't tried.

#add class models to URL.py app path('', question.index, name='index')




class Question(models.Model):
    #user = models.ForeignKey(to='users.user', on_delete=models.CASCADE, related_name='questions')
    title = models.CharField(max_length=255)
    body = models.TextField()
    #time_created = models.DateTimeField(auto_now_add=True)
    #time_edited = models.DateTimeField(auto_now_add=True)
    #favorited_by= models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='star_question', blank=True)
    #starred = models.BooleanField(default=False)
    #questions_with_answers =  models.ManyToManyField('Questions', related_name='question')
    #resgistered_users = models.ManyToManyField(Authors)

    def __str__(self):
        return self.question


class Answer (models.Model):
    #user = models.ForeignKey(to='users.user', on_delete=models.CASCADE, related_name='answer')
    body = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answer')
    #created = models.DateTimeField(auto_now_add=True)
    #edited = models.DateTimeField(auto_now_add=True)
    #favorited_by = models.ManyToManyField(User, related_name='favorite_answer', blank=True)

def __str__(self):
    return self.answer