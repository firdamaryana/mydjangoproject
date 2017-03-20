from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to My Second Project!")

def about(request):
    return HttpResponse("This is About Page!")
