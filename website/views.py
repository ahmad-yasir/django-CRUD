from django.shortcuts import render, redirect
from django.template import loader
from .models import Member
from .forms import MemberForm
from django.contrib import messages
 
# Create your views here.
def home(request):
    db = Member.objects.all
    return render(request, 'home.html', {"db" : db})

def join(request):
    if request.method == "POST":
        form = MemberForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, "Your Form has been submitted successfully")
            return redirect('home')
        else:
            fname = request.POST['fname']
            lname = request.POST['lname']
            age = request.POST['age']
            email = request.POST['email']
            passwd = request.POST['passwd']

            messages.success(request, "There is an Error! Try again...")
            return render(request, 'join.html', {
                'fname' : fname,
                'lname' : lname,
                'age' : age,
                'email' : email,
                'passwd' : passwd, 
            })
        
    else:
        return render(request, 'join.html', {})


def delete_event(request,event_id):
    event = Member.objects.get(pk=event_id)
    event.delete()

    return redirect("home")

def edit(request, event_id):
    event = Member.objects.get(pk=event_id)
    form = MemberForm(request.POST or None, instance=event)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request,'update.html', {'event' : event, 'form': form})