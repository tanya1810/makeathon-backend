from django.shortcuts import render
from .models import Resource

# Create your views here.
def all_resources(request):
    resources = Resource.objects.all()
    context = {
        'resources' : resources,
    }
    print(resources)
    return render(request, 'resources/all_resources.html', context)
    