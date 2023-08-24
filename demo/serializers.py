from rest_framework.serializers import ModelSerializer
from demo.models import Article, Customer, Patient

 
 
 
 #création des Serializer
 
 
class ArticleSerializer(ModelSerializer):
 
    class Meta:
        model = Article
        fields = ['id', 'nom_article', 'prix', 'description']
        
    
    
        
        
        
        
        
class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'nom_prenom', 'telephone']
        
        
        
class PatientSerializer(ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'phone', 'password', 'first_name', 'last_name']