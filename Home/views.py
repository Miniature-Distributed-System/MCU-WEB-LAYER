from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse
import pandas as pd
from Home.models import usersinfo, filelog
import random
from django.template import loader
from csv import reader
from csv import writer
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
                filelogd = filelog.objects.filter(userid = loginuserid).values()
                context = {
                    "loginuserid" : loginuserid,
                    "filelogd"    : filelogd
                }
                return render(request,'home.html',context)

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
        userid = request.POST.get('userid')
        filelogd = filelog.objects.filter(userid = userid).values()
        algorithm = request.POST.get('algo')
        try:       
            csv_file = request.FILES['file']  
            
            
            if not csv_file.name.endswith('.csv'):
                messages.error(request,"*Please Upload a CSV File")
                context  = { 'loginuserid' : userid,
                              'filelogd' : filelogd}
                return render(request,'home.html',context)
            
            try:
                if str(csv_file) in filelog.objects.filter(file_name = str(csv_file)).values_list('file_name')[0][0]:   #checks if file exist 
                    messages.error(request,"File Already Exist.")
                    context  = { 'loginuserid' : userid,
                                'filelogd' : filelogd}
                    return render(request,'home.html',context)
            except:
                    df =  pd.read_csv(csv_file)
                    headers = df.axes[1]        #reading the headers of the csv and storing into a list
                    print(headers)
                    # """ CHECKING OF HEADERS WITH THE ALGORITHM REQUIREMENTS"""
                    if len(headers) == 5:

                            fp = open(os.path.join('D:\Miniature Compute Unit Web Layer\MCU\CSV Samples' , str(csv_file)), 'x')
                            fp1 = open(os.path.join('D:\Miniature Compute Unit Web Layer\MCU\CSV Samples\CSV UPLOADS', str(csv_file)),'x')
                            fp.close()
                            fp1.close()
                    
                            text = '\\n'
                            with csv_file.open('rb') as read_obj, \
                                    open(os.path.join('D:\Miniature Compute Unit Web Layer\MCU\CSV Samples\CSV UPLOADS', str(csv_file)), 'w', newline='') as write_obj:
                            
                                csv_reader = reader(codecs.iterdecode(read_obj, 'utf-8'))
                            
                                csv_writer = writer(write_obj)
                                
                                #appending
                                for row in csv_reader:
                                    row.append(text)
                                    csv_writer.writerow(row)        

                            x = len(filelog.objects.all().values_list('file_name'))
                            filelog.objects.update_or_create(id = x+1, userid = userid, file_name = csv_file, status = "Processing", algorithm = algorithm)
                            
                            os.remove(os.path.join("D:\Miniature Compute Unit Web Layer\MCU\CSV Samples" , str(csv_file)))
                            messages.success(request,"File Uploaded.")  #message after csv file upload
                            context  = { 'loginuserid' : userid,
                                        'filelogd' : filelogd}
                            return render(request,'home.html',context)

                    else:
                            messages.error(request,"Can't Process The File.")
                            context  = { 'loginuserid' : userid,
                                    'filelogd' : filelogd}
                            return render(request,'home.html',context)

            else:
                    df =  pd.read_csv(csv_file)
                    headers = df.axes[1]        #reading the headers of the csv and storing into a list
                    print(headers)
                    # """ CHECKING OF HEADERS WITH THE ALGORITHM REQUIREMENTS"""
                    if len(headers) == 5:

                            fp = open(os.path.join('D:\Miniature Compute Unit Web Layer\MCU\CSV Samples' , str(csv_file)), 'x')
                            fp1 = open(os.path.join('D:\Miniature Compute Unit Web Layer\MCU\CSV Samples\CSV UPLOADS', str(csv_file)),'x')
                            fp.close()
                            fp1.close()
                    
                            text = '\\n'
                            with csv_file.open('rb') as read_obj, \
                                    open(os.path.join('D:\Miniature Compute Unit Web Layer\MCU\CSV Samples\CSV UPLOADS', str(csv_file)), 'w', newline='') as write_obj:
                            
                                csv_reader = reader(codecs.iterdecode(read_obj, 'utf-8'))
                            
                                csv_writer = writer(write_obj)
                                
                                #appending
                                for row in csv_reader:
                                    row.append(text)
                                    csv_writer.writerow(row)        

                            x = len(filelog.objects.all().values_list('file_name'))
                            filelog.objects.update_or_create(id = x+1, userid = userid, file_name = csv_file, status = "Processing", algorithm = algorithm)
                            
                            os.remove(os.path.join("D:\Miniature Compute Unit Web Layer\MCU\CSV Samples" , str(csv_file)))
                            messages.success(request,"File Uploaded.")  #message after csv file upload
                            context  = { 'loginuserid' : userid,
                                        'filelogd' : filelogd}
                            return render(request,'home.html',context)

                    else:
                            messages.error(request,"Can't Process The File.")
                            context  = { 'loginuserid' : userid,
                                    'filelogd' : filelogd}
                            return render(request,'home.html',context)
                        
        except Exception as e:
            
            messages.error(request,f"ERROR : File Not Uploaded. File May already Exist")
            context  = { 'loginuserid' : userid,
                            'filelogd' : filelogd}
            return render(request,'home.html',context)




    
    return render(request,'home.html')



def delete(request,id,userid):
    filelogd = filelog.objects.filter(userid = userid).values()
    
    try:
        filename = filelog.objects.filter(id = id).values_list('file_name')[0][0]
        filelog.objects.get(id=id).delete()
        os.remove(os.path.join("D:\Miniature Compute Unit Web Layer\MCU\CSV Samples\CSV UPLOADS", filename))
        try:
            os.remove(os.path.join("D:\Miniature Compute Unit Web Layer\MCU\CSV Samples\CSV UPLOADS", filename))
        except:
            None    
        messages.success(request,"File Deleted Successfully")
        context  = { 'loginuserid' : userid,
                                'filelogd' : filelogd}
        return render(request,'home.html',context)

    except:
        messages.success(request,"File deleted already")
        context  = { 'loginuserid' : userid,
                              'filelogd' : filelogd}
        return render(request,'home.html',context)


    