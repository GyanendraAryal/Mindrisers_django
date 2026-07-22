from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import TodoList

# Create your views here.
# def index(request):
#     return HttpResponse("Welcome this is index page!")


def home(request):
    users = [
        {
            "id": 1,
            "name": "Alice Johnson",
            "age": 25,
            "email": "alice@example.com",
            "city": "New York",
        },
        {
            "id": 2,
            "name": "Bob Smith",
            "age": 13,
            "email": "bob@example.com",
            "city": "London",
        },
        {
            "id": 3,
            "name": "Charlie Brown",
            "age": 22,
            "email": "charlie@example.com",
            "city": "Sydney",
        },
        {
            "id": 4,
            "name": "David Wilson",
            "age": 8,
            "email": "david@example.com",
            "city": "Toronto",
        },
        {
            "id": 5,
            "name": "Emma Davis",
            "age": 24,
            "email": "emma@example.com",
            "city": "Paris",
        },
        {
            "id": 6,
            "name": "Frank Miller",
            "age": 35,
            "email": "frank@example.com",
            "city": "Berlin",
        },
        {
            "id": 7,
            "name": "Grace Taylor",
            "age": 27,
            "email": "grace@example.com",
            "city": "Tokyo",
        },
        {
            "id": 8,
            "name": "Henry Anderson",
            "age": 31,
            "email": "henry@example.com",
            "city": "Dubai",
        },
        {
            "id": 9,
            "name": "Isabella Thomas",
            "age": 23,
            "email": "isabella@example.com",
            "city": "Rome",
        },
        {
            "id": 10,
            "name": "Jack White",
            "age": 29,
            "email": "jack@example.com",
            "city": "Singapore",
        },
        {
            "id": 11,
            "name": "Karen Harris",
            "age": 26,
            "email": "karen@example.com",
            "city": "Madrid",
        },
        {
            "id": 12,
            "name": "Liam Martin",
            "age": 32,
            "email": "liam@example.com",
            "city": "Amsterdam",
        },
        {
            "id": 13,
            "name": "Mia Thompson",
            "age": 21,
            "email": "mia@example.com",
            "city": "Seoul",
        },
        {
            "id": 14,
            "name": "Noah Garcia",
            "age": 14,
            "email": "noah@example.com",
            "city": "Chicago",
        },
        {
            "id": 15,
            "name": "Olivia Martinez",
            "age": 28,
            "email": "olivia@example.com",
            "city": "Los Angeles",
        },
        {
            "id": 16,
            "name": "Peter Robinson",
            "age": 12,
            "email": "peter@example.com",
            "city": "Melbourne",
        },
        {
            "id": 17,
            "name": "Queenie Lewis",
            "age": 24,
            "email": "queenie@example.com",
            "city": "Dublin",
        },
        {
            "id": 18,
            "name": "Ryan Walker",
            "age": 15,
            "email": "ryan@example.com",
            "city": "Kathmandu",
        },
        {
            "id": 19,
            "name": "Sophia Hall",
            "age": 29,
            "email": "sophia@example.com",
            "city": "Bangkok",
        },
        {
            "id": 20,
            "name": "Thomas Young",
            "age": 36,
            "email": "thomas@example.com",
            "city": "San Francisco",
        },
    ]
    context = {
        "body": "Welcome. This is index page",
        "title": "Index page",
        "users": users,
    }
    return render(request, "home.html", context)


def contact(request):
    return render(request, "contact.html")


def task(request):
    tasks = TodoList.objects.all()
    # print(task)
    context = {"tasks": tasks}
    return render(request, "task.html", context)


def create(request):
    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        description = request.POST.get("description", "").strip()
        status = "status" in request.POST
        if not title or not description:
            context={
                "error":"Both fields are required!!"
            }
            return render(request, "create.html", context)
        else:
            TodoList.objects.create(title=title, description=description, status=status)
            return redirect("task")
    return render(request, "create.html")


def edit(request, id):
    task = get_object_or_404(TodoList, id=id)
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        status = "status" in request.POST

        task.title = title
        task.description = description
        task.status = status

        task.save()

        return HttpResponse("Task Updated successfully")
    return render(request, "edit.html", {"task": task})


def toggle(request,id):
    task = get_object_or_404(TodoList, id=id)
    if request.method == "POST":
        task.status = not task.status
        task.save()
        return redirect("task")


def delete(request,id):
    context = {"message": "Todo Deleted Successfully"}
    task= get_object_or_404(TodoList,id=id)
    task.delete()
    return redirect( "/task/")
