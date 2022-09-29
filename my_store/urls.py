from django.contrib import admin
from django.urls import path
from views import home_page, about_page, contact_page


urlpatterns = [
    path("", home_page),
    path(about_page, about_page),
    path(contact_page, contact_page),
    path('admin/', admin.site.urls),
]
