from django.urls import path
from AdminApp import views

urlpatterns = [
    path('baseFarmer/', views.baseFarmer, name='baseFarmer'),
    path('indexFarmer/', views.indexFarmer, name='indexFarmer'),
    path('viewFarmer/', views.viewFarmer, name='viewFarmer'),
    path('save_Farmer_data/', views.save_Farmer_data, name='save_Farmer_data'),
    path('Edite_farmers/<int:farmer_id>/', views.Edite_farmers, name='Edite_farmers'),
    path('update_farmer/<int:f_id>/', views.update_farmer, name='update_farmer'),
    path('Add_Seeds/', views.Add_Seeds, name='Add_Seeds'),
    path('Save_SeedsData/', views.Save_SeedsData, name='Save_SeedsData'),
    path('View_Seeds/', views.View_Seeds, name='View_Seeds'),

]
