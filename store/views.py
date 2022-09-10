from django.shortcuts import HttpResponse,render,redirect,reverse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("loginuser"))
    return render(request, "index.html")


def loginuser(request):
    if(request.method=='POST'):
        usern=request.POST.get('username')
        passw= request.POST.get('password')
        user=authenticate(request,username=usern,password=passw)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect(reverse("index"))
        else:
            messages.error(request,message="Username or Password incorrect")
            return render(request, 'login.html')
    return render(request, 'login.html')



def logoutuser(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def signup(request):
    if request.method=="POST":
        usernm=request.POST.get("username")
        firstnm=request.POST.get("firstname")
        lastnm=request.POST.get("lastname")
        emailid=request.POST.get("email")
        passw=request.POST.get("password")
        try:
            user=User.objects.create_user(username=usernm,password=passw,email=emailid)
        except :
            # user already exists
            messages.error(request,message="user already exists")

        else:
            user.first_name=firstnm
            user.last_name=lastnm
            user.save()
            messages.success(request,message="Sign Up successfully")
            return HttpResponseRedirect(reverse("loginuser"))
    return render(request,"signup.html")