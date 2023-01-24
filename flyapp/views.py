from django.shortcuts import render
from django.shortcuts import render,redirect
from flyapp.models import bikedata,bikecategory,admindb
from frontend.models import Messagesdb,emailsubscription
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User



def index(request):
    return render(request,"indexpg.html")
    

#bike

def addbike(request):
    data=bikecategory.objects.all()
    return render(request,"addbike.html",{'data':data})
def savebike(request):
    if request.method=='POST':
        mod=request.POST.get('bikename')
        com=request.POST.get('company')
        yr=request.POST.get('price')
        pc=request.POST.get('category')
        cr=request.POST.get('description')
        im=request.FILES['image']
        obj=bikedata(Bikename=mod,Company=com,Price=yr,Description=cr,Image=im,PCategory=pc)
        obj.save()
        return redirect(addbike)
        
def showbike(request):
    data=bikedata.objects.all()
    return render(request,"showbike.html",{'data':data})

def editbike(request,dataid):
    data= bikedata.objects.get(id=dataid)
    da=bikecategory.objects.all()
    print (data)
    return render(request,"bikeedit.html",{'data':data,'da':da})

def updatebike(request,dataid):
    if request.method=='POST':
        mod=request.POST.get('bikename')
        com=request.POST.get('company')
        yr=request.POST.get('price')
        cr=request.POST.get('description')
        pc=request.POST.get('category')
        try:
            im=request.FILES['image']
            fs=FileSystemStorage()
            file=fs.save(im.name,im)
        except MultiValueDictKeyError:
            file=bikedata.objects.get(id=dataid).Image
        bikedata.objects.filter(id=dataid).update(Bikename=mod,Company=com,Price=yr,Description=cr,Image=file,PCategory=pc)
        return redirect(showbike)

def deletebike(request,dataid):
    data=bikedata.objects.filter(id=dataid)
    data.delete()
    return redirect(showbike)



#Category

def addcategory(request):
    return render(request,"addcategory.html")
def savecategory(request):
    if request.method=="POST":
        ca=request.POST.get('category')
        de=request.POST.get('catdescription')
        img=request.FILES['catimage']
        obj=bikecategory(Category=ca,CatDescription=de,CatImage=img)
        obj.save()
        return render(request,"addcategory.html")
def showcategory(request):
    data=bikecategory.objects.all()
    return render(request,"showcategory.html",{'data':data})

def editcategory(request,dataid):
    data=bikecategory.objects.get(id=dataid)
    print(data)
    return render(request,"editcategory.html",{'data':data})
def updatecategory(request,dataid):
    if request.method=="POST":
        cat=request.POST.get('category')
        de=request.POST.get('catdescription')
        try:
            im=request.FILES['catimage']
            fs=FileSystemStorage()
            file=fs.save(im.name,im)
        except MultiValueDictKeyError:
            file=bikecategory.objects.get(id=dataid).CatImage
    bikecategory.objects.filter(id=dataid).update(Category=cat,CatDescription=de,CatImage=file)
    return redirect(showcategory)

def deletecategory(request,dataid):
    data=bikecategory.objects.filter(id=dataid)
    data.delete()
    return redirect(showcategory)



#admin

def addadmin(request):
    return render(request,"addadmin.html")
def saveadmin(request):
    if request.method=="POST":
        na=request.POST.get('name')
        em=request.POST.get('email')
        mo=request.POST.get('mobile')
        pa=request.POST.get('password')
        obj=admindb(Name=na,Email=em,Mobile=mo,Password=pa)
        obj.save()
    return redirect(addadmin)
def showadmin(request):
    data=admindb.objects.all()
    return render(request,"showadmin.html",{'data':data})


#message

def showmessage(request):
    data=Messagesdb.objects.all()
    return render(request,"showmessage.html",{'data':data})

def deletemessage(request,dataid):
    data=Messagesdb.objects.filter(id=dataid)
    data.delete()
    return redirect(showmessage)
#Email
def showemail(request):
    data=emailsubscription.objects.all()
    return render(request,"showemail.html",{'data':data})
    


def deleteemail(request,dataid):
    data=emailsubscription.objects.filter(id=dataid)
    data.delete()
    return redirect(showemail)

#login

def adminlogin(request):
    return render(request,"loginpage.html")
def loginauth(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        if User.objects.filter(username__contains=username).exists():
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                request.session['username']=username
                request.session['password']=password
                return redirect(index)
            else:
                return redirect(adminlogin)
        else:
            return redirect(adminlogin)
