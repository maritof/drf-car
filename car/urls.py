from django.urls import path
from .views import CarListProv, CarCreate, CarDetailProv, CarDeleteProv

urlpatterns = [
    path('cars-list/', CarListProv.as_view()),
    path('cars/', CarCreate.as_view()),
    path('cars/<id>/', CarDetailProv.as_view()),
    path('cars-delete/<id>/', CarDeleteProv.as_view()),
]
