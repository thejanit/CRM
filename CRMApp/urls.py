from django.urls import path
from CRMApp import views

urlpatterns = [
    path('', views.HomePage, name='homepage'),
    path('logout/', views.LogoutUser, name='logout'),
    path('register/', views.RegisterUser, name='register'),
    path('individual-record/<int:pk>', views.IndividualRecord, name='individual-record'),
    path('delete-record/<int:pk>', views.DeleteRecord, name='delete-record'),
    path('add-record/', views.AddRecord, name='add-record'),
    path('update-record/<int:pk>', views.UpdateRecord, name='update-record')
]
