from django.shortcuts import render,redirect
from django.contrib import messages
# Create your views here.


def index(request):
    return render(request,"index.html")

def login(request):

    if request.method == "POST":
        loginuserid = request.form['loginuserid']
        loginusername = request.form['loginusername']
        loginpassword = request.form['loginpassword']

        if loginuserid == "" and loginusername == "" and loginpassword == "" :
            messages.error(request,"Please fill the details")
            return render('login.html')

       #add query here
        useri = mcu.query.filter_by( userid = int(loginuserid), username = loginusername, password = loginpassword).first()
        
        
        if useri :
            context = {
                "loginuserid" : loginuserid,
                "loginusername" : loginusername,

            }
            return render( request,'homepage.html', context)

        else:
            messages.error(request,"Login credentials are incorrect")
            return redirect("/login")    
       
    return render('login.html')




def homepage(request):
    return render(request,'homepage.html')


