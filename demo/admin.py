from django.contrib import admin
from demo.models import Article, Commande, LigneCommande, Customer


admin.site.register(Article)
admin.site.register(Customer)
admin.site.register(Commande)
admin.site.register(LigneCommande)

# Register your models here.
