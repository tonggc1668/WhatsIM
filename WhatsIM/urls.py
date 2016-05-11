"""WhatsIM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from IMapp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home),
    url(r'^index/', views.index),
    url(r'^login/', views.login),
    url(r'^register/', views.register),
    url(r'^logout/', views.logout),
    url(r'^check_username/', views.check_username),
    url(r'^check_passwd/', views.check_passwd),
    url(r'^contact_list/', views.contact_box),
    url(r'^chat_box/', views.chat_box),

    url(r'^pushMessage/', views.push_message),
    url(r'^pullMessage/', views.pull_message),
    url(r'^addContact/', views.add_contact),
    url(r'^getContactList/', views.get_contact_list),

    url(r'^chat_with_contact/', views.chat_with_contact),
    url(r'^get_chat_with/', views.get_chat_with),
]
