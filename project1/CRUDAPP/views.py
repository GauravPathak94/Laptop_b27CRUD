from django.shortcuts import render, redirect
from .forms import LaptopForm
from .models import Laptop
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='loginpage_url')
def LaptopView(request):
    form = LaptopForm()
    template_name = 'CRUDAPP/lapform.html'
    context = {'form': form}
    if request.method == 'POST':
        form = LaptopForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('showlap_url')
    return render(request, template_name, context)

@login_required(login_url='loginpage_url')
def showLaptopView(request):
    data = Laptop.objects.all()
    template_name = 'CRUDAPP/showlap.html'
    context = {'obj': data}
    return render(request, template_name, context)

def updateLaptopView(request, id):
    obj = Laptop.objects.get(id = id)  #(primarykey_col_name = parameter_name)
    form = LaptopForm(instance=obj)
    template_name = 'CRUDAPP/lapform.html'
    context = {'form': form}
    if request.method == 'POST':
        form = LaptopForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('showlap_url')
    return render(request, template_name, context)

def deleteLaptopView(request,id):
    obj = Laptop.objects.get(id = id)  #(primarykey_col_name = parameter_name)
    template_name = 'CRUDAPP/confirmation.html'
    context = {'obj': obj}
    if request.method == 'POST':
        obj.delete()
        return redirect('showlap_url')
    return render(request, template_name, context)

'''
user id = b27
password = b27

login id: Gaurav
password: g12345678
'''