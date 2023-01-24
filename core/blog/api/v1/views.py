from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.response import Response
from .serializers import PostSerializer, CategorySerializer
from ...models import Post, Category
from rest_framework import status, mixins, viewsets 
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, ListAPIView, CreateAPIView,RetrieveUpdateDestroyAPIView
from .permissions import IsAuthorOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from . pagination import LargeResultSetPagination

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

class PostList(ListAPIView, CreateAPIView):
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



class PostDetailOld(APIView):
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
    
class PostDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status = True)
    lookup_field = 'id' # Or path('post/<int:pk>/', PostDetail.as_view(), name= 'post_detail'),


    

class PostViewSetOld(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status = True)
    # lookup_field = 'id'

    def list(self, request):
        serializer = self.serializer_class(self.queryset, many = True)
        return Response(serializer.data)

    def retrieve(self, request, pk = None):
        PostObj = get_object_or_404(self.queryset, pk = pk)
        serializer = self.serializer_class(PostObj)
        return Response(serializer.data)
        
    def create(self, request): 
        serializer = self.serializer_class(data = request.data)
        serializer.is_valid(raise_exception= True)
        serializer.save()
        return Response(serializer.data)

    def put(self, request, pk):
        post = get_object_or_404(Post ,pk = pk)
        serializer = self.serializer_class(post, data= request.data)
        serializer.is_valid(raise_exception= True)
        serializer.save()
        return Response(serializer.data)


    def destroy(self, request, pk):
        post = get_object_or_404(Post ,pk = pk)
        post.delete()
        return Response({'detail':'Item removed successfully'})
    

class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status = True)
    filter_backends = [DjangoFilterBackend,SearchFilter, OrderingFilter]
    filterset_fields = {'category':['exact','in'], 'author':['exact'],'status':['exact'],'published_date':['lt','gt']}
    search_fields = ['title','content']
    ordering_fields = ['published_date']
    pagination_class =  LargeResultSetPagination

    @action(methods=['get'], detail= False)
    def get_ok(self, request):
        return Response({'detail':'ok'})

class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


