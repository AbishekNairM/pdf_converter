from django.shortcuts import render, redirect
from django.views.generic import DetailView
from .forms import FileCreateForm
from .models import Text
from pdf2image import convert_from_path
import pytesseract
from PIL import Image
import os
from django.conf import settings

def convert(filepath):
    txt = ""
    if filepath[-3:] == "pdf":
        doc = convert_from_path(filepath)
        for im in doc:
            txt += pytesseract.image_to_string(im)
            txt += '\n'
    elif filepath[-3:] in ['jpg', 'png'] or filepath[-4:] in ['jpeg', 'webp']:
        im = Image.open(filepath)
        txt = pytesseract.image_to_string(im)
    else:
        txt = "File format not supported"
    return txt

def file_upload_view(request):
    if request.method == 'POST':
        form = FileCreateForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.save(commit=False)
            form.save()
            filepath = os.path.join(settings.MEDIA_ROOT, file.document.name)
            converted_text = convert(filepath)
            new_text = Text.objects.create(text=converted_text, file_associated=file)
            return render(request, 'pdfinfo.html', {'pk': new_text.pk, 'text': converted_text})
    else:
        form = FileCreateForm()
    return render(request, 'acceptPDF.html', {'form': form})

class TextDetailView(DetailView):
    model = Text
    template_name = 'pdfinfo.html'
    context_object_name = 'text'
