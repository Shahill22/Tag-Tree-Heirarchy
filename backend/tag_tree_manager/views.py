from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import TreeNode
from .serializers import TreeNodeSerializer
from django.db import transaction

class TreeNodeViewSet(ModelViewSet):
    queryset = TreeNode.objects.filter(parent__isnull=True)
    serializer_class = TreeNodeSerializer

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        """
        Custom POST method to save a new tree hierarchy.
        """
        tree_data = request.data
        root_node = self.save_tree(tree_data)
        return Response(TreeNodeSerializer(root_node).data)

    def save_tree(self, data, parent=None):
        node = TreeNode.objects.create(
            name=data['name'],
            parent=parent,
            data=data.get('data', {})
        )
        children = data.get('children', [])
        for child in children:
            self.save_tree(child, parent=node)
        return node

    @action(detail=False, methods=['get'])
    def get_all_trees(self, request):
        """
        GET endpoint to fetch all trees with their nested structure.
        """
        trees = TreeNode.objects.filter(parent__isnull=True)
        serializer = TreeNodeSerializer(trees, many=True)
        return Response(serializer.data)

    @transaction.atomic
    def update(self, request, *args, **kwargs):
        """
        PUT method to update an existing tree hierarchy.
        """
        instance = self.get_object()
        instance.children.all().delete()  # Remove existing children
        instance.name = request.data['name']
        instance.data = request.data.get('data', {})
        instance.save()
        children = request.data.get('children', [])
        for child_data in children:
            self.save_tree(child_data, parent=instance)
        return Response(TreeNodeSerializer(instance).data)

