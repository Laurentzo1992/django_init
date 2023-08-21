from django import forms
from demo.models import Article
from django.core.validators import RegexValidator


### FORM CONTRAT ###

class ArticleForm(forms.ModelForm):
    
    nom_article = forms.CharField(
        label='Nom',
        widget=forms.TextInput(attrs={'placeholder': 'Nom de l\'article'})
    )
    

    class Meta:
        model = Article
        fields = '__all__'