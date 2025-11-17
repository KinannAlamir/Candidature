# 🏦 Cadrage Data Science : Prédiction des Moments de Vie

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![LaTeX](https://img.shields.io/badge/LaTeX-Beamer-orange)](https://www.latex-project.org/)

**Mission de cadrage data science** pour la prédiction des moments de vie des clients d'une banque française.

> **Objectif principal :** Développer une démarche de cadrage structurée pour un cas d'usage data science, avec livrables méthodologiques et présentation exécutive.

## 📋 Table des Matières

- [Mission de Cadrage](#-mission-de-cadrage)
- [Démarche Méthodologique](#-démarche-méthodologique)
- [Livrables](#-livrables)
- [Présentation Exécutive](#-présentation-exécutive)
- [Implémentation Technique](#-implémentation-technique)
- [Structure du Projet](#structure-du-projet)

---

## 🎯 Mission de Cadrage

**Contexte :** Sollicitation pour intervenir sur le cadrage d'un cas d'usage data science visant à prédire des moments de vie des clients d'une banque française.

**Questions centrales :**
- Quelle démarche de cadrage mettre en place à l'arrivée chez le client ?
- Quels sont les livrables associés ?
- Comment structurer une mission de 6 semaines ?

### 8 Moments de Vie Identifiés

1. 💍 **Mariage / PACS** - Opportunité produits épargne couple
2. 👶 **Naissance / Adoption** - Assurance vie, épargne enfant  
3. 🏠 **Achat immobilier** - Crédit immobilier, assurance habitation
4. 💼 **Changement d'emploi** - Négociation salaire, mobilité bancaire
5. 🏖️ **Retraite** - Produits retraite, défiscalisation
6. 💐 **Décès d'un proche** - Succession, réorganisation patrimoine
7. 💔 **Divorce / Séparation** - Réorganisation comptes, crédit
8. 🚀 **Création d'entreprise** - Compte pro, crédit professionnel

**Enjeu métier :** Anticiper ces moments pour proposer des offres personnalisées au bon moment, augmentant la satisfaction client et les revenus.

---

## 🗺️ Démarche Méthodologique

### Phase 1: Compréhension Métier (S1-S2)
**Objectif :** Comprendre les enjeux business et cartographier l'existant

**Activités :**
- **Ateliers métier** avec équipes Marketing, Retail Banking, Crédits
- **Audit données** (CRM, transactions, comportements digitaux)
- **Identification des 8 moments de vie** prioritaires selon ROI potentiel
- **Définition des KPIs** de succès et métriques métier

**Livrables :**
- Cartographie des sources de données
- Matrice d'impact/faisabilité des 8 moments de vie
- Définition des cas d'usage prioritaires

### Phase 2: Structuration Technique (S3-S4)
**Objectif :** Concevoir l'architecture et la méthodologie

**Activités :**
- **Architecture technique** (ingestion, feature store, ML, API)
- **Feature engineering** (100+ variables comportementales)
- **Sélection algorithmes** ML adaptés aux cas d'usage
- **Roadmap de déploiement** sur 12 mois

**Livrables :**
- Architecture technique détaillée
- Spécifications fonctionnelles ML
- Planning de déploiement par moments de vie

### Phase 3: POC & Validation (S5-S6)
**Objectif :** Valider la faisabilité avec un prototype

**Activités :**
- **POC** sur 1-2 moments de vie (Immobilier + Naissance)
- **Tests et validation** des modèles sur données historiques
- **Dashboard de monitoring** des performances
- **Présentation aux sponsors** et recommandations

**Livrables :**
- Prototype fonctionnel
- Résultats de validation (métriques business)
- Recommandations de déploiement

---

## 📋 Livrables

### 1. Méthodologiques
✅ **Démarche de cadrage structurée** (3 phases / 6 semaines)  
✅ **Analyse des enjeux métier** et cartographie use cases  
✅ **Architecture technique** et roadmap de déploiement  

### 2. Techniques (Illustrations)
✅ **Dataset synthétique** réaliste (10,000 clients, 40+ features)  
✅ **Code d'analyse** (génération données + baseline ML)  
✅ **Prototype de modèle** (Random Forest, F1-score ~70%)  

### 3. Exécutifs
✅ **Présentation de cadrage** (6 slides LaTeX/Beamer)  
✅ **Hypothèses de travail** documentées  
✅ **ROI estimé** et plan de déploiement  

### 4. ROI et Quick Wins

| Use Case | ROI Estimé | Volume/mois | Impact €/mois |
|----------|------------|-------------|---------------|
| 🏠 Achat Immobilier | +25% | 500 clients | €150-200K |
| 🏖️ Retraite | +22% | 200 clients | €80-120K |
| 👶 Naissance | +18% | 400 clients | €70-100K |

**Impact total :** 1,100 clients ciblés/mois → **€300-420K** revenus additionnels/mois

---

## � Présentation Exécutive

**Format :** 6 slides LaTeX/Beamer (selon cahier des charges)

### Contenu des Slides

1. **🎯 Démarche de cadrage** - Vue d'ensemble (3 phases, 6 semaines)
2. **🔍 Phase 1** - Compréhension métier (ateliers, audit données)
3. **💡 Moments de vie** - 8 événements identifiés + hypothèses métier
4. **🏗️ Architecture** - Design technique + roadmap 12 mois
5. **📦 Livrables** - 5 catégories + quick wins
6. **💰 ROI** - Top 3 use cases (ROI 18-25%)

**Hypothèses de travail intégrées :**
- Corrélations comportementales fortes 2-6 mois avant événements
- Données CRM + transactionnelles suffisantes pour prédiction
- Acceptabilité client pour offres anticipées personnalisées
- Capacité d'absorption métier pour déploiement graduel

Pour compiler la présentation :
```bash
make presentation
# ou
cd presentation && pdflatex presentation_cadrage.tex
```

---

## 💻 Implémentation Technique

> **Note importante :** L'implémentation technique ci-dessous sert d'**illustration concrète** des concepts de cadrage. L'objectif principal reste le cadrage méthodologique, pas le développement technique.

### Démarrage Rapide

```bash
# Cloner le repository
git clone https://github.com/KinannAlamir/Candidature.git
cd case_study_banque

# Exécuter le prototype complet
make all
```

**Durée d'exécution : ~2 minutes**

### Étapes Détaillées

```bash
# Installer les dépendances Python
make setup

# Générer le dataset synthétique (10,000 clients)
make generate

# Exécuter l'analyse exploratoire + ML
make analyze

# Compiler la présentation (si LaTeX installé)
make presentation
```

### Résultats du Prototype

| Métrique | Valeur | 
|----------|--------|
| **Algorithme** | Random Forest (baseline) |
| **Précision** | 70-75% |
| **Recall** | 60-65% |
| **F1-Score** | 65-70% |
| **Clients testés** | 10,000 (données synthétiques) |

**Top 5 Features Prédictives :**
1. `simulation_pret_immobilier` (15%)
2. `age` (12%)  
3. `epargne_totale` (10%)
4. `augmentation_epargne_recente` (8%)
5. `revenu_mensuel` (7%)

---

## 📁 Structure du Projet

```
case_study_banque/
├── README.md                     # Documentation (focus cadrage)
├── Makefile                      # Automatisation prototype
├── presentation/
│   ├── presentation_cadrage.tex # Source LaTeX (6 slides)
│   └── presentation_cadrage.pdf # Présentation exécutive
├── code/                         # Illustration technique
│   ├── generate_dataset.py      # Génération dataset synthétique
│   ├── analyse_exploratoire.py  # Prototype ML baseline
│   └── requirements.txt         # Dépendances Python
└── data/                         # Données d'illustration
    ├── clients_data.csv         # 10,000 clients synthétiques
    ├── life_events.csv          # Événements générés
    ├── feature_importance.csv   # Résultats ML
    └── analyse_exploratoire.png # Visualisations
```

**Organisation par priorité :**
1. **`presentation/`** - Cœur du livrable (cadrage + hypothèses)
2. **`README.md`** - Démarche méthodologique détaillée  
3. **`code/` + `data/`** - Illustrations techniques du cadrage

---

## � Dataset Synthétique (Illustration)

### Caractéristiques Générées

**10,000 clients** avec **40+ features** réalistes :

- **Démographiques** : âge, genre, situation familiale, CSP, région
- **Financières** : revenus, épargne, crédits en cours  
- **Comportementales** : transactions, connexions app, visites agence
- **Signaux prédictifs** : simulations prêts, consultations produits

### Distribution des 8 Moments de Vie

| Moment de Vie | Prévalence | Logique Métier |
|--------------|------------|----------------|
| Mariage | ~3% | Pic 25-35 ans, corrélé revenus |
| Naissance | ~4% | Post-mariage, âge 25-40 |
| Achat immobilier | ~5% | Corrélé épargne + revenus stables |
| Changement emploi | ~8% | Plus fréquent, tous âges |
| Retraite | ~2% | Âge 60-70, épargne importante |
| Décès proche | ~3% | Aléatoire, impact patrimonial |
| Divorce | ~2% | Corrélé durée mariage |
| Création entreprise | ~1% | Profils CSP+, épargne |

---

## � Présentation

Le dossier `presentation/` contient une présentation LaTeX/Beamer de 6 slides :

1. **Démarche de cadrage** - Vue d'ensemble (3 phases, 6 semaines)
2. **Phase 1** - Compréhension métier (ateliers, audit données)
3. **Moments de vie** - 8 événements identifiés + hypothèses
4. **Architecture** - Design technique + roadmap 12 mois
5. **Livrables** - 5 catégories + quick wins
6. **ROI** - Top 3 use cases (ROI 18-25%)

Pour compiler :

```bash
make presentation
# ou
cd presentation && pdflatex presentation_cadrage.tex
```

---

## 🎯 Démarche de Cadrage (6 Semaines)

### Phase 1: Compréhension (S1-S2)
- Ateliers métier (Marketing, Retail, Crédits)
- Audit données (CRM, transactions, comportements)
- Identification 8 moments de vie prioritaires
- Définition KPIs

### Phase 2: Structuration (S3-S4)
- Architecture technique (5 couches)
- Feature engineering (100+ features)
- Sélection algorithmes ML
- Roadmap déploiement 12 mois

### Phase 3: POC & Validation (S5-S6)
- POC sur 1-2 moments de vie
- Tests et validation modèles
- Dashboard monitoring
- Présentation sponsors

---

## 💰 ROI et Quick Wins

### Top 3 Use Cases

| Use Case | ROI | Volume/mois |
|----------|-----|-------------|
| 🏠 Achat Immobilier | +25% | 500 clients |
| 🏖️ Retraite | +22% | 200 clients |
| 👶 Naissance | +18% | 400 clients |

**Impact total estimé :** 1,100 clients ciblés/mois → €300-500K revenus additionnels/mois

---

## �️ Technologies

- **Python 3.8+** : pandas, numpy, scikit-learn, matplotlib
- **LaTeX/Beamer** : Présentation professionnelle
- **Makefile** : Automatisation des tâches

---

## 📄 License

MIT License - Projet éducatif et de démonstration.

**Note :** Les données sont entièrement synthétiques.

---

## ✨ Auteur

Cas d'étude créé pour une mission de cadrage data science - Novembre 2025

---

**� Prêt à commencer ?** `make all`
