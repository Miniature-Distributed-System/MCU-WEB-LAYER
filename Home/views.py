from django.shortcuts import render
# from django.http import HttpResponseRedirect
from django.contrib import messages
# from django.urls import reverse
import pandas as pd
from Home.models import usersinfo, filelog,devlog,instances
from datetime import datetime  
import random
from csv import reader
from csv import writer
import codecs
import os


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
        aliasname_raw = request.POST.get('aliasname')
        aliasname = aliasname_raw.replace(" ","")
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
                    if str(csv_file) in filelog.objects.filter(file_name = str(csv_file)).values_list('file_name')[0][0]:   #checks if file exist 
                        messages.error(request,"File Already Exist.")
                        context  = { 'loginuserid' : userid,
                                    'filelogd' : filelogd,
                                    'instance_list' : instance_list}
                        return render(request,'home.html',context)
            
        except:
                        
                        
                        with csv_file.open('rb') as read_obj, \
                                        open(os.path.join('/home/vishnu/Project_full/temp/user_data/', str(csv_file)), 'w', newline='') as write_obj:
                                    
                                        csv_reader = reader(codecs.iterdecode(read_obj, 'utf-8'))
                                    
                                        csv_writer = writer(write_obj)
                                        
                                        for row in csv_reader:
                                            csv_writer.writerow(row)  

                    
                        # x = len(filelog.objects.all().values_list('file_name'))
                        filelog.objects.update_or_create(userid = userid, file_name = csv_file, status = "Pending", instance_type = instance_type, aliasname = aliasname, file_size = os.path.getsize(os.path.join(os.path.join('/home/vishnu/Project_full/temp/user_data/', str(csv_file)))) / (1024 * 1024), timestamp = datetime.now, priority = 1, final_result = "Not Updated")
                        

                        messages.success(request,f"File Uploaded.") #message after csv file upload
                        context  = { 'loginuserid' : userid,
                                                'filelogd' : filelogd,
                                                'instance_list' : instance_list}
                        return render(request,'home.html',context)


                    

        
            
        messages.error(request,f"ERROR : File Not Uploaded.")
        context  = { 'loginuserid' : userid,
                            'filelogd' : filelogd,
                            'instance_list' : instance_list}
        
        return render(request,'home.html',context)




    return render(request,'home.html',context)



def delete(request,userid,file_name,instance_type):
    filelogd = filelog.objects.filter(userid = userid).values()
    instance_list = instances.objects.all()
    try:
        filename = filelog.objects.filter(file_name = file_name).values_list('file_name')[0][0]
        filelog.objects.get(file_name = file_name).delete()
        os.remove(os.path.join("/home/vishnu/Project_full/temp/user_data/", filename))
        try:
            os.remove(os.path.join("/home/vishnu/Project_full/temp/user_data/", filename))
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



def devlogin(request):
    if request.method == "POST":
        devid = request.POST.get('devid')
        devpassword = request.POST.get('devpassword')       

        if devid == "" and devpassword == "" :
            messages.error(request,"Please fill the details")
            return render(request,'devlogin.html')
        
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
        os.remove(os.path.join("/home/vishnu/Project_full/temp/instance/", instance_name + '.csv'))
    except:
            None
    data = instances.objects.all()
    context = {
         "devid" : devid,
         "data" : data
    }
    return render(request,"activeinstance.html",context)


def addInstance(request,devid):
     
    try:  
        if request.method == "POST":
            instancename = request.POST.get('instancename')
            algorithm = request.POST.get('algo')

            column_count = int(request.POST.get('column_counter'))
            columns = [request.POST.get('survey_options_' + str(idx)) for idx in  range(1, column_count + 1)]
            columns_values = [request.POST.get('survey_values_' + str(idx)) for idx in  range(1, column_count + 1)]
            print(columns)
            print(columns_values)
        
            columnNames=[]
            columnValuesDict={}
            columns_list = columns
            values = columns_values
            columnNames = columns_list
            verticalMatrixLength = 0

            def instanceRowConstructor(depth):
                row = []
                for i in columnValuesDict.keys():
                    row.append(columnValuesDict.get(i)[depth])
                return row	

            for i in range(len(columnNames)):
                    
                    columnValuesDict[columnNames[i]] = values[i].split() if values[i] is not None else []
                    if(len(columnValuesDict[columnNames[i]]) > verticalMatrixLength):
                        verticalMatrixLength = len(columnValuesDict[columnNames[i]])

            with open("/home/vishnu/Project_full/temp/instance/" + str(instancename) + '.csv' , 'w', newline = '') as f:
                mywriter = writer(f, dialect='excel')
                mywriter.writerows([columnNames])
                for depth in range(verticalMatrixLength):
                    mywriter.writerows([instanceRowConstructor(depth)])	

            timestamp = str(datetime.now())
            csvfile = str(instancename) + '.csv'
            print(type(instancename))
            # x = len(instances.objects.all().values_list('instance_name'))
            instances.objects.update_or_create(instance_name = str(instancename), algorithm = 1, timestamp = timestamp, csvfile = csvfile)
            
            return render(request,"addinstance.html")
        
    except Exception as e:
        print("Error " + str(e))
        messages.error(request,"Error")
        return render(request,"addinstance.html")

    context = { "devid" : devid}
    return render(request,"addinstance.html",context)


def viewmore(request,loginuserid,file_name,instance_type):
    
    filedetails = filelog.objects.filter(file_name = file_name)
    final_result = filelog.objects.filter(file_name = file_name).values_list("final_result")[0][0]
    status = filelog.objects.filter(file_name = file_name).values_list("status")[0][0]
    list = []
    with open( os.path.join('/home/vishnu/Project_full/temp/instance/' , str(instance_type) + '.csv') , mode ='r') as file:
        csv_reader = reader(file)
        for row in csv_reader:
            list.append(row)
           
        
    print(list)
    print(instance_type)     
    print(os.path.join('/home/vishnu/Project_full/temp/instance/' , str(instance_type) + '.csv'))


    values_list = []
    j = 0
    while(j!=len(list[1])):
        for i in range(1,len(list)):
            values_list.append(list[i][j])
        j = j + 1
        values_list.append(" | ")        

    print(values_list.pop(len(values_list)-1))  

    context = {
        "loginuserid" : loginuserid,
        "filedetails" : filedetails,
        "file_dir" : 'D:\Miniature Compute Unit Web Layer\MCU\INSTANCE CSV UPLOADS',
        "header" :  list[0],
        "values" :  values_list,
        "final_result" : final_result
    }

    return render(request,"viewmore.html",context)

def resultspart(request,loginuserid,file_name,instance_type):
     
    filedetails = filelog.objects.filter(file_name = file_name)
    final_result = filelog.objects.filter(file_name = file_name).values_list("final_result")[0][0]
    list = []
    with open( os.path.join('/home/vishnu/Project_full/temp/instance/' , str(instance_type) + '.csv') , mode ='r') as file:
        csv_reader = reader(file)
        for row in csv_reader:
            list.append(row)
           
        
    print(list)
    print(instance_type)     
    print(os.path.join('/home/vishnu/Project_full/temp/instance/' , str(instance_type) + '.csv'))

    # with open(os.path.join('/home/vishnu/Project_full/temp/user_data/' , str(file_name) + '.csv') , mode ='r') as file:
    def parse_file(input_file,result_file,target_column_name,final_result_specific_list):

        p = 0 
        total = 0 
        with open(input_file, 'r') as file:
                                    
            with open(result_file, 'w', newline = '') as f:
                                            
                hypothesis = final_result_specific_list
                                            
                csvreader = reader(file)
                header = next(csvreader)
                mywriter = writer(f, dialect='excel')
                header.append(target_column_name)
                mywriter.writerows([header])
                #print(type(header))
                val={}
                for row in csvreader:
                    flag=1
                    result=1
                    total = total + 1        
                    for i in range(len(hypothesis)):
                        # print(row[i]+"-"+hypothesis[i]+" ",'')
                        if(hypothesis[i]!="?"):
                            if(row[i]!=hypothesis[i]):
                                flag=0
                                break
                                                        
                    if(flag==0):
                        result=0
                                                
                    if(result==1):
                        row.append("Positive")
                        p = p + 1
                    else:
                        row.append("Negative")
                                                
                                            
                    mywriter.writerows([row])

        return p,total


    input_file = '/home/vishnu/Project_full/temp/user_data/' + str(file_name)
    output_file = '/home/vishnu/Downloads/' + str(file_name) + '.csv'
    target_column_name = "Result"
    print(final_result)
    final_result_s = final_result.split(":")
    print(final_result_s)
    final_result_specific_list = final_result_s[1].split(",")
    print(final_result_specific_list)
    p,total = parse_file(input_file,output_file,target_column_name,final_result_specific_list)
    print(p)
    print(total-p)
    values_list = []
    j = 0
    while(j!=len(list[1])):
        for i in range(1,len(list)):
            values_list.append(list[i][j])
        j = j + 1
        values_list.append(" | ")        

    print(values_list.pop(len(values_list)-1)) 
    general_hypo = final_result_s[0]
    specific_hypo = final_result_s[1]
    context = {
        "loginuserid" : loginuserid,
        "filedetails" : filedetails,
        "file_dir" : 'D:\Miniature Compute Unit Web Layer\MCU\INSTANCE CSV UPLOADS',
        "header" :  list[0],
        "values" :  values_list,
        "final_result" : final_result,
        "general_hypo" : general_hypo,
        "specific_hypo" : specific_hypo,
        "p" : p,
        "n" : total - p
    }




    return render(request,"viewmorepie.html",context)
