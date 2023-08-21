from rest_framework.serializers import ModelSerializer
from demo.models import Article, Customer
from django.contrib.auth.models import User
 
class ArticleSerializer(ModelSerializer):
 
    class Meta:
        model = Article
        fields = ['id', 'nom_article', 'prix', 'description']
        
        
        
        
        
class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'nom_prenom', 'telephone']
        
        
        
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']