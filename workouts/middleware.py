import time

class PageLoadTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        
    def __call__(self, request):
        # Отсчет времени
        start_time = time.time()
        # Запрос уходит во view для обработки
        response = self.get_response(request)
        # Финиш и вычисление разницы
        duration = time.time() - start_time
        print(f'Врем генерации страницы - {duration:.3f} сек.')
            
        return response
    