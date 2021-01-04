from django.urls import path

from  vegan import views


app_name = 'vegan'

urlpatterns = [
    path('restaurants', views.restaurantList , name = 'restaurants'),
    path('addRestaurants', views.createRestaurant , name = 'create_restaurants'),
    path('recettes', views.recetteList, name = 'recettes'),
    path('addRecette', views.createRecette , name = 'create_recette'),
    path('shops', views.shopList , name = 'shops'),
    path('addShop', views.createShop , name = 'create_shop'),
]