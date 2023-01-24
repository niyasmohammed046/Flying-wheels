from django.contrib import admin
from django.urls import path
from frontend import views


urlpatterns = [
   path('findex/',views.findex,name="findex"),
   path('contactpg/',views.contactpg,name="contactpg"),
   path('category/<itemcat>/',views.category,name="category"),
   path('messagepage/',views.messagepage,name="messagepage"),
   path('singleproduct/<int:dataid>/',views.singleproduct,name="singleproduct"),
   path('emailsub/',views.emailsub,name="emailsub"),
   path('',views.frontendloginpage,name="frontendloginpage"),
   path('bikenews/',views.bikenews,name="bikenews"),
   path('registersave/',views.registersave,name="registersave"),
   path('userloginsave/',views.userloginsave,name="userloginsave"),
   path('logout/',views.logout,name="logout")
   
]