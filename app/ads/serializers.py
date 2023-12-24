from rest_framework import serializers

from .models import Ad, Comment


class CommentSerializer(serializers.ModelSerializer):
    """ Сериализатор отзыва. """

    class Meta:
        model = Comment
        fields = '__all__'


class AdSerializer(serializers.ModelSerializer):
    """ Сериализатор объявления. """

    class Meta:
        model = Ad
        fields = '__all__'


class AdDetailSerializer(serializers.ModelSerializer):
    """ Сериализатор просмотра одного объявления. """

    class Meta:
        model = Ad
        fields = '__all__'
