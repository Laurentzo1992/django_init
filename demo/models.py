from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, AbstractBaseUser
from re import M

class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Crée et enregistre un utilisateur avec l'e-mail et le mot de passe donnés.
        """
        if not email:
            raise ValueError('Les utilisateurs doivent avoir une adresse e-mail')




        user = self.model(
        email=self.normalize_email(email),
        )




        user.set_password(password)
        user.save(using=self._db)
        return user




    def create_staffuser(self, email, password):
        """
        Crée et enregistre un utilisateur du staff avec l'e-mail et le mot de passe donnés.
        """
        user = self.create_user(
        email,
        password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user




    def create_superuser(self, email, password):
        """
        Crée et enregistre un superutilisateur avec l'e-mail et le mot de passe donnés.
        """
        user = self.create_user(
        email,
        password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user



class User(AbstractBaseUser):

    objects = UserManager()
    email = models.EmailField(
    verbose_name='email address',
    max_length=255,
    unique=True,
    )

    phone = models.CharField(max_length=100, default="345656")

    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False) # a admin user; non super-user
    admin = models.BooleanField(default=False) # a superuser
    # remarquez l'absence du "champ password", c'est intégré pas besoin de preciser.
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] # Email & Password sont requis par défaut.
    def get_full_name(self):
    # L'utilisateur est identifié par son adresse e-mail
        return self.email
    def get_short_name(self):
    # L'utilisateur est identifié par son adresse e-mail
        return self.email

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "L'utilisateur a-t-il une autorisation spécifique ?"
    # Réponse la plus simple possible : Oui, toujours
        return True

    def has_module_perms(self, app_label):
        "L'utilisateur dispose-t-il des autorisations nécessaires pour voir l'application ?`app_label`?"
    # Réponse la plus simple possible : Oui, toujours
        return True
        
    @property
    def is_staff(self):
        "L'utilisateur est-il un membre du personnel ?"
        return self.staff
    @property
    def is_admin(self):
        "L'utilisateur est-il un membre administrateur?"
        return self.admin
    
    




    
    

    

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
    
   
    

    
    
    
