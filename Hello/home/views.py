from django.shortcuts import render, HttpResponse

def index(request):
    context ={
        'variable':"Welcome to Afiya Website"
    }
    return render (request, 'index.html',context)

def nature(request):
    return render (request, 'nature.html')

def car(request):
    return render (request, 'car.html')

def cuteanimals(request):
    return render (request, 'cute-animals.html')

def common(request):
    return render (request, 'common.html')
def colors(request):
    return render (request, 'colors.html')
def contact(request):
    return render (request, 'contact.html')
