from rest_framework import serializers
from .models import Note

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = (
            'title',
            'due_date',
            'label',
            'links',
        )