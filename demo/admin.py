from django.contrib import admin
from demo.models import Article, Commande, LigneCommande, Customer
from .models import Patient

class PatientAdmin(admin.ModelAdmin):
    list_display = ('phone', 'date_naissance', 'is_staff')  # Champs à afficher dans la liste
    list_filter = ('is_staff', 'is_superuser')  # Filtres sur le côté droit
    search_fields = ('phone', 'first_name', 'last_name')  # Barre de recherche
    
    

# Enregistrement du modèle Patient avec la classe d'administration personnalisée
admin.site.register(Patient, PatientAdmin)
admin.site.register(Article)
admin.site.register(Customer)
admin.site.register(Commande)
admin.site.register(LigneCommande)

# Register your models here.
