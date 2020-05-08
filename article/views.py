from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404

from .models import UserAuthor,Group,Post
from .serializers import GroupSerializeer

class GroupView(APIView):
    def get(self,request):
        groups = Group.objects.all()
        serialize = GroupSerializeer(groups, many=True)
        return Response({'groups':serialize.data})


    def post(self,request):
        group = request.data.get('group')

        serialize = GroupSerializeer(data=group)
        if serialize.is_valid(raise_exception=True):
            group_saved = serialize.save()
        return Response({"success": "Group '{}' create successfully".format(group_saved.name_group)})

    def put(self,request,pk):
        save_group = get_object_or_404(Group.objects.all(), pk=pk)
        data = request.data.get('group')
        serializer = GroupSerializeer(instance=save_group, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            group_saved = serializer.save()

        return Response({"success": "Group '{}' updated successfully".format(group_saved.name_group)})

    def delete(self,request,pk):
        group = get_object_or_404(Group.objects.all(), pk=pk)
        group.delete()
        return Response({"message": "Group '{}' has been deleted".format(pk)},status=204)
