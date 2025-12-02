from rest_framework.viewsets import ModelViewSet

from core.establishment.models import Ingredient
from core.establishment.serializers import IngredientSerializer
from rest_framework.filters import SearchFilter

class IngredientViewSet(ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name']
    http_method_names = ['get', 'post', 'put', 'delete']