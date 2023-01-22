from rest_framework import serializers
from ...models import Post, Category
from accounts.models import Profile


# class PostSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length = 255)
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    # relative_url = serializers.URLField(source = 'get_absolute_api_url', read_only = True)
    absolute_url = serializers.SerializerMethodField() 
    category = serializers.SlugRelatedField(many = False, slug_field='name',queryset =  Category.objects.all())
    # category = CategorySerializer()
    class Meta:
        model = Post
        # fields = '__all__' 
        fields =   ['author','title','content','image','category','status','absolute_url','created_date','published_date', ]
        read_only_fields = ['author']

    def get_absolute_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.id)
    
    def to_representation(self, instance):
        request = self.context.get('request')
        rep =  super().to_representation(instance)
        rep['state'] = 'list'
        if request.parser_context.get('kwargs').get('pk'):
            rep['state'] = 'single'
            rep.pop('absolute_url', None)
        rep['category'] = CategorySerializer(instance.category, context = {'request':request}).data
        return rep
    
    def create(self, validated_data):
        validated_data['author'] = Profile.objects.get(user__id = self.context.get('request').user.id)
        return super().create(validated_data)
    
