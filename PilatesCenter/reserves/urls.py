from django.urls import path
from .views import (
    home_view, 
    create_view, 
    list_view, 
    detail_view, 
    filter_by_profesor, 
    filter_by_suplente,
    ClaseCreateView,
    ProfesorCreateView
)

urlpatterns = [
    path("", home_view),
    path("crear/<profesor>/<suplente>/<nivel>/<descripcion>/<estado>", create_view),
    path("list/", list_view, name = "reserves-list"),
    path("detail/<int:reserves_id>", detail_view, name="detail_view"),
    path('filter/profesor/<str:profesor_name>/', filter_by_profesor, name='filter_by_profesor'),
    path('filter/suplente/<str:suplente_name>/', filter_by_suplente, name='filter_by_suplente'),
    path("create/clases/", ClaseCreateView.as_view(), name="clases_create"),
    path("create/profesor/", ProfesorCreateView.as_view(), name = "profesor_create"),
]