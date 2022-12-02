from django.shortcuts import render,redirect
from django.contrib import messages
from Home.models import usersinfo
# Create your views here.


def index(request):
    return render(request,"index.html")

def login(request):

    if request.method == "POST":
        loginuserid = request.POST.get("loginuserid")
        loginusername = request.POST.get("loginusername")
        loginpassword = request.POST.get("loginpassword")

        if loginuserid == "" and loginusername == "" and loginpassword == "" :
            messages.error(request,"Please fill the details")
            return render(request,'login.html')

       #add query here
        # useri = usersinfo.objects.filter( userid = int(loginuserid), username = loginusername, password = loginpassword).first
        
        try:
            if loginuserid in str(usersinfo.objects.filter(userid = loginuserid).values_list("userid")[0][0]) and loginusername in usersinfo.objects.filter(username = loginusername).values_list("username")[0][0] and loginpassword in usersinfo.objects.filter(password = loginpassword).values_list("password")[0][0]:
                context = {
                    "loginuserid" : loginuserid,
                    "loginusername" : loginusername,

                }
                return render(request,'homepage.html', context)

            else:
                messages.error(request,"Login credentials are incorrect")
                return render(request,"login.html")    

        except:
            messages.error(request,"Login credentials are incorrect")
            return render(request,"login.html")
       
    return render(request,'login.html')


def homepage(request):


    if request.method == "GET":
        render(request,"csvupload.html")

    
    if request.method == "POST": 
        try:       
            csv_file = request.FILES['file']  
            
            if not csv_file.name.endswith('.csv'):
                messages.error(request,"*Please Upload a CSV File")
                # return render(request,'homepage.html')


        except:
            messages.error(request,"*No file choosen")





    return render(request,'homepage.html')


