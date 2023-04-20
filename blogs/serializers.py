from rest_framework import serializers

from blogs import models


# class BlogSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(max_length=100)
#     blog = serializers.CharField()
def even_number(value):
    if value % 2 != 0:
        raise serializers.ValidationError('This number cannt be add number')


class BlogSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=100)

    class Meta:
        model = models.Blog
        fields = '__all__'
        # fields = ('id', 'title')
