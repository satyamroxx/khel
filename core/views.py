from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .models import CSTEST,CTEST,CPPTEST,JAVATEST,PYTHONTEST,result
import datetime
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render





@login_required
def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


@login_required
def javaq(request):
    context = {
        'query_results' : JAVATEST.objects.all()
    }
    return render(request, 'javaq.html',context)


    


@login_required
def javar(request):
    if request.method=="POST":
        chosenOption = ''
        correctAns = ''
        c=0
        x=1
        for ans in JAVATEST.objects.all():
            chosenOption=str(request.POST.get("java"+str(x)))
            correctAns=str(ans.ANSWER)
            if chosenOption==correctAns:
                c=c+1
            x=x+1
        article = result()
        article.sid = request.user
        article.marks = c
        article.subject = 'JAVA'
        article.tdate = str(datetime.datetime.now())
        article.save()      
          
        context = {
            'query_results1' :c
        }
    return render(request, 'result.html',context)       


@login_required
def csq(request):
    context = {
        'query_results' : CSTEST.objects.all()
    }
    return render(request, 'csq.html',context)

@login_required
def csr(request):
    if request.method=="POST":
        chosenOption = ''
        correctAns = ''
        c=0
        x=1
        for ans in CSTEST.objects.all():
            chosenOption=str(request.POST.get("java"+str(x)))
            correctAns=str(ans.ANSWER)
            if chosenOption==correctAns:
                c=c+1
            x=x+1
        article = result()
        article.sid = request.user
        article.marks = c
        article.subject = 'C#'
        article.tdate = str(datetime.datetime.now())
        article.save()     
        context = {
            'query_results1' :c
        }
    return render(request, 'result.html',context) 


@login_required
def cq(request):
    context = {
        'query_results' : CTEST.objects.all()
    }
    return render(request, 'cq.html',context)


@login_required
def cr(request):
    if request.method=="POST":
        chosenOption = ''
        correctAns = ''
        c=0
        x=1
        for ans in CTEST.objects.all():
            chosenOption=str(request.POST.get("java"+str(x)))
            correctAns=str(ans.ANSWER)
            if chosenOption==correctAns:
                c=c+1
            x=x+1
        article = result()
        article.sid = request.user
        article.marks = c
        article.subject = 'C'
        article.tdate = str(datetime.datetime.now())
        article.save()     
        context = {
            'query_results1' :c
        }
    return render(request, 'result.html',context)       


@login_required
def cppq(request):
    context = {
        'query_results' : CPPTEST.objects.all()
    }
    return render(request, 'cppq.html',context)


@login_required
def cppr(request):
    if request.method=="POST":
        chosenOption = ''
        correctAns = ''
        c=0
        x=1
        for ans in CPPTEST.objects.all():
            chosenOption=str(request.POST.get("java"+str(x)))
            correctAns=str(ans.ANSWER)
            if chosenOption==correctAns:
                c=c+1
            x=x+1
        article = result()
        article.sid = request.user
        article.marks = c
        article.subject = 'C++'
        article.tdate = str(datetime.datetime.now())
        article.save()     
        context = {
            'query_results1' :c
        }
    return render(request, 'result.html',context) 



@login_required
def pythonq(request):
    context = {
        'query_results' : PYTHONTEST.objects.all()
    }
    return render(request, 'pythonq.html',context)


@login_required
def pythonr(request):
    if request.method=="POST":
        chosenOption = ''
        correctAns = ''
        c=0
        x=1
        for ans in PYTHONTEST.objects.all():
            chosenOption=str(request.POST.get("java"+str(x)))
            correctAns=str(ans.ANSWER)
            if chosenOption==correctAns:
                c=c+1
            x=x+1
        article = result()
        article.sid = request.user
        article.marks = c
        article.subject = 'Python'
        article.tdate = str(datetime.datetime.now())
        article.save()     
        context = {
            'query_results1' :c
        }
    return render(request, 'result.html',context)      


@login_required
def mini(request):
    contact_list = result.objects.filter(sid=request.user)
    paginator = Paginator(contact_list, 5) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)

    return render(request,'mini.html', {"contacts": contacts})
       