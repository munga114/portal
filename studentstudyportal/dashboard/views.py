from pydoc import describe
from django.shortcuts import render
from . forms import *

# Create your views here.
def home(request):
    return render(request,'dashboard/home.html')

def notes(request):
    if request.method == "POST":
        form = NotesForm(request.Post)
        if form.is_valid():
            notes = Notes(user=request.user,title=request.POST['title'],description=request.POST['description'])
            notes.save()
        messages.success(request,f"Notes added from {request.user.username} successfully")

    form = NotesForm()
    notes = Notes.objects.filter(user=request.user)
    context = {'notes':notes,'form':form}
    return render(request,'dashboard/notes.html',context)