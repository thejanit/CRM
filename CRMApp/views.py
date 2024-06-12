from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegistrationForm, AddRecordsForm
from CRMApp.models import Customer

# Create your views here.

def HomePage(request):
    
    if request.method == "POST":
        username = request.POST['Username']
        password = request.POST['password']
        
        # Authentication Check
        userAuth = authenticate(request, username=username, password=password)
        if userAuth is not None:
            login(request, userAuth)
            messages.success(request, f"Hi {username}, you are successfully logged into the CRM !!!")
            return redirect('homepage')
        else:
            messages.success(request, "It seema there is some error while logging in. Please try again after sometime.")
            return redirect('homepage')
    else:
        # Fetching All records from Customer model
        customer_data = Customer.objects.all()
        return render(request, 'homepage.html', {'customer_data':customer_data})


def LogoutUser(request):
    logout(request)
    messages.success(request, "You have been successfully logged out !!")
    return redirect('homepage')


def RegisterUser(request):
    
    # Registration Form Saving
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            # Authentication and User Login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            userAuth = authenticate(username=username, password=password)
            login(request, userAuth)
            messages.success(request, f"Hey {username}, your registration has been done :) and you are logged in successfully!!!")
            return redirect('homepage')
    else:
        form = RegistrationForm()
        return render(request, 'register.html', {'form':form})
    
    return render(request, 'register.html', {'form':form})


def IndividualRecord(request, pk):
    # Fetching Single specific record
    if request.user.is_authenticated:
        individual_record = Customer.objects.get(id=pk)
        return render(request, 'individual_record.html', {'individual_record':individual_record})
    
    else:
        messages.success(request, "Hey, you must be authenticated to view the records. Please Log in to proceed further.")
        return redirect('homepage')
    
    
def DeleteRecord(request, pk):
    # Deleting Single Specific record
    if request.user.is_authenticated:
        del_record = Customer.objects.get(id=pk)
        del_record.delete()
        messages.success(request, "Your requested record is deleted successfully.")
        return redirect('homepage')
    
    else:
        messages.success(request, "Hey, you must be authenticated to delete any records. Please Log in to proceed further.")
        return redirect('homepage')


def AddRecord(request):
    # Adding records to the model
    form = AddRecordsForm(request.POST)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                form.save()
                messages.success(request, "The new record has been added successfully.")
                return redirect('homepage')
        else:
            return render(request, 'add_record.html', {'form':form})
    else:
        messages.success(request, "Hey, you must be authenticated to add the new records. Please Log in to proceed further.")
        return render(request, 'add_record.html', {'form':form})
                

def UpdateRecord(request, pk):
    if request.user.is_authenticated:
        current_record = Customer.objects.get(id=pk)
        form = AddRecordsForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record Has Been updated successfully!!!")
            return redirect('homepage')
        else:
            return render(request, 'update_record.html', {'form':form})
    else:   
        messages.success(request, "Hey, you must be authenticated to update the existing records. Please Log in to proceed further.")
        return redirect('homepage')
