from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostSerializer
from ...models import Post

@api_view()
def postDetail(request, id):
    post = Post.objects.get(pk = id)
    serializer =  PostSerializer(post)
    data = serializer.data
    return Response(data)