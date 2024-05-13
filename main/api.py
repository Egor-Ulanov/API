from flask import Flask, request, jsonify
from ultralytics import YOLO
from collections import Counter
from findObject import YOLO_Test
from YOLO_Test import objectFinder

app = Flask(__name__)

# Определяем путь к файлам модели YOLO
model_path = 'yolov8n.pt'

# Загружаем модель YOLO
model = YOLO(model_path)

# Функция для обработки изображений
def process_images(images):
    results = []

    for image in images:
        # Используем функцию objectFinder для определения объектов на изображении
        objects = objectFinder(image)
        results.append(objects)

    return results

# Обработчик API для загрузки и обработки изображений
@app.route('/api', methods=['POST'])
def api_image_processing():
    # Получаем изображения от пользователя
    images = request.files.getlist('image')

    # Обрабатываем изображения
    processed_images = process_images(images)

    # Возвращаем результаты в формате JSON
    return jsonify(processed_images)

if __name__ == '__main__':
    app.run(debug=True)
