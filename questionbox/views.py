
#from django.contrib.auth.decorators import login_required
#from users.models import User
#from django.http import JsonResponse
#from .models import Question, Answer
#from django.contrib.auth.decorators import login_required
#from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Question, Answer
from .forms import QuestionForm, AnswerForm
# Create your views here.


#should I use built in class based views
#QuestionListView
#RegisteredUserListView

#Each view is responsible for doing one of two things: returning an HttpResponse object containing the content for the requested page, or raising an exception such as Http404




#def homepage(request):
    #if request.user.is_authenticated:
        #return redirect(to="question_list")
        #return render(request, "recipes/home.html")

#@login_required
def add_question(request):
    if request.method == 'POST':
        form = QuestionForm(data=request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            #question.user = request.user
            question.save()
            return redirect(to='list_questions')
    else:
        form = QuestionForm()
    return render(request, 'questionbox/add_question.html', {'form': form})

#@login_required
def list_questions(request):
    questions = Question.objects.all()
    return render(request, 'questionbox/list_questions.html', {'questions': questions}) #show all questions before selecting to see details

#@login_required
def show_question(request, pk):
    pass


#@login required
def show_answers (request, answer_id):
    pass

def favorite_question(request, pk): #jason
    pass


#def star_note(request, pk):
    #note = get_object_or_404(Note, pk=pk)
    #if note.starred:
        #note.starred = False
    #else:
        #note.starred = True
    #note.save()

    r#eturn JsonResponse({"note_starred": note.starred}, status = 200)