from django.shortcuts import render,HttpResponse,redirect
from firstapp.forms import SiteUserForm,UserRoleForm,NewSiteUserForm
from firstapp.models import SiteUser,UserRole,NewSiteUser
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.hashers import make_password,check_password
import os

# Create your views here.


def index(request):
    return HttpResponse("<h1> Welcome to First Response</h1>")

def home(request):
    return render(request,"home.html")

def about(request):
    name ="jitin"
    names=["jitin","Nitin","Shikha","tushar"]
    return render(request,"about.html",{'n': name,'l':names})

def index2(request):
    return render(request,"index.html")

def index3(request):
    return render(request,"index3.html")

def signup(request):

    if request.method=="POST":
        form=SiteUserForm(request.POST)
        f= form.save(commit=False)
        f.userFullName = request.POST["t1"]
        f.userMobile = request.POST["t2"]
        f.userPassword = make_password(request.POST["p1"])
        f.userEmail = request.POST["t3"]
        f.isActive = True
        f.roleId_id = 2
        f.save()
        return render(request, "signup.html",{'success':True})
    return render(request, "signup.html")


def signup2(request):
    if request.method=="POST":
        form=UserRoleForm(request.POST)
        f=form.save(commit=False)
        f.isActive = True
        f.roleName= request.POST["t1"]
        f.save()
        return  render(request,"signup2.html",{'success':True})
    return render(request,"signup2.html")

#get(),filter(),all()
def datafetch(request):
    data=SiteUser.objects.all()
    #data = SiteUser.objects.filter(isActive=1)
    #data = SiteUser.objects.get(userEmail="lksdcv@gmail.com")
    return render(request,"viewdata.html",{'d':data})


def signup3(request):
    if request.method=="POST":
        form=NewSiteUserForm(request.POST)
        f= form.save(commit=False)
        try:
            if request.FILES["img1"]:
                my_file = request.FILES["img1"]
                fs = FileSystemStorage()
                file_name = fs.save(my_file.name,my_file)
                img1 = fs.url(file_name)
                img1 = my_file.name
        except:
            pass

        f.userFullName = request.POST["t1"]
        f.userMobile = request.POST["t2"]
        f.userPassword = make_password(request.POST["p1"])
        f.userEmail = request.POST["t3"]
        f.image = img1
        f.isActive = True
        f.roleId_id = 2
        f.save()
        return render(request,"signup3.html",{'success':True})
    return render(request, "signup3.html")


def dataupdate(request):
    oldemail=request.GET["id"]
    data = SiteUser.objects.get(userEmail=oldemail)
    if request.method=="POST":

        Name = request.POST["t1"]
        mobile = request.POST["t2"]
        passw = make_password(request.POST["p1"])
        emailId = oldemail
        updateD =SiteUser(userEmail=emailId,userPassword=passw,userMobile=mobile,userFullName=Name)
        updateD.save(update_fields=["userFullName","userMobile","userPassword"])
        return redirect("/viewdata/")

    return render(request, "updatedata.html",{"e":data.userEmail,"n":data.userFullName,"pas":data.userPassword,"m":data.userMobile})


def deleteData(request):
    emailid = request.GET["id"]
    data = SiteUser.objects.get(userEmail = emailid)
    data.delete()
    return redirect("/viewdata/")


def imagedataupdate(request):
    oldemail=request.GET["id"]
    data = NewSiteUser.objects.get(userEmail=oldemail)
    if request.method=="POST":

        Name = request.POST["t1"]
        mobile = request.POST["t2"]
        passw = make_password(request.POST["p1"])
        emailId = oldemail
        try:
            if request.FILES:
                os.remove("media/" + data.image)
                my_file = request.FILES["img1"]
                fs = FileSystemStorage()
                file_name = fs.save(my_file.name,my_file)
                img1 = fs.url(file_name)
                img1 = my_file.name
                updateD = NewSiteUser(userEmail=emailId, userPassword=passw, userMobile=mobile, userFullName=Name,
                                   image=img1)
                updateD.save(update_fields=["userFullName", "userMobile", "userPassword", "image"])
                return redirect("/imageviewdata/")

        except:
            pass
        updateD =NewSiteUser(userEmail=emailId,userPassword=passw,userMobile=mobile,userFullName=Name)
        updateD.save(update_fields=["userFullName","userMobile","userPassword"])
        return redirect("/imageviewdata/")

    return render(request, "imagedata.html",{"e":data.userEmail,"n":data.userFullName,"pas":data.userPassword,"m":data.userMobile,"i":data.image})

def imagedatafetch(request):
    data=NewSiteUser.objects.all()
    #data = SiteUser.objects.filter(isActive=1)
    #data = SiteUser.objects.get(userEmail="lksdcv@gmail.com")
    return render(request,"imageviewd.html",{'d':data})


def imgdeleteData(request):
    emailid = request.GET["id"]
    data = NewSiteUser.objects.get(userEmail = emailid)
    imagepath = data.image
    os.remove("media/" + imagepath)
    data.delete()
    return redirect("/imageviewdata/")