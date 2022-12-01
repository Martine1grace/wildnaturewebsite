from django.http import request
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from core.models import TourPackage, Service, Message, Hotel, Slider, Destination
from core.forms import DayActionForm, TourPackageForm, ServiceForm, DayAction
from django.core.paginator import Paginator
# import sweetify
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

success = 'Success!'
def loginOrg(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password') 
        
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Username or password does not exist')

    context = {'page':page}
    return render(request, 'dashboardtemplates/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

def registerUser(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Something went wrong during registration')

    context = {'form':form}
    return render(request, 'dashboardtemplates/login_register.html', context)

def home(request):


    # q = request.GET.get('q') if request.GET.get('q') != None else ''

    # volcanoes = Destination.objects.filter(category=q)


    three_packages = TourPackage.objects.values('id').order_by('id')[:]
    print(three_packages)

    services = Service.objects.all()
    sliders = Slider.objects.all()
    packages = TourPackage.objects.all()
    destinations = Destination.objects.all()
    hotels = Hotel.objects.order_by("-name")[:3]
    paginator = Paginator(packages, 4) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    tour_packages = paginator.get_page(page_number)
    context = {'tour_packages':tour_packages, 'packages':packages, 'services':services, 'sliders':sliders, 'destionations':destinations, 'hotels':hotels}

    return render(request, 'core/home.html', context)



def packageDetails(request, pk_package):

    package = TourPackage.objects.get(id=pk_package)
    tour_days = package.day_actions.all()
    print(tour_days)
    context = {'package':package, 'tour_days':tour_days}
    return render(request, 'core/packageDetails.html', context)

def hotelsDetails(request):

    hotels = Hotel.objects.all()
    context = {'hotels':hotels}
    return render(request, 'hotelsDetails.html')

def allpackageDetails(request):

    package = TourPackage.objects.all()
    context = {}
    context['tourpackages'] = package
    return render(request, 'core/allpackageDetails.html')    

@login_required(login_url='/login')
def delete_package(request, pk):
    package = TourPackage.objects.get(id=pk)
    TourPackage.objects.delete(package)
    # sweetify.success(request, success, text='You have successfully deleted tour package', icon='success', timerProgressBar='true', timer=3000)
    return redirect('tour_packages')

@login_required(login_url='/login')
def package_details_admin(request, pk):
    
    package = TourPackage.objects.get(id=pk)
    
    tour_days = package.day_actions.all()
    context = {'package':package, 'tour_days':tour_days}
    return render(request, 'dashboardtemplates/packageDetailsAdmin.html', context)

def contactusPage(request):
    
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email'].lower()
        subject = request.POST['subject']
        message = request.POST['message']
        send_mail(
     subject,
    'Here is the message. from '+str(email)+', <br>'+str(message)+'',
    'info.wildnaturediscovery@gmail.com',
    ['info.wildnaturediscovery@gmail.com'],
    fail_silently=False,
)
        # send_mail(name,subject,message,'info.wildnaturediscovery@gmail.com',['info.wildnaturediscovery@gmail.com'])
        # sweetify.success(request, success, text='You have successfully submitted your suggestion', icon='success', timerProgressBar='true', timer=3000)
        return redirect('home')
    
    context = {}
    return render(request, 'core/contactusPage.html', context)

def aboutusPage(request):
    
    context = {}
    return render(request, 'core/aboutusPage.html', context)

@login_required(login_url='/login')
def tourPackages(request):
    
    packages = TourPackage.objects.all()
    paginator = Paginator(packages, 5) 

    page_number = request.GET.get('page')
    tour_packages = paginator.get_page(page_number)
    
    context = {'tour_packages':tour_packages}
    return render(request, 'dashboardtemplates/tourPackages.html', context)

@login_required(login_url='/login')
def dashboard(request):
    
    context = {}
    return render(request, 'dashboardtemplates/dashboard.html', context)

@login_required(login_url='/login')
def services(request):
    
    services = Service.objects.all()
  
    context = {'services':services}
    return render(request, 'dashboardtemplates/services.html', context)

@login_required(login_url='/login')
def messages(request):
    
    messages = Message.objects.all().order_by('-date_added')
    context = {'messages':messages}
    return render(request, 'dashboardtemplates/messages.html', context)

@login_required(login_url='/login')
def add_tour_package(request):
    title = 'Add'
    form = TourPackageForm()
    if request.method == 'POST':
        form = TourPackageForm(request.POST)
        if form.is_valid:
            form.save()
            # sweetify.success(request, success, text='You have successfully added tour package', icon='success', timerProgressBar='true', timer=3000) 
            return redirect('tour_packages')
    context = {'form':form, 'title':title}
    return render(request, 'dashboardtemplates/packageForm.html', context)

@login_required(login_url='/login')
def add_service(request):
    title = 'Add'
    form = ServiceForm()
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid:
            form.save()
            # sweetify.success(request, success, text='You have successfully added service', icon='success', timerProgressBar='true', timer=3000) 
            return redirect('services')
    context = {'form':form, 'title':title}
    return render(request, 'dashboardtemplates/serviceForm.html', context)

@login_required(login_url='/login')
def add_day_action(request, pk):
    tour_package = TourPackage.objects.get(id=pk)
    tour_package.day_actions.all()
    title = 'Add'
    form = DayActionForm()
    if request.method == 'POST':
        form = DayActionForm(request.POST)
        if form.is_valid:
            day_action = form.save()
            tour_package.day_actions.add(day_action)
            # sweetify.success(request, success, text='You have successfully added day action', icon='success', timerProgressBar='true', timer=3000) 
            return redirect('package_detail', pk=tour_package.id)
    
    context = {'title':title, 'form':form}
    return render(request, 'dashboardtemplates/dayForm.html', context)

