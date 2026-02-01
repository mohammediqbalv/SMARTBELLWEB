
from django.contrib import admin
from django.urls import path

from MyApp import views

urlpatterns = [

    path('login/',views.login),
    path('login_post/',views.login_post),
    path('addpolicestation/',views.addpolicestation),
    path('addpolicestation_post/',views.addpolicestation_post),
    path('changepassword/',views.changepassword),
    path('changepassword_post/',views.changepassword_post),
    path('editpolicestation/<id>',views.editpolicestation),
    path('editpolicestation_post/',views.editpolicestation_post),
    path('delete_policestation/<id>', views.delete_policestation),

    path('sendreply/<id>',views.Sendreply),
    path('Sendreply_post/',views.Sendreply_post),
    path('viewcomplaint/',views.Viewcomplaint),
    path('Viewcomplaint_post/',views.Viewcomplaint_post),
    path('viewpolicestation/',views.Viewpolicestation),
    path('Viewpolicestation_post/',views.Viewpolicestation_post),
    path('viewregisterdhouseowners/',views.Viewregisteredhouseowners),
    path('Viewregisteredhouseowners_post/',views.Viewregisteredhouseowners_post),
    path('Viewsuggestions_post/',views.Viewsuggestions_post),
    path('viewsuggestions/',views.ViewSuggestions),
    path('ahome/',views.ahome),
    path('admin_view_criminallist/',views.admin_view_criminallist),


    path('policehome/',views.policehome),
    path('addcrimehistory/',views.addcrimehistory),
    path('addcrimehistory_post/',views.addcrimehistory_post),
    path('addcriminal/',views.addcriminal),
    path('addcriminal_post/',views.addcriminal_post),
    path('police_changepassword/',views.police_changepassword),
    path('police_changepassword_post/',views.police_changepassword_post),
    path('editcrimehistory/',views.editcrimehistory),
    path('editcrimehistory_post/',views.editcrimehistory_post),
    path('editcriminal/<id>',views.editcriminal),
    path('editcriminal_post/',views. editcriminal_post),
    path('viewcrimehistory/',views. viewcrimehistory),
    path('viewcrimehistory_post/',views. viewcrimehistory_post),
    path('viewcriminal/',views. viewcriminal),
    path('viewcriminal_post/',views.viewcriminal_post),
    path('viewcriminal_post/',views.viewcriminal_post),
    path('deleteCriminal/<id>',views.deleteCriminal),
    path('viewprofile/',views.viewprofile),

    ####################houseowner#################
    path('flutt_login/',views.flutt_login),
    path('flutt_changepassword/',views.flutt_changepassword),
    path('flutt_register/',views.flutt_register),
    path('flutt_viewprofile/',views.flutt_viewprofile),
    path('flutt_manageuserdetails/',views.flutt_manageuserdetails),
    path('flutt_viewcriminals/',views.flutt_viewcriminals),
    path('flutt_sendsuggestions/',views.flutt_sendsuggestions),
    path('flutt_viewcriminaldetection/',views.flutt_viewcriminaldetection),
    path('flutt_sendcomplaint/',views.flutt_sendcomplaint),
    path('flutt_viewreply/',views.flutt_viewreply),
    path('flutt_cameramanagement/',views.flutt_cameramanagement),
    path('flutt_viewuser/',views.flutt_viewuser),
    path('flutt_editprofile/',views.flutt_editprofile),
    path('flutt_deleteuser/',views.flutt_deleteuser),
    path('flutt_edituserget/',views.flutt_edituserget),
    path('flutt_editfamilymember/',views.flutt_editfamilymemeber),
    path('Viewnotificationalert/',views.Viewnotificationalert),
    path('flutt_viewpolicestation/',views.flutt_ViewPolicestation),
    path('deletecriminaldetection/',views.deletecriminaldetection),
    path('qr_checking/',views.qrchecking)
    ,
    path('houseownerhome/', views.houseownerhome),
]
