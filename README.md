# 🏦 Prédiction des Moments de Vie - Data Science Case Study

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebooks-orange)](https://jupyter.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Projet de data science pour prédire les moments de vie des clients bancaires et personnaliser les offres commerciales.

## 📊 Notebooks

### 1️⃣ Génération des Données (`1_generation_donnees.ipynb`)
- Génération de 10,000 clients synthétiques
- 8 moments de vie avec probabilités réalistes
- Signaux comportementaux faibles
- **Output :** `clients_data.csv`, `life_events.csv`

### 2️⃣ Analyse Exploratoire (`2_analyse_exploratoire.ipynb`)
- Statistiques descriptives et corrélations
- Visualisations multiples
- Modèle baseline Random Forest
- **Output :** Feature importance, visualisations

### 3️⃣ Résultats Concrets (`3_resultats_concrets.ipynb`)
- Modèles pour tous les moments de vie
- Scores de propension par client
- Segmentation (Faible/Moyen/Élevé)
- Top 100 clients par événement
- Recommandations business
- **Output :** ~15 fichiers CSV + rapport consolidé

---

## 💡 8 Moments de Vie Prédits

💍 **Mariage** • 👶 **Naissance** • 🏠 **Achat immobilier** • 💼 **Changement emploi**  
🏖️ **Retraite** • 💐 **Décès proche** • 💔 **Divorce** • 🚀 **Création entreprise**

---

## 🎯 Résultats Attendus

Après exécution complète des notebooks :

### Données Générées
- `clients_data.csv` - 10,000 clients avec 25+ features
- `life_events.csv` - ~2,000 événements de vie

### Résultats d'Analyse
- Feature importance
- Visualisations exploratoires
- Performance modèle baseline (AUC ~0.75-0.85)

### Outputs Business
- Scores de propension pour tous les clients
- Segmentation par moment de vie
- Top 100 clients prioritaires par événement
- Recommandations d'actions commerciales
- Rapport consolidé

**Total : ~20 fichiers exploitables**

---

## 📚 Documentation

- **`docs/HYPOTHESES_ET_METHODOLOGIE.md`** - Approche détaillée
- **`docs/LIVRABLES.md`** - Liste complète des livrables
- **`INSTRUCTIONS.md`** - Contexte du case study

---

## ⚠️ Note Importante

> Les données sont **100% synthétiques** et générées pour démonstration. Aucune donnée bancaire réelle n'est utilisée.

---

