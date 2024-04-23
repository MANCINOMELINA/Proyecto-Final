from django.urls import path
from .views import (
    home_view, 
    create_view, 
    list_view, 
    detail_view, 
    filter_by_profesor, 
    filter_by_suplente,
    ClaseCreateView,
    ProfesorCreateView,
    user_login_view,
    user_creation_view,
    user_logout_view,
    UserUpdateView,
)

urlpatterns = [
    path("", home_view, name ="home"),
    path("crear/<profesor>/<suplente>/<nivel>/<descripcion>/<estado>", create_view),
    path("list/", list_view, name = "reserves-list"),
    path("detail/<int:reserves_id>", detail_view, name ="detail_view"),
    path('filter/profesor/<str:profesor_name>/', filter_by_profesor, name ='filter_by_profesor'),
    path('filter/suplente/<str:suplente_name>/', filter_by_suplente, name ='filter_by_suplente'),
    path("create/clases/", ClaseCreateView.as_view(), name ="clases_create"),
    path("create/profesor/", ProfesorCreateView.as_view(), name = "profesor_create"),
    path("crear-usuario/", user_creation_view, name ="crear-usuario"),
    path("login/", user_login_view, name ="login"),
    path("logout/", user_logout_view, name ="logout"),
    path('editar-perfil/', UserUpdateView.as_view(), name ='editar-perfil'),
]