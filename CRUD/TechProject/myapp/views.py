from django.shortcuts import render
from .models import *
from random import *

# Create your views here.
def home(request):    
    return render(request,"myapp/login.html")

def home_admin(request):
    if "c_email" in request.session:
        aid=Admin.objects.get(email=request.session['c_email'])
        mid=Meeting.objects.all()
        context={
            'mid':mid,
        }
        return render(request,"myapp/homepageAdmin.html",{'context':context})
    else:
        return render(request,"myapp/login.html")

def home_emp(request):
    if "c_email" in request.session:
        aid=Employee.objects.get(email=request.session['c_email'])
        mid=Meeting.objects.all()
        context={
            'mid':mid,
        }
        return render(request,"myapp/homepageEmployee.html",{'context':context})
    else:
        return render(request,"myapp/login.html")

def login_fun(request):
    try:
        if request.POST:
            s_email=request.POST['email']
            s_password=request.POST['password']
            role=request.POST['role']
            if role=="Admin":
                sid=Admin.objects.get(email=s_email)
                if sid.password==s_password:
                    request.session['c_email']=sid.email
                    # alladmin=Admin.objects.all()
                    # allemployee=Employee.objects.all()
                    mid=Meeting.objects.all()
                    context={
                        'sid':sid,
                        # 'alladmin':alladmin,
                        # 'allemployee':allemployee,
                        'mid':mid,
                    }
                    return render(request,"myapp/homepageAdmin.html",{'context':context})
                else:
                    e_msg="wrong password"
                    return render(request,"myapp/login.html",{'e_msg':e_msg})
            else:
                sid=Employee.objects.get(email=s_email)
                if sid.password==s_password:
                    request.session['c_email']=sid.email
                    allemployee=Employee.objects.all()
                    mid=Meeting.objects.all()
                    context={
                        'sid':sid,
                        'mid':mid,
                    }
                    return render(request,"myapp/homepageEmployee.html",{'context':context})
                else:
                    e_msg="Something Went Wrong..."
                    return render(request,"myapp/login.html",{'e_msg':e_msg})
        else:
            # e_msg="something went wrong..."
            return render(request,"myapp/login.html",{'e_msg':e_msg})
    except:
        e_msg="something went wrong..."
        return render(request,"myapp/login.html",{'e_msg':e_msg})


# Create your views here.
def register_fun(request):
    try:
        if request.POST:
            email=request.POST['email']
            name=request.POST['name']
        
            gender=request.POST['gender']
            phone=request.POST['phone']
            role=request.POST['role']
            address=request.POST['address']
            password=request.POST['password']
            repassword=request.POST['repassword']
            if password==repassword:
                if role=="Admin": 
                    aid=Admin.objects.create(email=email,name=name,password=password,gender=gender,role=role,contactno=phone,address=address)
                    aid.save()
                    context={
                        'aid':aid,
                        }
                    s_msg="Added Successfully"
                    return render(request,"myapp/login.html",{'s_msg':s_msg,'context':context})
                else:
                    eid=Employee.objects.create(email=email,name=name,password=password,gender=gender,role=role,contactno=phone,address=address)
                    eid.save()
                    context={
                        'eid':eid,
                        }
                    s_msg="Added Successfully"
                    return render(request,"myapp/login.html",{'s_msg':s_msg,'context':context})
            else:
                msg="password not match"
                return render(request,"myapp/register.html",{'msg':msg})
        else:
            return render(request,"myapp/register.html")
    except:
        return render(request,"myapp/register.html")

def logout_fun(request):
    if "c_email" in request.session:
        del request.session['c_email']
        return render(request,"myapp/login.html")
    else:
        return render(request,"myapp/login.html")


def create_meeting_fun(request):
    return render(request,"myapp/createmeeting.html")


def meeting_done_fun(request):
    if request.POST:
        companyname=request.POST['companyname']
        companyaddress=request.POST['companyaddress']
        contactno=request.POST['contactno']
        Contactperson=request.POST['Contactperson']
        meetingpurpose=request.POST['meetingpurpose']
        date=request.POST['date']
        comments=request.POST['comments']
        mid = Meeting.objects.create(companyname=companyname,companyaddress=companyaddress,contactno=contactno,Contactperson=Contactperson,meetingpurpose=meetingpurpose,date=date,comments=comments)
        mid=Meeting.objects.all()
        
        alladmin=Admin.objects.all()
        allemployee=Employee.objects.all()
        context={
                    # 'sid':sid,
                    'alladmin':alladmin,
                    'allemployee':allemployee,
                    'mid':mid,
                }
        return render(request,"myapp/homepageAdmin.html",{'context':context})
    else:
        # msg="password not match"
        return render(request,"myapp/createmeeting.html")

def edit_fun(request,pk):
    aid=Admin.objects.get(email=request.session['c_email'])
    mid=Meeting.objects.get(id=pk)
    context={
                'aid':aid,
                'mid':mid,
            }
    return render(request,"myapp/edit-page-admin.html",{'context':context})

def edit_emp_fun(request,pk):
    aid=Employee.objects.get(email=request.session['c_email'])
    mid=Meeting.objects.get(id=pk)
    context={
                'aid':aid,
                'mid':mid,
            }
    return render(request,"myapp/edit-page-emp.html",{'context':context})

def update_emp_fun(request):
    if request.POST:
        companyname=request.POST['companyname']
        mid=Meeting.objects.get(companyname=companyname)
        companyaddress=request.POST['companyaddress']
        contactno=request.POST['contactno']
        Contactperson=request.POST['Contactperson']
        meetingpurpose=request.POST['meetingpurpose']
        date=request.POST['date']
        comments=request.POST['comments']

        mid.companyaddress=companyaddress
        mid.contactno=contactno
        mid.Contactperson=Contactperson
        mid.meetingpurpose=meetingpurpose
        mid.date=date
        mid.comments=comments
        mid.save()
        mid=Meeting.objects.all()
        context={
                # 'aid':aid,
                'mid':mid,
            }
        return render(request,"myapp/homepageEmployee.html",{'context':context})
    else:
        mid=Meeting.objects.all()
        context={
                # 'aid':aid,
                'mid':mid,
            }
        return render(request,"myapp/homepageEmployee.html",{'context':context})


def update_fun(request):
    if request.POST:
        companyname=request.POST['companyname']
        mid=Meeting.objects.get(companyname=companyname)
        companyaddress=request.POST['companyaddress']
        contactno=request.POST['contactno']
        Contactperson=request.POST['Contactperson']
        meetingpurpose=request.POST['meetingpurpose']
        date=request.POST['date']
        comments=request.POST['comments']

        mid.companyaddress=companyaddress
        mid.contactno=contactno
        mid.Contactperson=Contactperson
        mid.meetingpurpose=meetingpurpose
        mid.date=date
        mid.comments=comments
        mid.save()
        mid=Meeting.objects.all()
        context={
                # 'aid':aid,
                'mid':mid,
            }
        return render(request,"myapp/homepageAdmin.html",{'context':context})
    else:
        mid=Meeting.objects.all()
        context={
                # 'aid':aid,
                'mid':mid,
            }
        return render(request,"myapp/homepageAdmin.html",{'context':context})


def delete_fun(request,pk):
    aid=Admin.objects.get(email=request.session['c_email'])
    mid=Meeting.objects.get(id=pk)
    mid.delete()
    mid=Meeting.objects.all()
    context={
                'aid':aid,
                'mid':mid,
            }
    return render(request,"myapp/homepageAdmin.html",{'context':context})

def delete_emp_fun(request,pk):
    aid=Employee.objects.get(email=request.session['c_email'])
    mid=Meeting.objects.get(id=pk)
    mid.delete()
    mid=Meeting.objects.all()
    context={
                'aid':aid,
                'mid':mid,
            }
    return render(request,"myapp/homepageEmployee.html",{'context':context})
