from rest_framework import serializers
from ...models import Post, Category


# class PostSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length = 255)


class PostSerializer(serializers.ModelSerializer):
    # relative_url = serializers.URLField(source = 'get_absolute_api_url', read_only = True)
    absolute_url = serializers.SerializerMethodField() 
    class Meta:
        model = Post
        # fields = '__all__' 
        fields =   ['author','title','content','category','status','absolute_url','created_date','published_date', ]
        # read_only_fields = ['title']

    def get_absolute_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri()


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
