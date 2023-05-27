from rest_framework.views import APIView
from django.http import JsonResponse
from tutorial.dataclasses import TutorialRequestBody

from utils.error_utils import error_handler
from utils.request_validator import validator


class TutorialApi(APIView):
    @error_handler
    @validator(TutorialRequestBody)
    def post(self, request):
        return JsonResponse({'message': 'Hello World!'})