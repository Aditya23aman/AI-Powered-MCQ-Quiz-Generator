from django.shortcuts import render
from .services import  generate_questions, get_all_questions, create_quiz_txt

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world.")

def home(request):

    if request.method == "POST":
        text = request.POST['text']
        questions = generate_questions(text)
        context = {'questions': questions}
        return render(request, 'home.html', context)

    return render(request, 'home.html')

def history(request):
    if request.method == "GET":
        history_data = get_all_questions()
        # print(history_data)
        # print(type(history_data))
        context = {"data": history_data}
        
        return render(request, 'history.html', context)
    
    if request.method =="POST":
        quiz_id = request.POST.get('quiz_id')
        create_quiz_txt(quiz_id)
        return render(request, 'success.html')
    


def header(request):
    return render(request, "header.html")



