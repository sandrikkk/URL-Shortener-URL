from django.http import Http404
from django.shortcuts import redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Link
from .serializers import LinkSerializer
from rest_framework import permissions



# Create your views here.
class ShortenerUrlApiView(APIView):
    def get(self, request, *args, **kwargs):
        queryset = Link.objects.all()
        serializer = LinkSerializer(queryset, many=True)

        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        data = request.data

        serializer = LinkSerializer(data=data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)


class PremiumShortenerUrlApiView(APIView):


    def post(self, request):
        serializer = LinkSerializer(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)


class RetrieveUrlApiView(APIView):

    def get_object(self, pk):
        try:
            return Link.objects.all().filter(pk=pk).first()
        except Exception:
            raise Http404

    def get(self, request, pk=None):
        url = self.get_object(pk=pk)
        if url:
            url.count += 1
            url.save()
            serializer = LinkSerializer(url)
            return Response(serializer.data)
        return Response({'error': 'Object not found!'})

    def delete(self, request, pk=None):
        url = self.get_object(pk=pk)
        url.delete()

        return Response({'Object deleted!'})
        
class Redirector(APIView):
    def get(self, request, shortener_link= None, *args, **kwargs):
        redirect_link = Link.objects.filter(shortened_link__contains = shortener_link).first()
        redirect_link.count += 1
        redirect_link.save()
        return redirect(redirect_link.original_link)

