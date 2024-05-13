from xml.dom import ValidationErr
from django.shortcuts import render
from django.http import JsonResponse
from .models import Image
from rest_framework.decorators import api_view
from rest_framework import serializers
from .serializers import ImageSerializer  # Import from serializers.py
import os
from findObject import YOLO_Test
from .YOLO_Test import objectFinder

def index(request):
    return render(request,'index.html')

def photo(request):
    return render(request, 'foto.html')

def video(request):
    return render(request, 'video.html')

def main(request):
    return render(request, 'templates/foto.html')

@api_view(['POST'])
def upload_image(request):
    if request.method == 'POST':
        # Access the image file from request.FILES
        image_file = request.FILES.get('image_file')
        if image_file:
            try:
                image = Image.objects.create(name=image_file.name, image_file=image_file)
                serializer = ImageSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()

                # Save the image file to a temporary location
                image_path = os.path.join('/tmp', image.name)
                with open(image_path, 'wb') as f:
                    f.write(image_file.read())

                # Analyze the image using objectFinder
                objects_detected = objectFinder(image_path)

                # Remove the temporary file
                os.remove(image_path)

                # Build the JSON response with the detected objects
                response_data = {
                    'status': 'success',
                    'image_id': image.id,
                    'objects_detected': objects_detected
                }

                return JsonResponse(response_data)
                    
            except ValidationErr as e:
                # Handle validation error
                return JsonResponse({'status': 'error', 'message': str(e)})
            return JsonResponse({'status': 'success'})
        else:
            # Handle the case where no image file was uploaded
            return JsonResponse({'status': 'error', 'message': 'No image file uploaded'})
    else:
        return JsonResponse({
            'status': 'error',
            'message': 'Неверный метод запроса.'
        })