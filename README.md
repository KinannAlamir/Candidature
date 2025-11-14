# 🏦 Prédiction des Moments de Vie - Cas d'Étude Data Science

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![LaTeX](https://img.shields.io/badge/LaTeX-Beamer-orange)](https://www.latex-project.org/)

Cas d'étude complet de cadrage data science pour la prédiction des moments de vie des clients d'une banque française.

## 📋 Table des Matières

- [Vue d'Ensemble](#vue-densemble)
- [Démarrage Rapide](#démarrage-rapide)
- [Structure du Projet](#structure-du-projet)
- [Dataset](#dataset)
- [Résultats](#résultats)
- [Présentation](#présentation)

---

## 🎯 Vue d'Ensemble

Ce projet propose une **démarche de cadrage structurée sur 6 semaines** pour prédire 8 moments de vie clés des clients bancaires :

1. 💍 Mariage / PACS
2. 👶 Naissance / Adoption  
3. 🏠 Achat immobilier
4. 💼 Changement d'emploi
5. 🏖️ Retraite
6. 💐 Décès d'un proche
7. 💔 Divorce / Séparation
8. 🚀 Création d'entreprise

### Livrables

✅ **Dataset synthétique** : 10,000 clients avec 40+ features  
✅ **Code d'analyse** : Génération + ML baseline  
✅ **Présentation** : 6 slides LaTeX/Beamer  
✅ **Démarche de cadrage** : 3 phases structurées  
✅ **Modèle baseline** : Random Forest (F1-score ~70%)

---

## 🚀 Démarrage Rapide

### Prérequis

- Python 3.8+
- LaTeX (optionnel, pour la présentation)

### Installation et Exécution

```bash
# Cloner le repository
git clone https://github.com/votre-username/case-study-banque.git
cd case-study-banque

# Tout exécuter en une commande
make all
```

Ou étape par étape :

```bash
# Installer les dépendances
make setup

# Générer le dataset (10,000 clients)
make generate

# Exécuter l'analyse exploratoire
make analyze

# Compiler la présentation (si LaTeX installé)
make presentation
```

**Durée totale : ~2 minutes**

---

## 📁 Structure du Projet

```
case_study_banque/
├── README.md                     # Documentation
├── Makefile                      # Automatisation
├── code/
│   ├── generate_dataset.py      # Génération dataset
│   ├── analyse_exploratoire.py  # Analyse & ML
│   └── requirements.txt         # Dépendances
├── data/                         # Données générées
│   ├── clients_data.csv         # 10,000 clients
│   ├── life_events.csv          # Événements
│   ├── feature_importance.csv   # Features importantes
│   └── analyse_exploratoire.png # Visualisations
└── presentation/
    ├── presentation_cadrage.tex # Source LaTeX
    └── presentation_cadrage.pdf # Slides (après compilation)
```



---

## 📊 Dataset

### Caractéristiques

**10,000 clients** avec **40+ features** :

- **Démographiques** : âge, genre, situation familiale, CSP, région
- **Financières** : revenus, épargne, crédits en cours
- **Comportementales** : transactions, connexions app, visites agence
- **Signaux prédictifs** : simulations prêts, consultations produits

### 8 Moments de Vie

| Moment de Vie | Prévalence |
|--------------|------------|
| Mariage | ~3% |
| Naissance | ~4% |
| Achat immobilier | ~5% |
| Changement emploi | ~8% |
| Retraite | ~2% |
| Décès proche | ~3% |
| Divorce | ~2% |
| Création entreprise | ~1% |

## 📈 Résultats

### Performance du Modèle Baseline

| Métrique | Valeur |
|----------|--------|
| Algorithme | Random Forest |
| Précision | 70-75% |
| Recall | 60-65% |
| F1-Score | 65-70% |
| AUC-ROC | 0.75-0.80 |

### Top 5 Features Importantes

1. `simulation_pret_immobilier` (15%)
2. `age` (12%)
3. `epargne_totale` (10%)
4. `augmentation_epargne_recente` (8%)
5. `revenu_mensuel` (7%)

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
