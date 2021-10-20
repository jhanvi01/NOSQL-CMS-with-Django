
from Club.models import Event, JoinedEv
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.utils.timezone import datetime
from datetime import date
from django.core.mail import send_mail  


# Create your views here.

def home(request):

    users= User.objects.all()[1:]
    uid=request.user.id
    je=JoinedEv.objects.filter(s_id=uid).order_by('edate')
    i=[]
    for e in je:
        i.append(str(e.e_id))    
    print(i)
    
    events=Event.objects.order_by('date')
    today=date.today()
    # events=Event.objects.filter(start__gte=date.today()).order_by('date')
    nevents= []
    for e in events:
        if str(e.id) not in i:
            nevents.append(e)
    
    print(nevents)
    

    # nevents=nevents.sort(key='date')
    # je=list(je).sort(key=edate)


    return render(request,'home.html',{'users':users,'events':nevents, 'je':je})


def login(request):
    if request.method=='POST':
        username=request.POST['user']
        password=request.POST['pass']

        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.info(request,"Please enter valid credentials")
            return render(request,'home.html')



def register(request):
    if request.method=="POST":
        username= request.POST['user']
        password= request.POST['pass']
        rpass= request.POST['rpass']
        email= request.POST['email']

        if password==rpass:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Taken")
                return render(request,'home.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email Taken")
                return render(request,'home.html')
            else:
                user= User.objects.create_user(username=username,password=password,email=email)
                user.save()
                messages.info(request,"User created")
                return render(request,'home.html')
        else:
            messages.info('Password not matched')
            return render(request,'home.html')
    else:
        return render(request,'home.html')

def logout(request):
    auth.logout(request)
    return redirect('home') 


def deluser(request):
    id=request.GET.get('id')
    user=User.objects.get(id=id)
    user.delete()
    return redirect('home')


def addev(request):
    if request.method=="POST":
        name=request.POST['name']
        desc=request.POST['desc']
        edate=request.POST['edate']
        e= Event.objects.create(name=name,desc=desc,date=edate)
        e.save()
        emails=[]
        for user in User.objects.all():
            emails.append(user.email)
        print(emails[1:])
        send_mail(
            'New Event from CMS', 
            'Hello, Thank You for Joining our Website!\n We have a new event for you named :'+name+'\n, Do check it out!', 
            'host username', 
            emails[1:],
            fail_silently=False
           
        ) 


        return redirect('home')
        


    return render(request,'eventadd.html')



def delev(request):
    id=request.GET.get('id')
    Event.objects.filter(id=id).delete()
    return redirect('home')



def updatev(request):
    if request.method=="POST":
        id=request.GET.get('id')
        name=request.POST["name"]
        desc=request.POST["desc"]
        date=request.POST["edate"]
        Event.objects.filter(id=id).update(name=name,desc=desc,date=date)
        return redirect('home') 


    id=request.GET.get('id')
    e=Event.objects.filter(id=id)
    
    return render(request,'updatev.html',{'event':e[0]})


def joinev(request):
    sid=request.GET.get('sid')
    eid=request.GET.get('eid')
    e=Event.objects.filter(id=eid)
    name=e[0].name
    date=e[0].date
    je=JoinedEv.objects.create(s_id=sid,e_id=eid,ename= name,edate=date)
    je.save()
    return redirect('home')


def leavev(request):
    id=request.GET.get('id')
    JoinedEv.objects.filter(id=id).delete()
    return redirect('home')


def contact(request):
    name=request.POST['Name']
    subject=request.POST['Subject']
    message=request.POST['Message']

    send_mail(
        'CMS Contact-Form: '+subject,
        'From : '+ name+"\n"+ message,
        'host username',
        ['host username'],
        fail_silently=False
    )

    return redirect('home')