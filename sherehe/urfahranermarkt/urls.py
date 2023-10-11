from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),  # Add a comma here
    path('api/dustbins/', views.DustbinsList.as_view(), name='dustbins-list'),
    path('api/food_areas/', views.FoodAreasList.as_view(), name='food-areas-list'),
    path('api/food_stalls/', views.FoodStallsList.as_view(), name='food-stalls-list'),
    path('api/info_points/', views.InfoPointsList.as_view(), name='info-points-list'),
    path('api/kids_arena/', views.KidsArenaList.as_view(), name='kids-arena-list'),
    path('api/shops/', views.ShopsList.as_view(), name='shops-list'),
    path('api/souvenirs/', views.SouvenirsList.as_view(), name='souvenirs-list'),
    path('api/stages/', views.StagesList.as_view(), name='stages-list'),
    path('api/trampoline_park/', views.TrampolineParkList.as_view(), name='trampoline-park-list'),
    path('api/washrooms/', views.WashroomsList.as_view(), name='washrooms-list'),
    path('map/', views.map_view, name='map'),
]
