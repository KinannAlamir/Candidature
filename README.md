# 🏦 Prédiction des Moments de Vie - Data Science Case Study

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebooks-orange)](https://jupyter.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Projet de data science pour prédire les moments de vie des clients bancaires et personnaliser les offres commerciales.

---

## � Quick Start

```bash
# 1. Clone the repository
git clone <repo-url>
cd case_study_banque

# 2. Install dependencies
cd code
pip install -r requirements.txt

# 3. Launch Jupyter
jupyter notebook

# 4. Run notebooks in order:
#    → 1_generation_donnees.ipynb
#    → 2_analyse_exploratoire.ipynb
#    → 3_resultats_concrets.ipynb
```

**Temps d'exécution total :** ~15 minutes

---

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

## 📁 Structure du Projet

```
case_study_banque/
├── code/
│   ├── 1_generation_donnees.ipynb       # Génération dataset synthétique
│   ├── 2_analyse_exploratoire.ipynb     # Analyse et modèle baseline
│   ├── 3_resultats_concrets.ipynb       # Résultats business
│   └── requirements.txt                 # Dépendances Python
├── data/                                 # Données générées (vide au départ)
├── docs/                                 # Documentation détaillée
├── presentation/                         # Présentation LaTeX
│   ├── presentation_cadrage.pdf         # Slides finales
│   └── presentation_cadrage.tex         # Source LaTeX
└── README.md
```

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

## 🛠️ Technologies

- **Python 3.8+** - Langage principal
- **Pandas, NumPy** - Manipulation de données
- **Scikit-learn** - Machine learning
- **Matplotlib, Seaborn** - Visualisations
- **Jupyter** - Notebooks interactifs

---

## 📚 Documentation

- **`docs/HYPOTHESES_ET_METHODOLOGIE.md`** - Approche détaillée
- **`docs/LIVRABLES.md`** - Liste complète des livrables
- **`INSTRUCTIONS.md`** - Contexte du case study

---

## ⚠️ Note Importante

> Les données sont **100% synthétiques** et générées pour démonstration. Aucune donnée bancaire réelle n'est utilisée.

---

## � License

MIT License - Voir le fichier [LICENSE](LICENSE) pour plus de détails.

---
