from  . import views
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from demo.views import ArticleViewset, CustomerViewset, PatientViewset

# Ici nous créons notre routeur
router = routers.SimpleRouter()
# Puis lui déclarons une url basée sur le mot clé ‘category’ et notre view
# afin que l’url générée soit celle que nous souhaitons ‘/api/article/’
router.register('article', ArticleViewset, basename='article')
router.register('customer', CustomerViewset, basename='customer')
router.register('patient', PatientViewset, basename='patient')


urlpatterns = [
    path('',  views.login_page, name='login'),
    path('logout_user',  views.logout_user, name='logout_user'),
    path('home',  views.home, name='home'),
    path('create',  views.create, name='create'),
    path('commande',  views.commande, name='commande'),
    path('envoyer_message',  views.envoyer_message, name='envoyer_message'),
    path('api/', include(router.urls))  # Il faut bien penser à ajouter les urls du router dans la liste des urls disponibles.
]

