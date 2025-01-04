from rest_framework import serializers
from .models import TreeNode

class TreeNodeSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    class Meta:
        model = TreeNode
        fields = ['id', 'name', 'data', 'children']

    def get_children(self, obj):
        children = obj.children.all()
        return TreeNodeSerializer(children, many=True).data
