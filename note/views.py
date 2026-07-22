from django.shortcuts import render, redirect,get_object_or_404
from .models import Note
from django.http import HttpResponse

# Create your views here.
def note(request):
    notes = Note.objects.all()
    context = {
        "notes":notes
    }
    return render(request,'note.html',context)

def create_note(request):
    if request.method =="POST":
        title = request.POST.get("title", "").strip()
        content = request.POST.get("content", "").strip()
        status = "status" in request.POST
        if not title or not content:
            context={
                  "error":"Both fields are required!!"
                }
            return render(request, "create_note.html", context)
        else:
            Note.objects.create(title=title,content=content,status=status)
            return redirect("note")
    return render(request,"create_note.html")

def edit_note(request,id):
    note =get_object_or_404(Note, id=id)
    if request.method=="POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        status = "status" in request.POST

        note.title = title
        note.content = content
        note.status = status

        note.save()
        return HttpResponse("Note created successfully")
    return render(request,"edit_note.html",{"note":note})

def delete_note(request,id):
    note = get_object_or_404(Note,id=id)
    note.delete()
    return redirect("note")


def toggle_note(request,id):
    note = get_object_or_404(Note, id=id)
    if request.method=="POST":
        note.status = not note.status
        note.save()
        return redirect("note")
