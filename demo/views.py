from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from demo.models import Article, LigneCommande, Commande, Customer, Patient
from .forms import ArticleForm
from  django.contrib import messages
from django.db import transaction
from django.shortcuts import render
from twilio.rest import Client
from django.conf import settings
from demo.serializers import ArticleSerializer, CustomerSerializer, PatientSerializer
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth import  login, logout, authenticate, get_user_model
Patient = get_user_model()
from django.views import View
from django.http import JsonResponse



class LoginView(View):
    def post(self, request, *args, **kwargs):
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        
        user = authenticate(request, phone=phone, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'message': 'Logged in successfully.'})
        else:
            return JsonResponse({'message': 'Invalid credentials.'}, status=401)

class LogoutView(View):
    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            logout(request)
            return JsonResponse({'message': 'Logged out successfully.'})
        else:
            return JsonResponse({'message': 'User is not authenticated.'}, status=401)


 
class ArticleViewset(ModelViewSet):
 
    serializer_class = ArticleSerializer
    
    def get_queryset(self):
        return Article.objects.all()
    

    
    
    
    
class CustomerViewset(ModelViewSet):
 
    serializer_class = CustomerSerializer
 
    def get_queryset(self):
        return Customer.objects.all()
    
    
    
    
class PatientViewset(ModelViewSet):
 
    serializer_class = PatientSerializer
 
    def get_queryset(self):
        return Patient.objects.all()




def home(request):
    articles = Article.objects.all()
    commandes = Commande.objects.all()
    #articles = Article.objects.filter(prix)
    #print(articles)
    context = {"articles":articles, "commandes":commandes}
    return render(request, 'demo/home.html', context)


    
    
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            article_enregistre = form.cleaned_data.get('nom_article')
            messages.success(request, f"{article_enregistre}, ajouté avec succes")
            return HttpResponseRedirect('/')
        else:
            messages.error(request, "veuillez verifier les données ssaisies")
            return render(request, 'demo/create.html', {"form":form})
    else:
        form = ArticleForm()

    return render(request, 'demo/create.html', {"form":form}) 







def envoyer_message(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        destinataire = request.POST.get('destinataire')

        # Initialiser le client Twilio
        client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

        # Envoyer le message
        message = client.messages.create(
            body=message,
            from_='+18159348590',
            to=destinataire
        )

        return render(request, 'demo/message_envoye.html', {'message': message})

    return render(request, 'demo/message_envoye.html')





def commande(request):
    if request.method == 'POST':
        supplier_id = request.POST.get('fournisseur')
        supplier = Customer.objects.get(pk=supplier_id)
        date_commande = request.POST.get('date_commande')
        commande = Commande.objects.create(client=supplier,
                                            date_commande=date_commande,
                                                        
                                            )
        selected_products = request.POST.getlist('articles')
        number = 0
        with transaction.atomic():
            for article_id in selected_products:
                number += 1
                quantity = int(request.POST.get(f'quantity-{number}'))
                article = Article.objects.get(id=article_id)
                # Vérifiez si la quantité demandée est disponible
                article.save()

                LigneCommande.objects.create(commande=commande,
                                                     article=article,
                                                     quantite=quantity)
        messages.success(request, 'Votre commande a été passée avec succès!')
        return redirect('/')

    else:
        
        articles = Article.objects.all()
        
        suppliers = Customer.objects.all()
        
        context = {'articles': articles, "suppliers":suppliers}
        return render(request, 'demo/commande.html', context)