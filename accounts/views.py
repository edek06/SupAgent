from django.shortcuts import render, redirect #erweiter um redirect → "zurück zur Seite"
from django.contrib.auth.models import User # Modul USER für die Benutzerverwaltung
from django.contrib import auth # Autherntifizierung/Anmeldung

def login(request):
    if request.user.is_authenticated:
        return redirect('ticketportal:tickets')
    elif request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('ticketportal:tickets')
        else:
            return render(request, 'accounts/login.html', {'error': 'Username or password is incorrect. Try again!'})
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return render(request, 'accounts/logout.html')

def signup(request):
    if request.method == 'POST': # wenn wir die Informationen schicken wollen dann...
        if request.POST['password1'] == request.POST['password2']: # wenn das Passwort übereinstimmt
            try: # versucht
                user = User.objects.get(username=request.POST['username']) # hier wird geprüft, ob der Benutzer bereits existiert
                return render(request, 'accounts/signup.html', {'error':'Username already exist!'}) # wenn existiert dann Fehlermeldung vorbereiten und wieder die gleiche Seite mit der Fehlermeldung anzeigen
            except User.DoesNotExist: # wenn der Benutzer noch nicht existiert und das Passwrt übereinstimmt
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1']) # Benutzer erstellen
                auth.login(request, user) # den Benutzer anmelden
                return redirect('ticketportal:tickets') # und zurück zur Homepage
        return render(request, 'accounts/signup.html', {'error': 'Password not match!'}) # wenn die Passwörter nicht übereinstimmen
    else:
        return render(request, 'accounts/signup.html') # wenn das Formular nicht die Methode POST ist sondern GET