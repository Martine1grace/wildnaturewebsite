from django.contrib import admin
from django.urls import path

from core.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', loginOrg, name='login'),
    path('logoutUser/', logoutUser, name='logoutUser'),
    path('register/', registerUser, name='register'),
    path('', home, name='home'),
    path('package_details/<str:pk_package>', packageDetails, name='package_details'),
    path('contact_us', contactusPage, name='contact_us'),
    path('about_us', aboutusPage, name='about_us'),
    path('hotels_details', hotelsDetails, name='hotels_details'),
    path('allpackage_details', allpackageDetails, name='allpackage_details'),

    path('dashboard', dashboard, name='dashboard'),

    path('tour_packages', tourPackages, name='tour_packages'),
    path('add_package', add_tour_package, name='add_package'),
    path('delete_package/<str:pk>/', delete_package, name='delete_package'),
    path('add_day_action/<str:pk>/', add_day_action, name='add_day_action'),

    path('package_detail/<str:pk>', package_details_admin, name='package_detail'),

    path('services', services, name='services'),
    path('add_service', add_service, name='add_service'),

    path('messages', messages, name='messages'),

]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)