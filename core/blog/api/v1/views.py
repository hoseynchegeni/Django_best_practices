from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import PostSerializer
from ...models import Post
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework import mixins

api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def PostListFunctionBase(request):
    if request.method == 'GET':
        # posts = Post.objects.all()
        posts = Post.objects.filter(status  = True)
        serializer = PostSerializer(posts, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PostSerializer(data = request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data)
        # else:
        #     return Response(serializer.errors)
        serializer.is_valid(raise_exception= True)
        serializer.save()
        return Response(serializer.data)


class PostListApiView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    def get(self, request):
        posts = Post.objects.filter(status  = True)
        serializer = PostSerializer(posts, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostSerializer(data = request.data)
        serializer.is_valid(raise_exception= True)
        serializer.save()
        return Response(serializer.data)

class PostList(GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status = True)

    def get(self, request, *args, **kwargs):
        return self.list (request,*args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request,*args, **kwargs)

@api_view(['GET','PUT','DELETE'])
@permission_classes([IsAuthenticatedOrReadOnly])
def postDetailFunctionBase(request, id):
    # try:
    #     post = Post.objects.get(pk = id)
    #     serializer =  PostSerializer(post)
    #     data = serializer.data
    #     return Response(data)
    # except Post.DoesNotExist:
    #     return Response ({'detail':'Post does not exist!'}, status= status.HTTP_404_NOT_FOUND)
    post = get_object_or_404(Post ,pk = id)
    if request.method == 'GET':
        serializer =  PostSerializer(post)
        data = serializer.data
        return Response(data)
    elif request.method == 'PUT':
        serializer = PostSerializer(post, data= request.data)
        serializer.is_valid(raise_exception= True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        post.delete()
        return Response({'detail':'Item removed successfully'})



class PostDetail(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer

    def get(self, request, id):
        post = get_object_or_404(Post ,pk = id, status = True)  
        serializer =  self.serializer_class(post)
        data = serializer.data
        return Response(data)

    def put(self, request, id):
        post = get_object_or_404(Post ,pk = id)
        serializer = self.serializer_class(post, data= request.data)
        serializer.is_valid(raise_exception= True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, id):
        post = get_object_or_404(Post ,pk = id)
        post.delete()
        return Response({'detail':'Item removed successfully'})