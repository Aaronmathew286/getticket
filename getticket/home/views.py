
# Create your views here.
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User
from .models import category,films

def index(request):
    data=category.objects.all()
    print(data) 
    return render(request,"index.html",{"pro":data})
    

def about(request):
    return render(request,"about.html")

def login(request):
    if request.method == "POST":
        username = request.POST["uname"]
        password = request.POST["pname"]
        check = auth.authenticate(username=username, password=password)
        if check is not None:
            auth.login(request, check)
            return redirect("/")
        else:
            msg = "Invalid Username Or Password"
            return render(request, "login.html", {"msg": msg})
    else:
        return render(request, "login.html")


def register(request):
    if request.method == "POST":
        name = request.POST["fname"]
        username = request.POST["uname"]
        email = request.POST["ename"]
        password = request.POST["pname"]
        repassword = request.POST["re-pname"]
        ucheck = User.objects.filter(username=username)
        echeck = User.objects.filter(email=email)
        if ucheck:
            msg = "Username Exits"
            return render(request, "register.html", {"msg": msg})
        elif echeck:
            msg = "Email Exits"
            return render(request, "register.html", {"msg": msg})
        elif password == "" or password != repassword:
            msg = "Invalid Password"
            return render(request, "register.html", {"msg": msg})
        else:
            user = User.objects.create_user(
                first_name=name, username=username, email=email, password=password)
            user.save();
            return redirect("/")
    else:
        return render(request, "register.html")


def logout(request):
    auth.logout(request)
    return redirect("/")


def details(request):
    id=request.GET["id"]
    data=films.objects.filter(id=id)
    return render(request,"details.html",{"pro":data})
   



def final(request):
    id=request.GET["id"]
    print(id)
    if request.method=="POST":
        data=category.objects.all()
        fil=films.objects.filter(id=id)
        seatsneed=request.POST["seatsneed"]
        seat=films.objects.get(id=id)
        t1=int(seat.seatsavai)-int(seatsneed)
        films.objects.filter(id=id).update(seatsavai=t1)
        ev=films.objects.get(id=id)
        total=int(seatsneed)*int(ev.price)

    return render(request,"final.html",{"pro":data,"film":fil,"total":total})

