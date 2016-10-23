from django.shortcuts import render, redirect
from .models import Course, Description, Comment

# Create your views here.
def index(request):
    context = {"courses": Course.objects.all()}
    return render(request, "new_courses/index.html", context)

def addcourse(request):
    newCourse = Course.objects.create(name=request.POST["name"])
    Description.objects.create(course_id=newCourse, description=request.POST["description"])
    return redirect("/")

def confirm(request):
    context = {"course": Course.objects.all().filter(id = request.POST["id"])[0]}
    return render(request, "new_courses/confirm.html", context)

def deletecourse(request):
    Course.objects.filter(id = request.POST["id"]).delete()
    return redirect("/")

def comments(request):
    context = {"comments": Comment.objects.all().filter(course_id = request.POST["id"])}
    return render(request, "new_courses/comments.html", context)

def newcomment(request):
    courseToComment = Course.objects.all().get(id = request.POST["id"]) # can either use get since it returns one object, or filter which returns query set and have to use [0] since it's the first and only object in there
    Comment.objects.create(course_id = courseToComment, comment = request.POST["comment"]) # course_id has to be an object hence the above line. Can't just throw the relevant id number for the course in here!!
    return redirect("/")
