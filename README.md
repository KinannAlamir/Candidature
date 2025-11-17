# 🏦 Cadrage Data Science : Prédiction des Moments de Vie

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![LaTeX](https://img.shields.io/badge/LaTeX-Beamer-orange)](https://www.latex-project.org/)

**Case study :** Mission de cadrage data science (6 semaines) pour prédire les moments de vie des clients d'une banque française.

---

## 📋 Contexte du Case Study

**Mission :** Vous êtes sollicité pour intervenir sur le cadrage d'un cas d'usage data science visant à prédire des moments de vie des clients d'une banque française.

**Questions à traiter :**
- Quelle démarche de cadrage mettre en place à l'arrivée chez le client ?
- Quels sont les livrables associés ?
- Comment structurer une mission de 6 semaines ?

**Livrable attendu :** Présentation PPT de 5-6 slides avec hypothèses de travail.

---

## 🎯 Démarche de Cadrage Proposée

### Phase 1 : Compréhension Métier (S1-S2)
- Ateliers avec équipes Marketing, Retail Banking, Crédits
- Audit des données (CRM, transactions, comportements)
- Identification des 8 moments de vie prioritaires
- Définition des KPIs et métriques de succès

### Phase 2 : Structuration Technique (S3-S4)
- Architecture technique (ingestion, feature store, ML, API)
- Feature engineering (100+ variables comportementales)
- Sélection des algorithmes ML
- Roadmap de déploiement sur 12 mois

### Phase 3 : POC & Validation (S5-S6)
- POC sur 1-2 moments de vie prioritaires
- Tests et validation sur données historiques
- Dashboard de monitoring
- Présentation aux sponsors et recommandations

---

## 💡 8 Moments de Vie Identifiés

💍 **Mariage/PACS** • 👶 **Naissance** • 🏠 **Achat immobilier** • 💼 **Changement emploi**  
🏖️ **Retraite** • 💐 **Décès proche** • 💔 **Divorce** • 🚀 **Création entreprise**

**Hypothèses clés :**
- Signaux comportementaux détectables 3-6 mois avant l'événement
- Données CRM + transactionnelles suffisantes pour prédiction
- Précision >70% atteignable pour top 3 événements
- ROI positif avec 15% de conversion
- Conformité RGPD totale

---

## 📊 Contenu du Repository

### 1. Présentation Exécutive (Livrable principal)
📄 **\`presentation/presentation_cadrage.pdf\`** - 6 slides LaTeX/Beamer
- Démarche de cadrage (3 phases, 6 semaines)
- Architecture technique et roadmap
- Hypothèses de travail documentées
- ROI estimé sur top 3 use cases

\`\`\`bash
make presentation  # Compiler la présentation
\`\`\`

### 2. POC Technique (Illustration)
💻 **Dataset 100% synthétique** pour démonstration :
- 10,000 clients fictifs générés
- 40+ features réalistes
- 8 moments de vie simulés
- Prototype ML baseline (F1-score ~70%)

\`\`\`bash
make all  # Génère données + analyse + présentation (~2min)
\`\`\`

> **Important :** Le code et les données sont purement illustratifs pour valider la faisabilité technique. Aucune donnée réelle utilisée.

---

## 🗂️ Structure du Projet

\`\`\`
📂 case_study_banque/
├── 📊 presentation/
│   ├── presentation_cadrage.tex    # Source LaTeX (6 slides)
│   └── presentation_cadrage.pdf    # Livrable principal
├── 💻 code/
│   ├── generate_dataset.py         # Génération données synthétiques
│   ├── analyse_exploratoire.py     # Prototype ML
│   └── requirements.txt
└── 📊 data/
    ├── clients_data.csv            # 10K clients fictifs
    └── feature_importance.csv      # Résultats modèle
\`\`\`

---

## 💰 ROI Estimé

| Use Case | Volume/mois | ROI | Impact €/mois |
|----------|-------------|-----|---------------|
| 🏠 Achat Immobilier | 500 clients | +25% | €150-200K |
| 🏖️ Retraite | 200 clients | +22% | €80-120K |
| 👶 Naissance | 400 clients | +18% | €70-100K |

**Impact total :** €300-420K/mois de revenus additionnels estimés

---

## 🚀 Démarrage Rapide

\`\`\`bash
# Cloner le repository
git clone https://github.com/KinannAlamir/Candidature.git
cd case_study_banque

# Option 1 : Tout générer
make all

# Option 2 : Étape par étape
make setup        # Installer dépendances
make generate     # Générer dataset synthétique
make analyze      # Analyser et entraîner modèle
make presentation # Compiler slides
\`\`\`

---

## 📄 Informations

**License :** MIT - Projet éducatif  
**Données :** 100% synthétiques - aucune donnée réelle  
**Auteur :** Case study de cadrage data science - Novembre 2025

**🎯 Livrable principal :** \`presentation/presentation_cadrage.pdf\`
