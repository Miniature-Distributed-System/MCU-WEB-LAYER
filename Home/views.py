from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse
import pandas as pd
from Home.models import usersinfo, filelog, diagnosis_instance,disease_instance,devlog,active_instance
import random
from csv import reader
from csv import writer
import codecs
import os
import csv

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
        instance_type = request.POST.get('algo')
           
        csv_file = request.FILES['file']  
            
            
        if not csv_file.name.endswith('.csv'):
                messages.error(request,"*Please Upload a CSV File")
                context  = { 'loginuserid' : userid,
                              'filelogd' : filelogd}
                return render(request,'home.html',context)

        try:    
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
                        print(len(headers))
                        # """ CHECKING OF HEADERS WITH THE ALGORITHM REQUIREMENTS"""
                        if instance_type == "Diagnosis":
                            diagonsis_headers = ['diagnosis_id','fever','medicine']
                            if len(headers) == 3 and diagonsis_headers == list(headers):
                                
                                    with csv_file.open('rb') as read_obj, \
                                        open(os.path.join('D:\Miniature Compute Unit Web Layer\MCU\CSV UPLOADS', str(csv_file)), 'w', newline='') as write_obj:
                                    
                                        csv_reader = reader(codecs.iterdecode(read_obj, 'utf-8'))
                                    
                                        csv_writer = writer(write_obj)
                                        
                                        for row in csv_reader:
                                            csv_writer.writerow(row)  

                                    x = len(filelog.objects.all().values_list('file_name'))
                                    filelog.objects.update_or_create(id = x+1, userid = userid, file_name = csv_file, status = "Processing", instance_type = instance_type)

                                    with open(str(csv_file)) as csvfile1:
                                        csvfile = csv.reader(csvfile1,delimiter=",")
                                        for row in csvfile:
                                            diagnosis_instance.objects.update_or_create(
                                            diagnosis_id = row[0],
                                            fever = row[1],
                                            medicine = row[2],
                                            filename = str(csv_file)
                            
                                        )

                                    diagnosis_instance.objects.filter(filename = str(csv_file)).first().delete()
                                    messages.success(request,f"File Uploaded. {str(csv_file)}") #message after csv file upload
                                    context  = { 'loginuserid' : userid,
                                                'filelogd' : filelogd}
                                    return render(request,'home.html',context)


                        elif instance_type == "Disease":
                            disease_header = ['disease_id','fever','medicine']
                            if len(headers) == 3 and disease_header == list(headers):
                                    with csv_file.open('rb') as read_obj, \
                                        open(os.path.join('D:\Miniature Compute Unit Web Layer\MCU\CSV UPLOADS', str(csv_file)), 'w', newline='') as write_obj:
                                    
                                        csv_reader = reader(codecs.iterdecode(read_obj, 'utf-8'))
                                    
                                        csv_writer = writer(write_obj)
                                        
                                        for row in csv_reader:
                                            csv_writer.writerow(row)  

                                    x = len(filelog.objects.all().values_list('file_name'))
                                    filelog.objects.update_or_create(id = x+1, userid = userid, file_name = csv_file, status = "Processing", instance_type = instance_type)

                                    with open(str(csv_file)) as csvfile1:
                                        csvfile = csv.reader(csvfile1,delimiter=",")
                                        for row in csvfile:
                                            disease_instance.objects.update_or_create(
                                            disease_id = row[0],
                                            fever = row[1],
                                            medicine = row[2],
                                            filename = str(csv_file)
                            
                                        )

                                    disease_instance.objects.filter(filename = str(csv_file)).first().delete()
                                    messages.success(request,f"File Uploaded. {str(csv_file)}") #message after csv file upload
                                    context  = { 'loginuserid' : userid,
                                                'filelogd' : filelogd}
                                    return render(request,'home.html',context)

                        else:
                                messages.error(request,"Can't Process The File. Attribute might be missing.")
                                context  = { 'loginuserid' : userid,
                                        'filelogd' : filelogd}
                                return render(request,'home.html',context)

            else:
                        df =  pd.read_csv(csv_file)
                        headers = df.axes[1]        #reading the headers of the csv and storing into a list
                        print(headers)
                        print(len(headers))
                        # """ CHECKING OF HEADERS WITH THE ALGORITHM REQUIREMENTS"""
                        if instance_type == "Diagnosis":
                            diagonsis_headers = ['diagnosis_id','fever','medicine']
                            if len(headers) == 3 and diagonsis_headers == list(headers):
                                
                                    with csv_file.open('rb') as read_obj, \
                                        open(os.path.join('D:\Miniature Compute Unit Web Layer\MCU\CSV UPLOADS', str(csv_file)), 'w', newline='') as write_obj:
                                    
                                        csv_reader = reader(codecs.iterdecode(read_obj, 'utf-8'))
                                    
                                        csv_writer = writer(write_obj)
                                        
                                        for row in csv_reader:
                                            csv_writer.writerow(row)  

                                    x = len(filelog.objects.all().values_list('file_name'))
                                    filelog.objects.update_or_create(id = x+1, userid = userid, file_name = csv_file, status = "Processing", instance_type = instance_type)

                                    with open(str(csv_file)) as csvfile1:
                                        csvfile = csv.reader(csvfile1,delimiter=",")
                                        for row in csvfile:
                                            diagnosis_instance.objects.update_or_create(
                                            diagnosis_id = row[0],
                                            fever = row[1],
                                            medicine = row[2],
                                            filename = str(csv_file)
                            
                                        )

                                    diagnosis_instance.objects.filter(filename = str(csv_file)).first().delete()
                                    messages.success(request,f"File Uploaded. {str(csv_file)}") #message after csv file upload
                                    context  = { 'loginuserid' : userid,
                                                'filelogd' : filelogd}
                                    return render(request,'home.html',context)

                        elif instance_type == "Disease":
                            disease_header = ['disease_id','fever','medicine']
                            if len(headers) == 3 and disease_header == list(headers):
                                    with csv_file.open('rb') as read_obj, \
                                        open(os.path.join('D:\Miniature Compute Unit Web Layer\MCU\CSV UPLOADS', str(csv_file)), 'w', newline='') as write_obj:
                                    
                                        csv_reader = reader(codecs.iterdecode(read_obj, 'utf-8'))
                                    
                                        csv_writer = writer(write_obj)
                                        
                                        for row in csv_reader:
                                            csv_writer.writerow(row)  

                                    x = len(filelog.objects.all().values_list('file_name'))
                                    filelog.objects.update_or_create(id = x+1, userid = userid, file_name = csv_file, status = "Processing", instance_type = instance_type)

                                    with open(str(csv_file)) as csvfile1:
                                        csvfile = csv.reader(csvfile1,delimiter=",")
                                        for row in csvfile:
                                            disease_instance.objects.update_or_create(
                                            disease_id = row[0],
                                            fever = row[1],
                                            medicine = row[2],
                                            filename = str(csv_file)
                            
                                        )

                                    disease_instance.objects.filter(filename = str(csv_file)).first().delete()
                                    messages.success(request,f"File Uploaded. {str(csv_file)}") #message after csv file upload
                                    context  = { 'loginuserid' : userid,
                                                'filelogd' : filelogd}
                                    return render(request,'home.html',context)

                        else:
                                messages.error(request,"Can't Process The File. Attribute might be missing.")
                                context  = { 'loginuserid' : userid,
                                        'filelogd' : filelogd}
                                return render(request,'home.html',context)
                        
        except Exception as e:
            
            messages.error(request,f"ERROR : File Not Uploaded.")
            context  = { 'loginuserid' : userid,
                            'filelogd' : filelogd}
            return render(request,'home.html',context)




    
    return render(request,'home.html')



def delete(request,id,userid,file_name,instance_type):
    filelogd = filelog.objects.filter(userid = userid).values()
    if instance_type == "Diagnosis":
        diagnosis_instance.objects.filter(filename = file_name).delete()
    elif instance_type == "Disease":
        disease_instance.objects.filter(filename = file_name).delete()
    try:
        filename = filelog.objects.filter(id = id).values_list('file_name')[0][0]
        filelog.objects.get(id=id).delete()
        os.remove(os.path.join("D:\Miniature Compute Unit Web Layer\MCU\CSV UPLOADS", filename))
        try:
            os.remove(os.path.join("D:\Miniature Compute Unit Web Layer\MCU\CSV UPLOADS", filename))
        except:
            None      
        messages.success(request,f"File Deleted Successfully. {file_name}")
        context  = { 'loginuserid' : userid,
                                'filelogd' : filelogd}
        return render(request,'home.html',context)

    except:
        messages.success(request,"File deleted already")
        context  = { 'loginuserid' : userid,
                              'filelogd' : filelogd}
        return render(request,'home.html',context)

def result(request,loginuserid,file_name,instance_type):
    
    if instance_type == "Diagnosis":
        data  = diagnosis_instance.objects.filter(filename = file_name).all()
    if instance_type == "Disease":
        data  = disease_instance.objects.filter(filename = file_name).all()
    context = {
        "loginuserid" : loginuserid,
        "data" : data
        }

    if instance_type == "Diagnosis":
        return render(request,"results.html",context)

    if instance_type == "Disease":
        return render(request,"results1.html",context)    


def devlogin(request):
    if request.method == "POST":
        devid = request.POST.get('devid')
        devpassword = request.POST.get('devpassword')       

        if devid == "" and devpassword == "" :
            messages.error(request,"Please fill the details")
            return render(request,'login.html')
        
        try:
            if devid in str(devlog.objects.filter(devid = devid).values_list("devid")[0][0]) and devpassword in devlog.objects.filter(password = devpassword).values_list("password")[0][0]:
                context = {
                    "devid" : devid
                }
                return render(request,'devhome.html',context)

            else:
                messages.error(request,"Login credentials are incorrect")
                return render(request,"devlogin.html")    

        except:
            messages.error(request,"Login credentials are incorrect")
            return render(request,"devlogin.html")
       
    return render(request,'devlogin.html')

def clientlog(request,devid):

    data  = usersinfo.objects.all()
    context = {
        "devid" : devid,
        "data" : data
        }


    return render(request,"clientlog.html",context)


def viewactiveinstance(request,devid):
     
    data = active_instance.objects.all();

    context = {
         "devid" : devid,
         "data" : data
    }

    return render(request,"activeinstance.html",context)