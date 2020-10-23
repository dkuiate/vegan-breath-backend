#from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Contact, Recette, Restaurant, Shop



# Create your views here.
def index(request):
  
  recettes = Recette.objects.filter().order_by('-created_at')[:4]
  restaurants = Restaurant.objects.filter().order_by('-created_at')[:4]
  shops = Shop.objects.filter().order_by('-created_at')[:4]

  formatted_recettes = ["{}".format(recette.title) for recette in recettes]
  formatted_restaurants = ["{}".format(restaurant.title) for restaurant in restaurants]
  formatted_shops = ["{}".format(shop.title) for shop in shops]

  message = """{}<br>{}<br>{}""".format(formatted_recettes,formatted_restaurants ,formatted_shops)
  context = {
      #  'recette_list': recettes,
      # 'restaurant_list': restaurants,
      #  'shop_list': shops,
   }

  return HttpResponse(message)
     #todo plus vue




def listingRecette(request):
  recettes = Recette.objects.all()
  formatted_recettes = ["{}{}".format(recette.id,recette.title) for recette in recettes]
  messageRecette = """{}""".format(formatted_recettes)
  return HttpResponse(messageRecette)


def listingRestaurant(request):
  restaurants = Restaurant.objects.all()
  formatted_restaurants = ["{}".format(restaurant.title) for restaurant in restaurants]
  messageResto = """{}""".format(formatted_restaurants)
  return HttpResponse(messageResto)


def listingShop(request):
  shops = Shop.objects.all()
  formatted_shops = ["{}".format(shop.title) for shop in shops]
  messageShop = """{}""".format(formatted_shops)
  return HttpResponse(messageShop)



# def detailRecette(request, recette_id):
#     recette = Recette.objects.get(pk=recette.id)
#     detailRecette = "{}{}".format(recette.title,recette.description)
#     return HttpResponse(detailRecette)

# def detailRestaurant(request, restaurant_id):
#     restaurant = Restaurant.objects.get(pk=restaurant_id)
#     detailRestaurant = "{}{}".format(restaurant.title,restaurant.description)
#     return HttpResponse(detailRestaurant)

# def detailShop(request, shop_id):
#     shop = Shop.objects.get(pk=shop_id)
#     detailShop = "{}{}".format(shop.title,shop.description)
#     return HttpResponse(detailShop)











# def search(request):
#     query = request.GET.get('query')
#     if not query:
#         message = "Aucun artiste n'est demandé"
#     else:
#         recettes = [
#             recette for recette in Recette
#             if query in " ".join(artist['name'] for artist in recette['artists'])
#         ]

#         if len(recettes) == 0:
#             message = "Misère de misère, nous n'avons trouvé aucun résultat !"
#         else:
#             recettes = ["<li>{}</li>".format(recette['name']) for recette in recettes]
#             message = """
#                 Nous avons trouvé les recettes correspondant à votre requête ! Les voici :
#                 <ul>
#                     {}
#                 </ul>
#             """.format("</li><li>".join(recettes))

#     return HttpResponse(message)