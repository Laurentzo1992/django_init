from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager





class PatientManager(BaseUserManager):
    def create_user(self, phone, password=None, **extra_fields):
        if not phone:
            raise ValueError('The Phone field must be set')
        
        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(phone, password, **extra_fields)




class Patient(AbstractUser):
    phone = models.CharField(max_length=15, unique=True, verbose_name='Téléphone')
    date_naissance = models.DateField(null=True, blank=True, verbose_name='Date de naissance')
    first_name = None
    last_name = None
    username = None
    
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    objects = PatientManager()  # Utilisation du gestionnaire d'utilisateurs personnalisé

    def __str__(self):
        return self.phone

    
    

    

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
    
   
    

    
    
    
