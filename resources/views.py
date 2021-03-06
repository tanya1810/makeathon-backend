from django.shortcuts import render
from .models import Resource

# Create your views here.
def all_resources(request):
    resources = Resource.objects.order_by(['-id'])
    context = {
        'resources' : resources,
    }
    return render(request, 'resource/all_resources.html', context)


    