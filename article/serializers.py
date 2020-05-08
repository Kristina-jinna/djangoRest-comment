from rest_framework import serializers

from .models import Group

class GroupSerializeer(serializers.Serializer):
    id_vk_group = serializers.IntegerField()
    name_group = serializers.CharField(max_length=200)
    id_User = serializers.CharField()

    def create(self, validated_data):
        return Group.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id_vk_group = validated_data.get('id_vk_group', instance.id_vk_group)
        instance.name_group = validated_data.get('name_group',instance.name_group)
        instance.id_User = validated_data.get('id_User', instance.id_User)
        instance.save()
        return instance