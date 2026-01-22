# Contribuer à TRAMIL-API

## Déclaration de mission

Ce projet vise à **contribuer à la recherche ethnopharmacologique** en structurant les données de la TRAMILothèque dans une base de données accessible par API.

Tous les contributeurs acceptent :
- **Respecter les droits de propriété intellectuelle de TRAMIL**
- **Attribuer correctement toutes les données à la source TRAMIL**
- **Suivre les guide-lines scientifiques du projet**

## 🙅 Code de conduite

Tous les contributeurs doivent maintenir un environnement accueillant et respectueux :
- Pas de discrimination ou harcèlement
- Communication respectueuse et constructive
- Respect des délais et des standards de qualité

## 🔃 Processus de contribution

### 1. Avant de commencer

Assurez-vous que :
- Vous avez lu ce fichier et le README
- Vous comprenez les conditions légales (voir mentions légales du site TRAMIL)
- Votre contribution respecte la structure existante

### 2. Branches et commits

**Nommage des branches :**
```
feature/nom-fonctionnalite
bugfix/numero-issue
docs/sujet-documentation
```

**Messages de commit (en français) :**
```
[type] Courte description

Description plus détaillée si nécessaire.

Types autorisés:
- feat: nouvelle fonctionnalité
- fix: correction de bug
- docs: documentation
- test: tests unitaires
- refactor: refactorisation
```

### 3. Schéma de données

Toute contribution modifiant le schéma doit :
- Mettre à jour `docs/schema.json`
- Ajouter des migration Alembic
- Inclure des tests

### 4. Tests

```bash
# Exécuter les tests
pytest tests/

# Vérifier la couverture
pytest --cov=app tests/
```

Toute nouvelle fonctionnalité doit avoir une couverture >= 80%.

### 5. Pull Requests

**Template pour les PRs :**

```markdown
## Déscription
Décrire le changement proposé.

## Type de changement
- [ ] Nouvelle fonctionnalité
- [ ] Correction de bug
- [ ] Changement de documentation
- [ ] Changement du schéma

## Tests effectués
Décrire les tests réalisés.

## Attribution TRAMIL
- [ ] Les sources TRAMIL sont correctement attribuées
- [ ] Les données respectent le schéma

## Checklist
- [ ] Code testé localement
- [ ] Aucun conflit de merge
- [ ] README mis à jour si nécessaire
- [ ] Commits avec messages clair
```

## 🛠️ Outils et configuration

### Setup de développement

```bash
# Cloner le repo
git clone https://github.com/GuillaumeBld/tramil-api.git
cd tramil-api

# Créer l'environnement virtuel
python -m venv venv
source venv/bin/activate

# Installer les dépendances
pip install -r requirements.txt

# Installer les dépendances de développement
pip install pytest pytest-asyncio black flake8
```

### Linting et formatting

```bash
# Black (formattage)
black app/ tests/

# Flake8 (linting)
flake8 app/ tests/
```

## 📋 Domaines de contribution

### Parser/Scraper
- Ajouter support pour d'autres champs TRAMIL
- Amliorier la robustesse du parsing HTML
- Gérer les cas limites

### API
- Ajouter de nouveaux endpoints
- Implémenter des filtres avancés
- Ajouter support GraphQL

### Data
- Normalisation des données
- Nettoyage et validation
- Enrichissement avec des références

### Documentation
- API documentation
- Examples d'utilisation
- Guides pour les chercheurs

## 🐛 Signaler un bug

Créez une issue GitHub avec :
- Titre clair et concis
- Description détaillée
- Étapes de reproduction
- Screenshots si pertinent
- Environnement (OS, Python version, etc.)

## 💬 Questions?

- Ouvrez une discussion sur GitHub
- Contactez l'auteur via GitHub
- Consultez la documentation du projet

---

**Merci de contribuer à TRAMIL-API!** 🎉
