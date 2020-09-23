from django.shortcuts import render

def home(request):
    return render(request, "main/home.html",{"page_title": "Pagamento Online"})