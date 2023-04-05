from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse
import pandas as pd
from Home.models import usersinfo, filelog,devlog,instances
from datetime import datetime  
import random
from csv import reader
from csv import writer
import codecs
import os
import MCU.settings as settings

def index(request):
    return render(request,"index.html")

def login(request):

    if request.method == "POST":
        loginuserid = request.POST.get("loginuserid")
        loginpassword = request.POST.get("loginpassword")
        if loginuserid == "" and  loginpassword == "" :
            messages.error(request,"Please fill the details")
            return render(request,'login.html')
        
        try:
            if loginuserid in str(usersinfo.objects.filter(userid = loginuserid).values_list("userid")[0][0]) and loginpassword in usersinfo.objects.filter(password = loginpassword).values_list("password")[0][0]:
                filelogd = filelog.objects.filter(userid = loginuserid).values()
                instance_list = instances.objects.all()

                context = {
                    "loginuserid" : loginuserid,
                    "filelogd"    : filelogd,
                    "instance_list" : instance_list
                }
                return render(request,'home.html',context)

            else:
                messages.error(request,"Login credentials are incorrect")
                return render(request,"login.html")    

        except Exception as e:
            print(str(e))
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
        aliasname = request.POST.get('aliasname')
        csv_file = request.FILES['file']  
        instance_list = instances.objects.all()
       
            
        if not csv_file.name.endswith('.csv'):
                messages.error(request,"*Please Upload a CSV File")
                context  = { 'loginuserid' : userid,
                              'filelogd' : filelogd,
                              'instance_list' : instance_list
                              }
                return render(request,'home.html',context)

        try:    
            try:
                    if str(csv_file) in filelog.objects.filter(file_name = str(csv_file)).values_list('file_name')[0][0]:   #checks if file exist 
                        messages.error(request,"File Already Exist.")
                        context  = { 'loginuserid' : userid,
                                    'filelogd' : filelogd,
                                    'instance_list' : instance_list}
                        return render(request,'home.html',context)
            
            except:
                        df =  pd.read_csv(csv_file)
                        
                        with csv_file.open('rb') as read_obj, \
                                        open(os.path.join('D:\Miniature Compute Unit Web Layer\MCU\CSV UPLOADS', str(csv_file)), 'w', newline='') as write_obj:
                                    
                                        csv_reader = reader(codecs.iterdecode(read_obj, 'utf-8'))
                                    
                                        csv_writer = writer(write_obj)
                                        
                                        for row in csv_reader:
                                            csv_writer.writerow(row)  

                        x = len(filelog.objects.all().values_list('file_name'))
                        filelog.objects.update_or_create(id = x+1, userid = userid, file_name = csv_file, status = "Pending", instance_type = instance_type, aliasname = aliasname, file_size = os.path.getsize(os.path.join(os.path.join('D:\Miniature Compute Unit Web Layer\MCU\CSV UPLOADS', str(csv_file)))), upload_time = datetime.now)
                        
                        # with open(str(csv_file)) as csvfile1:
                        #     csvfile = csv.reader(csvfile1,delimiter=",")
                        #     for row in csvfile:
                        #         diagnosis_instance.objects.update_or_create(
                        #         diagnosis_id = row[0],
                        #         fever = row[1],
                        #         medicine = row[2],
                        #         filename = str(csv_file)
                            
                        #     )

                        # diagnosis_instance.objects.filter(filename = str(csv_file)).first().delete()
                        
                        messages.success(request,f"File Uploaded.") #message after csv file upload
                        context  = { 'loginuserid' : userid,
                                                'filelogd' : filelogd,
                                                'instance_list' : instance_list}
                        return render(request,'home.html',context)


                    

           
        except Exception:
            
            messages.error(request,f"ERROR : File Not Uploaded.")
            context  = { 'loginuserid' : userid,
                            'filelogd' : filelogd,
                            'instance_list' : instance_list}
            return render(request,'home.html',context)




    return render(request,'home.html',context)



def delete(request,id,userid,file_name,instance_type):
    filelogd = filelog.objects.filter(userid = userid).values()
    instance_list = instances.objects.all()
    try:
        filename = filelog.objects.filter(id = id).values_list('file_name')[0][0]
        filelog.objects.get(id=id).delete()
        os.remove(os.path.join("D:\Miniature Compute Unit Web Layer\MCU\CSV UPLOADS", filename))
        try:
            os.remove(os.path.join("D:\Miniature Compute Unit Web Layer\MCU\CSV UPLOADS", filename))
        except:
            None      
        messages.success(request,f"File Deleted Successfully.")
        context  = { 'loginuserid' : userid,
                                'filelogd' : filelogd,
                                'instance_list' : instance_list}
        return render(request,'home.html',context)

    except:
        messages.success(request,"File deleted already")
        context  = { 'loginuserid' : userid,
                              'filelogd' : filelogd,
                              'instance_list' : instance_list}
        return render(request,'home.html',context)

def result(request,loginuserid,file_name,instance_type):
    
    # if instance_type == "Diagnosis":
    #     data  = diagnosis_instance.objects.filter(filename = file_name).all()
    # if instance_type == "Disease":
    #     data  = disease_instance.objects.filter(filename = file_name).all()
    # context = {
    #     "loginuserid" : loginuserid,
    #     "data" : data
    #     }

    # if instance_type == "Diagnosis":
    #     return render(request,"results.html",context)

    # if instance_type == "Disease":
    #     return render(request,"results1.html",context)    
    pass


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

def devhome(request):
     
    return render(request,"devhome.html")

def clientlog(request,devid):

    data  = usersinfo.objects.all()
    context = {
        "devid" : devid,
        "data" : data
        }


    return render(request,"clientlog.html",context)


def viewactiveinstance(request,devid):
     
    data = instances.objects.all()

    context = {
         "devid" : devid,
         "data" : data
    }

    return render(request,"activeinstance.html",context)

def deleteInstance(request,instance_name,devid):
     
    instances.objects.filter(instance_name = instance_name).delete()
    try:
        os.remove(os.path.join("D:\Miniature Compute Unit Web Layer\MCU\CSV UPLOADS", instance_name + '.csv'))
    except:
            None
    data = instances.objects.all()
    context = {
         "devid" : devid,
         "data" : data
    }
    return render(request,"activeinstance.html",context)


def addInstance(request):
     
    if request.method == "POST":
        instancename = request.POST.get('instancename')
        algorithm = request.POST.get('algo')

        column_count = int(request.POST.get('column_counter'))
        columns = [request.POST.get('survey_options_' + str(idx)) for idx in  range(1, column_count + 1)]
        columns_values = [request.POST.get('survey_values_' + str(idx)) for idx in  range(1, column_count + 1)]
        print(columns)
        print(columns_values)

        with open( os.path.join('D:\Miniature Compute Unit Web Layer\MCU\CSV UPLOADS' , str(instancename) + '.csv') , 'w') as file:
            csv_writer = writer(file)                          
            csv_writer.writerow(columns)
            csv_writer.writerow(columns_values) 

        timestamp = str(datetime.now())
        csvfile = "NA"
        x = len(instances.objects.all().values_list('instance_name'))
        instances.objects.update_or_create(id = x + 1 ,instance_name = instancename, algorithm = algorithm, timestamp = timestamp, csvfile = csvfile)
        


    return render(request,"addinstance.html")


def viewmore(request,loginuserid,file_name,instance_type):
    
    filedetails = filelog.objects.filter(file_name = file_name)
    context = {
        "loginuserid" : loginuserid,
        "filedetails" : filedetails,
        "file_dir" : settings.CSV_UPLOAD_URL
    }
    return render(request,"viewmore.html",context)