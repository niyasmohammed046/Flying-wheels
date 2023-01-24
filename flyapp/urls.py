from django.contrib import admin
from django.urls import path
from flyapp import views

urlpatterns = [

#product(bike)

   path('index/',views.index,name="index"),
   path('addbike/',views.addbike,name="addbike"),
   path('savebike/',views.savebike,name="savebike"),
   path('showbike/',views.showbike,name="showbike"),
   path('editbike/<int:dataid>/',views.editbike,name="editbike"),
   path('updatebike/<int:dataid>/',views.updatebike,name="updatebike"),
    path('deletebike/<int:dataid>/',views.deletebike,name="deletebike"),


#category

    path('addcategory/',views.addcategory,name="addcategory"),
    path('savecategory/',views.savecategory,name="savecategory"),
    path('showcategory/',views.showcategory,name="showcategory"),
    path('editcategory/<int:dataid>/',views.editcategory,name="editcategory"),
    path('updatecategory/<int:dataid>/',views.updatecategory,name="updatecategory"),
    path('deletecategory/<int:dataid>/',views.deletecategory,name="deletecategory"),

#admin
    path('addadmin/',views.addadmin,name="addadmin"),
    path('saveadmin/',views.saveadmin,name="saveadmin"),
    path('showadmin/',views.showadmin,name="showadmin"),


#message
    path('showmessage/',views.showmessage,name="showmessage"),
    path('deletemessage/<int:dataid>',views.deletemessage,name="deletemessage"),

#email

    path('showemail/',views.showemail,name="showemail"),
    path('deleteemail/<int:dataid>',views.deleteemail,name="deleteemail"),

#login

    path('adminlogin/',views.adminlogin,name="adminlogin"),
    path('loginauth/',views.loginauth,name="loginauth")
]