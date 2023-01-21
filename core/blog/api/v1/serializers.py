from rest_framework import serializers
from ...models import Post, Category


# class PostSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length = 255)


class PostSerializer(serializers.ModelSerializer):
    snippet = serializers.CharField(source = 'get_snippet')
    relative_url = serializers.URLField(source = 'get_absolute_api_url', read_only = True)
    class Meta:
        model = Post
        # fields = '__all__' 
        fields =   ['author','title','content','snippet','category','status','relative_url','created_date','published_date',]
        # read_only_fields = ['title']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
