from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError

from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login


from django.shortcuts import render, redirect
from AdminApp.models import *


# Create your views here.
def baseFarmer(request):
    return render(request, 'base.html')


def indexFarmer(request):
    return render(request, 'index.html')


def viewFarmer(request):
    data = Farmers_Db.objects.all()
    return render(request, 'view_farmer.html',
                  {'data': data})


def save_Farmer_data(request):
    if request.method == "POST":
        farmer_name = request.POST.get('name')
        farmer_email = request.POST.get('email')
        farmer_phone = request.POST.get('phone_number')
        farmer_password = request.POST.get('password')
        obj = Farmers_Db(f_name=farmer_name,
                         f_email=farmer_email,
                         f_number=farmer_phone,
                         f_password=farmer_password)
        obj.save()
        return redirect(AddFarmer)


def Edite_farmers(request, farmer_id):
    data = Farmers_Db.objects.get(id=farmer_id)
    return render(request, 'Edite_farmers.html',
                  {'data': data})


def update_farmer(request, f_id):
    if request.method == "POST":
        farmer_name = request.POST.get('name')
        farmer_email = request.POST.get('email')
        farmer_phone = request.POST.get('phone_number')
        farmer_password = request.POST.get('password')
        Farmers_Db.objects.filter(id=f_id).update(f_name=farmer_name,
                                                  f_email=farmer_email,
                                                  f_number=farmer_phone,
                                                  f_password=farmer_password)
        return redirect(viewFarmer)
def Add_Seeds(request):
    return render(request,'Add_Seeds.html')
def Save_SeedsData(request):
    if request.method=="POST":
        S_name=request.POST.get('seed_name')
        S_type=request.POST.get('seed_type')
        S_quantity=request.POST.get('quantity')
        S_price=request.POST.get('price')
        S_description=request.POST.get('description')
        S_image = request.FILES['seed_image']
        obj=Seeds_Db(seeds_name=S_name,
                     seeds_type=S_type,
                     seeds_quantity=S_quantity,
                     seeds_price=S_price,
                     seeds_description=S_description,
                     seeds_image=S_image)
        obj.save()
        return redirect(Add_Seeds)
def View_Seeds(request):
    data=Seeds_Db.objects.all()
    return render(request,'View_Seeds.html',
                  {'data':data})



