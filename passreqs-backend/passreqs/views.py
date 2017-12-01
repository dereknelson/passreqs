from django.http import JsonResponse

from .models import Website


def get_pass_reqs(request):
    if request.method == "GET":
        website_list = Website.objects.all().order_by("word")
        serializer = UserProfileSerializer(website_list, many=True)
        return JsonResponse(serializer.data, safe=False)
