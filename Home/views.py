from django.shortcuts import render,redirect
from django.contrib import messages
import pandas as pd
from Home.models import usersinfo, filelog
import random
from csv import reader
from csv import writer
import shutil
import codecs
import os
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
                    "loginuserid" : loginuserid
                }
                return render(request,'homepage.html',context)

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
            return render(request,"ak.html", context)

    return  render(request,"signup.html")    


def homepage(request):

    
    if request.method == "POST": 
        try:       
            csv_file = request.FILES['file']  
            userid = request.POST.get('userid')
            
            if not csv_file.name.endswith('.csv'):
                messages.error(request,"*Please Upload a CSV File")

            
                

            else:
                df = pd.read_csv(csv_file)

                headers = df.axes[1]        #reading the headers of the csv and storing into a list

                # messages.success(request,headers.values)
                # dataset =  csv_file.read().decode('UTF-8')  #reading the cssv file
                # istring = io.StringIO(dataset)              #setting a file object
                # next(istring)

                #create the file contents and getting the data as columns
                
                # """ CHECKING OF HEADERS WITH THE ALGORITHM REQUIREMENTS"""
            
                fp = open(os.path.join('D:\Miniature Compute Unit Web Layer\MCU\CSV Samples' , str(csv_file)), 'x')
                fp1 = open(os.path.join('D:\Miniature Compute Unit Web Layer\MCU\CSV Samples\CSV UPLOADS', str(csv_file)),'x')
                fp.close()
                fp1.close()

                # shutil.copy(str(csv_file), os.path.join('D:\Miniature Compute Unit Web Layer\MCU\CSV Samples' , str(csv_file)))
                # file saved

                text = '\\n'
                with csv_file.open('rb') as read_obj, \
                        open(os.path.join('D:\Miniature Compute Unit Web Layer\MCU\CSV Samples\CSV UPLOADS', str(csv_file)), 'w', newline='') as write_obj:
                   
                    csv_reader = reader(codecs.iterdecode(read_obj, 'utf-8'))
                
                    csv_writer = writer(write_obj)
                    
                    #appending
                    for row in csv_reader:
                        row.append(text)
                        csv_writer.writerow(row)        

                filelog.objects.update_or_create(userid = userid, file_name = csv_file, status = "Processing")
                
                os.remove(os.path.join('D:\Miniature Compute Unit Web Layer\MCU\CSV Samples' , str(csv_file)))
                messages.success(request,"File Uploaded.")  #message after csv file upload
                context  = { 'loginuserid' : userid}
                return render(request,'homepage.html',context)
                      
        
        except Exception as e:
            messages.error(request,f"ERROR : {e}")
            context  = { 'loginuserid' : userid}
            return render(request,'homepage.html',context)




    
    return render(request,'homepage.html')

