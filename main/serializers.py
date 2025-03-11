from .models import library
from rest_framework import serializers

class librarySerializer(serializers.ModelSerializer):
    class Meta:
        model=library
        fields=['uid','title','author','published_date','added_by']

        read_only_fields=['uid','added_by']

    def create(self, validated_data):
        request=self.context.get('request')
        validated_data['added_by']=request.user
        return super().create(validated_data) 