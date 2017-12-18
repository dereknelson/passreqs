from django.http import JsonResponse
from .models import Website, PassReqs
from .serializers import WebsiteSerializer, PassreqsSerializer
from django.core import serializers
from rest_framework import viewsets, generics
from rest_framework.response import Response



class WebsiteViewset(viewsets.ModelViewSet):
    queryset = Website.objects.all().order_by('-created_at')
    serializer_class = WebsiteSerializer

def get_pass_reqs(request):
    if request.method == "GET":
        website_list = Website.objects.all().order_by("-created_at")
        serializer = WebsiteSerializer(website_list, many=True)
        return JsonResponse(serializer.data, safe=False)

class PassReqsView(generics.GenericAPIView):
    # queryset = PassReqs.objects.all().order_by('-created_at')
    serializer_class = PassreqsSerializer

    # def get_pass_reqs(request):
    #     if request.method == "GET":
    #         website = Website.objects.all().order_by("-created_at")
    #         serializer = WebsiteSerializer(website, many=True)
    #         return JsonResponse(serializer.data, safe=False)


    def get(self, request, *args, **kwargs):
        if 'website' in request.GET:
            try:
                website = PassReqs.objects.get(website=request.GET['website'])
                serializer = self.serializer_class(website)
                return Response(serializer.data, status=200)
            except PassReqs.DoesNotExist:
                data = {'error': "there is no database record for this website"}
                return Response(data, status=400)

        else:
            data = {'error': "you need to define a website to get the pass reqs for."}
            return Response(data, status=400)

