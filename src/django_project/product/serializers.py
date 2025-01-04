from rest_framework import serializers

class CreateProductResponseSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField()
    description = serializers.CharField()
    stock = serializers.IntegerField()
    active = serializers.BooleanField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()

class CreateProductRequestSerializer(serializers.Serializer):
    name = serializers.CharField()
    description = serializers.CharField()
    stock = serializers.IntegerField()
    active = serializers.BooleanField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2)


class ListOutputMetaSerializer(serializers.Serializer):
    current_page = serializers.IntegerField()
    per_page = serializers.IntegerField()
    total = serializers.IntegerField()

class ListProductResponseSerializer(serializers.Serializer):
    meta = ListOutputMetaSerializer()
    data = CreateProductResponseSerializer(many=True)