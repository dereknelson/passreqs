from django.http import JsonResponse
from .models import Website, PassReqs
from .serializers import WebsiteSerializer, PassreqsSerializer
from django.core import serializers
from rest_framework import viewsets


class WebsiteViewset(viewsets.ModelViewSet):
    queryset = Website.objects.all().order_by('-created_at')
    serializer_class = WebsiteSerializer

def get_pass_reqs(request):
    if request.method == "GET":
        website_list = Website.objects.all().order_by("-created_at")
        serializer = WebsiteSerializer(website_list, many=True)
        return JsonResponse(serializer.data, safe=False)

class PassReqsViewset(viewsets.ModelViewSet):
    queryset = PassReqs.objects.all().order_by('-created_at')
    serializer_class = PassreqsSerializer