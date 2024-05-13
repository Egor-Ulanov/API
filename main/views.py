from django.shortcuts import render
def index(request):
    return render(request,'index.html')

def photo(request):
    return render(request, 'foto.html')

def video(request):
    return render(request, 'video.html')

def main(request):
    return render(request, 'templates/foto.html')

from django.http import JsonResponse
from .models import Image
from rest_framework.decorators import api_view

@api_view(['POST'])
def upload_image(request):
    if request.method == 'POST':
        image_file = request.FILES['image_file']
        image = Image.objects.create(name=image_file.name, image_file=image_file)

        return JsonResponse({
            'status': 'success',
            'filename': image.name,
            # Добавьте другие поля JSON-ответа, если необходимо
        })
    else:
        return JsonResponse({
            'status': 'error',
            'message': 'Неверный метод запроса.'
        })