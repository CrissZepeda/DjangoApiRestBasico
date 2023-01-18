
from django.contrib import admin
from django.urls import path, include
from reservas import views as reserva
from api import views as api

from rest_framework import routers

router = routers.DefaultRouter()

router.register('reserva',api.ReservaViewset)
router.register('reserva',api.ReservaDetailsViewset)

urlpatterns = [
    path('', reserva.login_user, name="login"),
    path('logout/', reserva.logout_user, name="logout"),
    path("registrarse/", reserva.registrarse, name="registrarse"),
    path('inicio/', reserva.inicio,name="inicio"),
    path('reserva/', reserva.reservas,name="reserva"),
    path('reserva/<int:id>', reserva.actualizaReserva),
    path('lista/', reserva.listReserva, name="lista"),
    path('eliminar/<int:id>', reserva.eliminarReserva),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
