from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet, ModelViewSet

from blogs import models, serializers, services


# Create your views here.

def index(request, blog_id):
    blog = models.Blog.objects.get(id=blog_id)
    blog_titles = {
        'id': blog.id,
        'title': blog.title,
    }
    return JsonResponse(blog_titles, safe=False)


@api_view(['GET'])
def get_blog(request,*args ,**kwargs):
    # blogs = models.Blog.objects.all()
    # blogs = models.Blog.objects.filter(id__gt=1)
    # blog = models.Blog.objects.get(id=bid)
    blog = get_object_or_404(models.Blog.objects.all(), **kwargs)
    # serializer = serializers.BlogSerializer(blogs, many=True)
    serializer = serializers.BlogSerializer(blog)
    # serializer.is_valid(raise_exception=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_blogs(request):
    blogs = models.Blog.objects.all()
    serializer = serializers.BlogSerializer(blogs, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_blog(request):
    serializer = serializers.BlogSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    blog = models.Blog.objects.create(**serializer.validated_data)

    return Response(serializers.BlogSerializer(blog).data, status=status.HTTP_201_CREATED)


class BlogView(ViewSet):

    def list(self, request, *args, **kwargs):
        blogs = models.Blog.objects.all()
        serializer = serializers.BlogSerializer(blogs, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        blog = get_object_or_404(models.Blog.objects.all(), pk=pk)
        serializer = serializers.BlogSerializer(blog)

        return Response(serializer.data)


class BlogViewSet(ModelViewSet):
    blog_services: services.BlogServicesInterface = services.BlogServicesV1()
    # queryset = models.Blog.objects.all()
    serializer_class = serializers.BlogSerializer

    def get_queryset(self):
        return self.blog_services.get_blogs()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        print(serializer.validated_data)

        self.blog_services.create_blog(data=serializer.validated_data)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


    def list(self, request, *args, **kwargs):
        queryset = self.blog_services.get_blogs()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
