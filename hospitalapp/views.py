from django.shortcuts import render,redirect,get_object_or_404
from hospitalapp.models import *

# Create your views here.

def index(request):
    return render(request, 'index.html')

def starter(request):
    return render(request, 'starter-page.html')

def about(request):
    return render(request, 'about.html')

def service(request):
    return render(request, 'service.html')

def department(request):
    return render(request, 'department.html')

def doctors(request):
    return render(request, 'doctors.html')

def appoint(request):
    if request.method == "POST":
        myappointment =Appointment(
            name = request.POST['name'],
            email = request.POST['email'],
            phone = request.POST['phone'],
            date = request.POST['date'],
            department = request.POST['department'],
            doctor = request.POST['doctor'],
            message = request.POST['message'],
        )
        myappointment.save()
        return redirect('/show')

    else:
        return render(request,'appointment.html')

def contact(request):
    if request.method == "POST":
        mycontact = Tel(
            name = request.POST['name'],
            email = request.POST['email'],
            subject = request.POST['subject'],
            message = request.POST['message'],
        )
        mycontact.save()
        return redirect('/contact')

    else:
        return render(request, 'contact.html')

def show(request):
    all = Appointment.objects.all()
    return render(request, 'show.html', {'all': all})

def delete(request,id):
    deletedappointment = Appointment.objects.get(id=id)
    deletedappointment.delete()
    return redirect('/show')

def showcontacts(request):
    allcontacts = Tel.objects.all()
    return render(request, 'showcontacts.html', {'allcontacts': allcontacts})

def remove(request,id):
    deletedcontacts = Tel.objects.get(id=id)
    deletedcontacts.delete()
    return redirect('/showcontacts')

def edit(request,id):
    editinfo = get_object_or_404(Appointment,id=id)
    if request.method == "POST":
            editinfo.name=request.POST.get('name')
            editinfo.email=request.POST.get('email')
            editinfo.phone=request.POST.get('phone')
            editinfo.date=request.POST.get('date')
            editinfo.department=request.POST.get('department')
            editinfo.doctor=request.POST.get('doctor')
            editinfo.message=request.POST.get('message')

            editinfo.save()
            return redirect('/show')

    else:
        return render(request,'edit.html', {'editinfo':editinfo})

def register(request):
    return render(request,'register.html')

def login_view(request):
    return render(request,'login.html')
