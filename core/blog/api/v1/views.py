from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostSerializer
from ...models import Post
from rest_framework import status
from django.shortcuts import get_object_or_404

@api_view()
def postDetail(request, id):
    # try:
    #     post = Post.objects.get(pk = id)
    #     serializer =  PostSerializer(post)
    #     data = serializer.data
    #     return Response(data)
    # except Post.DoesNotExist:
    #     return Response ({'detail':'Post does not exist!'}, status= status.HTTP_404_NOT_FOUND)
    post = get_object_or_404(Post ,pk = id)
    serializer =  PostSerializer(post)
    data = serializer.data
    return Response(data)
