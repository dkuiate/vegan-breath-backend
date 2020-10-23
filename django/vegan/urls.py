from django.urls import path

from vegan import views


app_name = 'vegan'

urlpatterns = [
    path('', views.index , name='index'),
    path('recettes', views.listingRecette , name = 'recettes'),
    path('restaurants', views.listingRestaurant , name = 'restaurants'),
    path('shops', views.listingShop , name = 'shops'),
    

]