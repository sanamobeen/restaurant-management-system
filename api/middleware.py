import time
from django.utils.deprecation import MiddlewareMixin


class TimerMiddleware(MiddlewareMixin):
    def process_request(self, request):
        total = 0
        for i in range(10000000):
            total += i


class TimerMiddleware(MiddlewareMixin):
    def process_request(self, request):
        request.start_time = time.time)
        logging.basicConfig(
    filename="access.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
)

class TimerMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        logging.info(f"{request.path}")
        return response
