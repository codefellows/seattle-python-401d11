from rest_framework import serializers
from sweets_app.models import Sweet

class SweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sweet
        fields = ('name','rating')
