import json
from loguru import logger
from django.utils.deprecation import MiddlewareMixin

class LogAPIMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # Log incoming request details
        logger.info(f"Incoming Request: {request.method} {request.path}")
        if request.body:
            try:
                body = json.loads(request.body)
                logger.info(f"Request Body: {json.dumps(body, indent=2)}")
            except json.JSONDecodeError:
                logger.info("Request Body: [Non-JSON Data]")

    def process_response(self, request, response):
        # Log outgoing response details
        logger.info(f"Outgoing Response: {response.status_code} {request.path}")
        try:
            logger.info(f"Response Body: {response.content.decode('utf-8')}")
        except Exception as e:
            logger.warning(f"Could not decode response body: {e}")
        return response
