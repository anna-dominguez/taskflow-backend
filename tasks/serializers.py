from rest_framework import serializers
from .models import Category, Task


class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer pour le modèle Category.
    """
    tasks_count = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'name', 'tasks_count']
        read_only_fields = ['id']

    def get_tasks_count(self, obj):
        """Retourne le nombre de tâches dans cette catégorie."""
        return obj.tasks.count()

    def validate_name(self, value):
        """Valide que le nom de la catégorie est unique."""
        if not value or not value.strip():
            raise serializers.ValidationError("Le nom de la catégorie ne peut pas être vide.")

        # Vérification de l'unicité lors de la création
        if not self.instance and Category.objects.filter(name=value).exists():
            raise serializers.ValidationError("Une catégorie avec ce nom existe déjà.")

        # Vérification de l'unicité lors de la mise à jour
        if self.instance and Category.objects.exclude(pk=self.instance.pk).filter(name=value).exists():
            raise serializers.ValidationError("Une catégorie avec ce nom existe déjà.")

        return value.strip()


class TaskSerializer(serializers.ModelSerializer):
    """
    Serializer pour le modèle Task.
    """
    category_name = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = Task
        fields = ['id', 'description', 'is_completed', 'created_at', 'category', 'category_name']
        read_only_fields = ['id', 'created_at']

    def validate_description(self, value):
        """Valide que la description n'est pas vide."""
        if not value or not value.strip():
            raise serializers.ValidationError("La description ne peut pas être vide.")
        return value.strip()

    def validate_category(self, value):
        """Valide que la catégorie existe."""
        if not value:
            raise serializers.ValidationError("Une catégorie doit être spécifiée.")
        return value
