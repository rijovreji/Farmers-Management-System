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
