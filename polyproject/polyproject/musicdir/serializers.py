from rest_framework.serializers import ModelSerializer

from .models import Musicdir


class MusicdirSerializer(ModelSerializer):
    class Meta:
        model = Musicdir
        fields = ('title', 'content', 'category_id', 'is_published')
