global user_on
user_on=None
global admin_user
admin_user=None
from django.shortcuts import render
from django.http import HttpResponsePermanentRedirect
from django.urls import reverse
from django.shortcuts import render




#renvoie le chemin d'URL réel associé au nom 'index'
def toindex(request):
    return HttpResponsePermanentRedirect(reverse('index'))

#render : charger la page index.html
def index(request):
    return render(request,'index.html')


""" if __name__ == '__main__':
    app.run(debug=True)
 """