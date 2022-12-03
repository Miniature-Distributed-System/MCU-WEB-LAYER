from django.shortcuts import render,redirect
from django.contrib import messages
from Home.models import usersinfo, csv
import random
from csv import reader
import io
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
                # context = {
                #     "loginuserid" : loginuserid,
                #     "loginusername" : loginusername,

                # }
                return render(request,'homepage.html')

            else:
                messages.error(request,"Login credentials are incorrect")
                return render(request,"login.html")    

        except:
            messages.error(request,"Login credentials are incorrect")
            return render(request,"login.html")
       
    return render(request,'login.html')

def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')    

        if username == "" and password == "":
            messages.error(request,"Please fill the details")
            return render(request,"signup.html")

        try:
            user1 = usersinfo.objects.filter( username = username ).values_list("username")[0][0]
            if  username in user1:
                messages.error(request,"User already exist")
                return render(request,"signup.html")
        
              

        except:
            # uid = mcu(userid = randint(12405,20000), username = username, password = password)
            id = random.randint(12405,20000)
            usersinfo.objects.create(userid = id, 
                                     username = username, 
                                     password = password
            )
            context = { "userid" : id}
            # db.session.add(uid)
            # db.session.commit()
            return render(request,"ak.html", context)

    return  render(request,"signup.html")    


def homepage(request):

    
    if request.method == "POST": 
        try:       
            csv_file = request.FILES['file']  
            
            if not csv_file.name.endswith('.csv'):
                messages.error(request,"*Please Upload a CSV File")


            else:
                dataset =  csv_file.read().decode('UTF-8')  #reading the cssv file
                istring = io.StringIO(dataset)              #setting a file object
                next(istring)

                for column in reader(istring,delimiter=',',quotechar = '|'): #create the file contents and getting the data as columns
                        csv.objects.update_or_create( 
                            intial_velocity = column[0],
                            final_velocity = column[1],
                            time_taken = column[2]
                        )

                        
                messages.success(request,"File Uploaded.")        #message for csv file upload


         


        except:
            messages.error(request,"*No file choosen")





    return render(request,'homepage.html')


