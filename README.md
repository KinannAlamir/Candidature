# 🏦 Cadrage Data Science : Prédiction des Moments de Vie

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![LaTeX](https://img.shields.io/badge/LaTeX-Beamer-orange)](https://www.latex-project.org/)

**Mission de cadrage data science** pour la prédiction des moments de vie des clients d'une banque française.

> **Objectif :** Développer une démarche de cadrage structurée sur 6 semaines avec présentation exécutive (6 slides) + POC technique synthétique pour illustration.

## 🎯 Mission de Cadrage | 📊 Présentation | 💻 POC Synthétique

**Contexte :** Sollicitation pour intervenir sur le cadrage d'un cas d'usage data science visant à prédire des moments de vie des clients d'une banque française.

**Questions centrales :**
- Quelle démarche de cadrage mettre en place à l'arrivée chez le client ?
- Quels sont les livrables associés ?
- Comment structurer une mission de 6 semaines ?

**Livrables :**

**Présentation de cadrage** : 6 slides LaTeX/Beamer  
**Démarche méthodologique** : 3 phases structurées  
**POC technique** : Dataset 100% synthétique + prototype ML  

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

### 2. Techniques (Illustrations POC)
✅ **Dataset 100% synthétique** : 10,000 clients fictifs pour démonstration  
✅ **Code d'analyse** : Génération données + baseline ML automatisé  
✅ **Prototype fonctionnel** : Random Forest baseline (F1-score ~70%)  

> **Note :** Le dataset est entièrement généré synthétiquement pour illustrer la faisabilité technique du cadrage, sans utiliser aucune donnée réelle.  

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

## 💻 Dataset Synthétique & POC Technique

> **Important :** Toutes les données sont **100% générées synthétiquement** pour ce POC. Aucune donnée bancaire réelle n'a été utilisée.

### Objectif du Dataset Synthétique
- **Démonstrer la faisabilité** technique des concepts de cadrage
- **Valider les hypothèses** de corrélation comportementale 
- **Servir d'exemple** pour les discussions avec les équipes métier
- **Prototyper rapidement** sans contraintes RGPD/données sensibles

### Caractéristiques Générées

**10,000 clients fictifs** avec **40+ features** réalistes :

- **Démographiques** : âge, genre, situation familiale, CSP, région
- **Financières** : revenus, épargne, crédits en cours  
- **Comportementales** : transactions, connexions app, visites agence
- **Signaux prédictifs** : simulations prêts, consultations produits

### Distribution des 8 Moments de Vie (Synthétiques)

| Moment de Vie | Prévalence | Logique Métier Simulée |
|--------------|------------|------------------------|
| Mariage | ~3% | Pic 25-35 ans, corrélé revenus |
| Naissance | ~4% | Post-mariage, âge 25-40 |
| Achat immobilier | ~5% | Corrélé épargne + revenus stables |
| Changement emploi | ~8% | Plus fréquent, tous âges |
| Retraite | ~2% | Âge 60-70, épargne importante |
| Décès proche | ~3% | Aléatoire, impact patrimonial |
| Divorce | ~2% | Corrélé durée mariage |
| Création entreprise | ~1% | Profils CSP+, épargne |

---

## 💰 ROI et Quick Wins

### Top 3 Use Cases

| Use Case | ROI | Volume/mois |
|----------|-----|-------------|
| 🏠 Achat Immobilier | +25% | 500 clients |
| 🏖️ Retraite | +22% | 200 clients |
| 👶 Naissance | +18% | 400 clients |

**Impact total estimé :** 1,100 clients ciblés/mois → €300-500K revenus additionnels/mois

