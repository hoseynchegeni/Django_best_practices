from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostSerializer
from ...models import Post
from rest_framework import status
from django.shortcuts import get_object_or_404

@api_view(['GET', 'POST'])
def PostList(request):
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


@api_view(['GET','PUT','DELETE'])
def postDetail(request, id):
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

