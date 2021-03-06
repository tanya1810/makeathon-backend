from django.shortcuts import render, redirect
from .models import *
from .forms import *
from PyPDF2 import PdfFileWriter, PdfFileReader


# Create your views here.
def all_resources(request):
    resources = Resource.objects.order_by('-id')
    context = {
        'resources' : resources,
    }
    return render(request, 'resources/all_resources.html', context)

def post_resource(request):
    if request.method == "POST":
        form = NewResourceForm(request.POST, request.FILES)
        if form.is_valid():
            print("help")
            f = form.save()
            pages_to_keep = [1] # page numbering starts from 0
            infile = PdfFileReader(f.pdf_file, 'rb')
            output = PdfFileWriter()

            for i in pages_to_keep:
                p = infile.getPage(i)
                output.addPage(p)

            with open('media/preview/'+str(f.id)+'_preview.pdf', 'wb+') as fi:
                output.write(fi)    

            f.preview = 'media/preview/'+str(f.id)+'_preview.pdf'
            f.owner_id = request.user
            f.save()

            return redirect('all-resources')

    else:
        form = NewResourceForm()

    context = {
        'form' : form,
    }

    return render(request, 'resources/resource_form.html', context)
