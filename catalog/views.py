from django.http import HttpResponse
from django.shortcuts import render

def contacts(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        return HttpResponse(f"Спасибо {name}! Сообщение успешно отправлено. \n <a href='/'>Каталог</a>")

    return render(request, 'contacts.html')

def home(request):
    return render(request, 'home.html')