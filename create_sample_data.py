"""
Script pour créer des données de test pour l'application Todo List.

Usage:
    python3 manage.py shell < create_sample_data.py
"""

from tasks.models import Category, Task

print("🚀 Création de données de test...\n")

# Nettoyage des données existantes
print("📦 Nettoyage des données existantes...")
Task.objects.all().delete()
Category.objects.all().delete()
print("✅ Données nettoyées\n")

# Création des catégories
print("📁 Création des catégories...")
categories_data = [
    "Travail",
    "Personnel",
    "Courses",
    "Sport",
    "Études",
]

categories = []
for cat_name in categories_data:
    cat = Category.objects.create(name=cat_name)
    categories.append(cat)
    print(f"   ✓ Catégorie créée : {cat.name}")

print(f"\n✅ {len(categories)} catégories créées\n")

# Création des tâches
print("✅ Création des tâches...")
tasks_data = [
    {"description": "Finir le projet Django", "category": categories[0], "is_completed": False},
    {"description": "Préparer la présentation", "category": categories[0], "is_completed": False},
    {"description": "Réviser le code React", "category": categories[0], "is_completed": True},
    {"description": "Faire les courses pour la semaine", "category": categories[2], "is_completed": False},
    {"description": "Acheter du lait", "category": categories[2], "is_completed": True},
    {"description": "Aller à la salle de sport", "category": categories[3], "is_completed": False},
    {"description": "Courir 5km", "category": categories[3], "is_completed": True},
    {"description": "Lire le chapitre 5", "category": categories[4], "is_completed": False},
    {"description": "Faire les exercices de maths", "category": categories[4], "is_completed": False},
    {"description": "Appeler maman", "category": categories[1], "is_completed": False},
    {"description": "Payer les factures", "category": categories[1], "is_completed": True},
    {"description": "Nettoyer la maison", "category": categories[1], "is_completed": False},
]

tasks = []
for task_data in tasks_data:
    task = Task.objects.create(**task_data)
    tasks.append(task)
    status = "✓" if task.is_completed else "○"
    print(f"   {status} Tâche créée : {task.description[:50]}... [{task.category.name}]")

print(f"\n✅ {len(tasks)} tâches créées\n")

# Résumé
print("=" * 60)
print("📊 RÉSUMÉ DES DONNÉES DE TEST")
print("=" * 60)
print(f"Catégories totales : {Category.objects.count()}")
print(f"Tâches totales : {Task.objects.count()}")
print(f"Tâches terminées : {Task.objects.filter(is_completed=True).count()}")
print(f"Tâches en cours : {Task.objects.filter(is_completed=False).count()}")

print("\n📈 Distribution des tâches par catégorie :")
for cat in categories:
    count = cat.tasks.count()
    completed = cat.tasks.filter(is_completed=True).count()
    print(f"   • {cat.name}: {count} tâche(s) ({completed} terminée(s))")

print("\n✨ Données de test créées avec succès !")
print("\n🔗 Testez l'application :")
print("   Backend : http://localhost:8000/api/")
print("   Frontend : http://localhost:3000")
