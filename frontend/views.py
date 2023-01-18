from django.shortcuts import render,redirect
from flyapp.models import bikedata,bikecategory
from frontend.models import Messagesdb,emailsubscription,Registersave



def findex(request):
    data=bikedata.objects.all()
    da=bikecategory.objects.all()
    return render(request,"findex.html",{'data':data,'da':da})

def contactpg(request):
    data=bikedata.objects.all()
    da=bikecategory.objects.all()
    return render(request,"contactpage.html",{'data':data,'da':da})


def category(request,itemcat):    #itemcat which is defined in html page
    da=bikecategory.objects.all()
    cat=itemcat.upper()
    data=bikedata.objects.filter(PCategory=itemcat)   #take product cat only
    coun=bikecategory.objects.all()
    context={
        'cat':cat,
        'data':data,
        'coun':coun,
        'da':da
    }
    return render(request,"categorypage.html",context)

def singleproduct(request,dataid):
    data=bikedata.objects.get(id=dataid)
    da=bikecategory.objects.all()
    return render(request,"singleproductpg.html",{'data':data,'da':da})



def messagepage(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        textarea=request.POST.get('textarea')
        obj=Messagesdb(Name=name,Email=email,Subject=subject,Textarea=textarea)
        obj.save()
        return redirect(contactpg)

def emailsub(request):
    if request.method=="POST":
        emailsub=request.POST.get('emailsub')
        obj=emailsubscription(Emailsub=emailsub)
        obj.save()
    return render(request,"findex.html")

def bikenews(request):
    return render(request,"bikenews.html")

def frontendloginpage(request):
    return render(request,"frontendloginpage.html")

def registersave(request):
    if request.method=="POST":
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        password1=request.POST.get('password1')
        if password==password1:
            obj=Registersave(Username=username,Email=email,Password=password,Password1=password1)
            obj.save()
            return render(request,"frontendloginpage.html")


def userloginsave(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")

        if Registersave.objects.filter(Username=username,Password=password).exists():
            request.session['username']=username
            request.session['password']=password
            return redirect(findex)

        else:
            return render(request,"frontendloginpage.html",{'msg':"Sorry,Password Does not Match.Please Login Again"})
    else:
        return redirect(findex)

def logout(request):
    del request.session['username']
    # del request.session['password']

    return redirect(findex)







