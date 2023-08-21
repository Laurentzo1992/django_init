from django.db import models



class Article(models.Model):
    nom_article = models.CharField(max_length=100, null=True, blank=True, verbose_name='Nom de l\'article')
    prix = models.FloatField()
    description = models.TextField()
    
    
    
    def __str__(self):
        return self.nom_article
    
    
    
class Customer(models.Model):
    nom_prenom = models.CharField(max_length=100, null=True, blank=True, verbose_name='Nom du client')
    telephone = models.IntegerField()
    
    
    def __str__(self):
        return self.nom_prenom
    
    
    
class Commande(models.Model):
    articles = models.ManyToManyField(Article, through='LigneCommande')
    client = models.ForeignKey(Customer, null=True, blank=True, on_delete=models.CASCADE)
    date_commande = models.DateField(null=True, blank=True)
    create_at = models.DateField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.client.nom_prenom
    
    
    
    
class LigneCommande(models.Model):
    article = models.ForeignKey(Article, null=True, blank=True, on_delete=models.CASCADE)
    commande = models.ForeignKey(Commande, null=True, blank=True, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField()
    create_at = models.DateField(auto_now_add=True, null=True, blank=True)
    
    
    
    def __str__(self):
        return self.commande.date_commande
    
   
    

    
    
    
