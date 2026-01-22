# n8n Workflow Setup - TRAMIL Crawler

Ce document explique comment configurer le workflow n8n pour crawler les données TRAMIL.

## Vue d'ensemble du workflow

Le workflow n8n automatise :
1. Crawler les pages d'index TRAMIL (A-Z)
2. Extraire les URLs des plantes
3. Télécharger et parser chaque page de monographie
4. Normaliser les données selon `docs/schema.json`
5. Stocker en JSON dans le dossier `data/`
6. Committer automatiquement vers GitHub

## Installation n8n

### Option 1 : Self-hosted (local)
```bash
npm install -g n8n
n8n start
# Accéder à http://localhost:5678
```

### Option 2 : Cloud (n8n.cloud)
- S'inscrire sur https://n8n.cloud
- Créer une nouvelle workflow

## Structure du Workflow

### Node 1: HTTP Request - Fetch Index Page
- **URL** : `https://tramil.net/en/tramilotheque/a` (ou b, c, etc.)
- **Méthode** : GET
- **Headers** : 
  ```
  User-Agent: Mozilla/5.0 (compatible; TRAMIL-Research-Bot/1.0)
  ```

### Node 2: HTML Parse - Extract Plant Links
- **Selector CSS** : `a[href*="/plant/"]`
- **Extraire** : `href`, `textContent`
- **Sortie** : tableau des URLs de plantes

### Node 3: Loop - Process Each Plant
- **Boucle sur** : tableau des URLs
- **Pour chaque URL** : créer un job de téléchargement

### Node 4: HTTP Request - Fetch Plant Page
- **URL dynamique** : construire `https://tramil.net{plant_url}`
- **Méthode** : GET

### Node 5: HTML Parse - Extract Plant Data

Selecteurs CSS pour extraire :
```json
{
  "scientific_name": "h1 ~ p:first-of-type",
  "botanical_family": "a[href*='/famille/']",
  "vernacular_names_en": "[data-language=\"en\"] .vernacular",
  "vernacular_names_fr": "[data-language=\"fr\"] .vernacular",
  "uses": ".uses-section li",
  "preparations": ".preparations-section li",
  "toxicity_warning": ".toxicity-warning",
  "images": "img[src*='img_plant']"
}
```

### Node 6: Transform Data
- Mapper les données extraites vers schema.json
- Générer UUID pour chaque plante
- Structurer en JSON propre
- Ajouter `source`, `date_accessed`

### Node 7: Write to File
- **Chemin** : `data/plants/{slug}.json`
- **Format** : JSON (pretty print)

### Node 8: Git Commit (optionnel)
- Utiliser le nœud "Execute Command" pour :
  ```bash
  git add data/
  git commit -m "[bot] Mettre à jour plantes TRAMIL - $(date)"
  git push origin main
  ```

## Variables d'environnement

Créer un fichier `.env` pour n8n :
```env
# TRAMIL Crawler
TRAMIL_BASE_URL=https://tramil.net/en
TRAMIL_DELAY_MS=2000  # Délai entre les requêtes (respecter les ressources)
OUTPUT_DIR=data

# GitHub (pour commit automatique)
GIT_USER_NAME=tramil-api-bot
GIT_USER_EMAIL=bot@tramil-api.local
GIT_TOKEN=${GITHUB_TOKEN}
```

## Exécution du workflow

### Test manuel
1. Ouvrir n8n
2. Charger le workflow JSON (voir section d'export)
3. Tester avec une seule plante (ex: A)
4. Vérifier le fichier JSON généré dans `data/`

### Execution planifiée
- Configurer un trigger "Schedule" pour lancer :
  - **Chaque nuit** (23h00 UTC) pour un crawl complet
  - **Chaque semaine** pour une mise à jour incrémentale

## Gestion des erreurs

Ajouter des nodes "Catch" pour :
- **404 (page non trouvée)** : logger et continuer
- **Timeout** : retry jusqu'à 3 fois avec délai exponentiel
- **Erreurs de parsing** : sauvegarder le HTML brut pour débug

## Performance

- **Concurrence** : limiter à 2-3 requêtes parallèles pour respecter TRAMIL
- **Caching** : vérifier le hash du HTML pour éviter le re-parsing
- **Compression** : stocker en `.json.gz` pour économiser l'espace

## Export du Workflow

Après configuration, exporter le workflow JSON :
```json
{
  "name": "TRAMIL-Crawler",
  "nodes": [...],
  "connections": {...},
  "active": true,
  "settings": {
    "saveManualExecutions": true,
    "executionTimeout": 300
  }
}
```

Sauvegarder dans `n8n/tramil-crawler.json`

## Troubleshooting

### Les images ne sont pas téléchargées
- Vérifier les URLs absolues vs relatives
- Ajouter `https://tramil.net` au début des URLs relatives

### Données incomplètes
- Inspecter le HTML de TRAMIL avec DevTools
- Mettre à jour les sélecteurs CSS dans Node 5

### Commits Git échouent
- Vérifier le token GitHub avec les permissions `repo`
- Tester la CLI Git localement : `git clone <repo>`

## Prochaines étapes

1. Crawler 50-100 plantes pour MVP
2. Valider schéma JSON
3. Générer fichier agregé `data/plants.json` (toutes les plantes)
4. Télécharger les images en `/assets/images/`
5. Committer vers GitHub

---

**Notes importantes**
- Respecter le robots.txt de TRAMIL : https://tramil.net/robots.txt
- Ajouter un délai entre les requêtes pour ne pas surcharger le serveur
- Toujours attribuer TRAMIL comme source
