from rest_framework.viewsets import ModelViewSet

from core.establishment.models import Ingredient
from core.establishment.serializers import IngredientSerializer

class IngredientViewSet(ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    http_method_names = ['get', 'post', 'put', 'delete']