from django.db import models

class Category(models.Model):
    """
    Modèle représentant une catégorie de tâches.
    """
    name = models.CharField(
        max_length=100,
        unique=True,
        help_text="Nom unique de la catégorie"
    )

    class Meta:
        verbose_name = "Catégorie"
        verbose_name_plural = "Catégories"
        ordering = ['name']

    def __str__(self):
        return self.name


class Task(models.Model):
    """
    Modèle représentant une tâche.
    """
    description = models.TextField(
        help_text="Description de la tâche"
    )
    is_completed = models.BooleanField(
        default=False,
        help_text="Indique si la tâche est terminée"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Date de création de la tâche"
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='tasks',
        help_text="Catégorie associée à la tâche"
    )

    class Meta:
        verbose_name = "Tâche"
        verbose_name_plural = "Tâches"
        ordering = ['-created_at']

    def __str__(self):
        status = "✓" if self.is_completed else "○"
        return f"{status} {self.description[:50]}"
