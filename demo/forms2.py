from django import forms
from demo.models import Article
from django.core.validators import RegexValidator
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField
Patient = get_user_model()

class ArticleForm(forms.ModelForm):
    
    nom_article = forms.CharField(
        label='Nom',
        widget=forms.TextInput(attrs={'placeholder': 'Nom de l\'article'})
    )
    

    class Meta:
        model = Article
        fields = '__all__'
        
        




class RegisterForm(forms.ModelForm):
    """
    The default

    """

    password = forms.CharField(widget=forms.PasswordInput)
    password_2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = Patient
        fields = ['phone']

    def clean_email(self):
        '''
        Verify phone is available.
        '''
        phone = self.cleaned_data.get('phone')
        qs = Patient.objects.filter(phone=phone)
        if qs.exists():
            raise forms.ValidationError("le numero est pris")
        return phone

    def clean(self):
        '''
        Vérifiez que les deux mots de passe correspondent.
        '''
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_2 = cleaned_data.get("password_2")
        if password is not None and password != password_2:
            self.add_error("password_2", "Your passwords must match")
        return cleaned_data


class UserAdminCreationForm(forms.ModelForm):
    """
    Un formulaire pour créer de nouveaux utilisateurs. Comprend tout le nécessaire
    champs, plus un mot de passe répété.
    """
    password = forms.CharField(widget=forms.PasswordInput)
    password_2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = Patient
        fields = ['phone']

    def clean(self):
        '''
        Vérifiez que les deux mots de passe correspondent.
        '''
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_2 = cleaned_data.get("password_2")
        if password is not None and password != password_2:
            self.add_error("password_2", "Your passwords must match")
        return cleaned_data

    def save(self, commit=True):
        # Enregistrez le mot de passe fourni au format haché
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class UserAdminChangeForm(forms.ModelForm):
    """Un formulaire pour mettre à jour les utilisateurs. Inclut tous les champs sur
    l'utilisateur, mais remplace le champ du mot de passe par celui de l'administrateur
    champ d'affichage du hachage du mot de passe.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Patient
        fields = ['phone', 'password', 'is_active']

    def clean_password(self):
    # Indépendamment de ce que l'utilisateur fournit, renvoie la valeur initiale.
    # Cela se fait ici, plutôt que sur le terrain, car le
    # le champ n'a pas accès à la valeur initiale
        return self.initial["password"]
        
        
        
