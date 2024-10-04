from django.shortcuts import render

from app.forms import CreateLoadPictureForm
from app.models import Picture


def index(request):
    return render(request, 'index.html')

def load_picture(request):
    if request.method == 'POST':
        form = CreateLoadPictureForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img = form.instance
            path_pict = request.build_absolute_uri(img.image.url)
            context = {'form': form, 'img': img, 'path_pict': path_pict}
            return render(request, 'load_picture.html', context)
    else:
        form = CreateLoadPictureForm()
    return render(
        request,
        'load_picture.html',
        {'form': form}
    )

def detail(request, pk):
    get_pct = Picture.objects.get(pk=pk)
    return render(request, 'detail.html', {'get_pct': get_pct})