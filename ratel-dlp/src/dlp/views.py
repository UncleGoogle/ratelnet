from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from .scanner import scan_content


@method_decorator(csrf_exempt, name="dispatch")
class CheckContentView(View):
    def post(self, request):
        binary_content = request.FILES.get('content')

        regex_patterns = []  # dummy
        checks = scan_content(binary_content, regex_patterns)

        response_data = {
            'ok': all(checks.values())
        }
        return JsonResponse(response_data)

    def get(self, request):
        return JsonResponse({'error': 'Invalid request method'}, status=405)
