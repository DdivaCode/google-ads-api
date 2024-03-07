from django.contrib import admin
from django.contrib.admin import AdminSite
from  .models import  News
# Register your models here.
class MyEmsAdminSite(AdminSite):

    site_title = 'googleadss admin'
    #
    site_header = 'googleadss admin'
    #
    index_title = 'googleadss admin'



myems_admin_site = MyEmsAdminSite()

