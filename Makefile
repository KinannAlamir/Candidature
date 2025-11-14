.PHONY: help setup generate analyze presentation clean all

# Variables
PYTHON = python3
VENV = venv
PDFLATEX = pdflatex

help:
	@echo "🏦 Cas d'Étude Data Science - Prédiction des Moments de Vie"
	@echo "============================================================"
	@echo ""
	@echo "Commandes disponibles:"
	@echo "  make setup         - Créer l'environnement virtuel et installer les dépendances"
	@echo "  make generate      - Générer le dataset synthétique"
	@echo "  make analyze       - Exécuter l'analyse exploratoire"
	@echo "  make presentation  - Compiler la présentation LaTeX"
	@echo "  make all           - Exécuter toutes les étapes"
	@echo "  make clean         - Nettoyer les fichiers temporaires"
	@echo ""

setup:
	@echo "📦 Installation des dépendances..."
	$(PYTHON) -m pip install --upgrade pip
	$(PYTHON) -m pip install -r code/requirements.txt
	@echo "✅ Setup terminé!"

generate:
	@echo "📊 Génération du dataset..."
	cd code && $(PYTHON) generate_dataset.py
	@echo "✅ Dataset généré!"

analyze:
	@echo "🔍 Analyse exploratoire..."
	cd code && $(PYTHON) analyse_exploratoire.py
	@echo "✅ Analyse terminée!"

presentation:
	@echo "📄 Compilation de la présentation..."
	cd presentation && $(PDFLATEX) presentation_cadrage.tex
	cd presentation && $(PDFLATEX) presentation_cadrage.tex
	@echo "✅ Présentation compilée: presentation/presentation_cadrage.pdf"

all: setup generate analyze
	@echo ""
	@echo "✅ Toutes les étapes sont terminées!"
	@echo ""
	@echo "📋 Fichiers générés:"
	@echo "  - data/clients_data.csv"
	@echo "  - data/life_events.csv"
	@echo "  - data/feature_importance.csv"
	@echo "  - data/analyse_exploratoire.png"
	@echo ""
	@echo "📖 Pour compiler la présentation: make presentation"

clean:
	@echo "🧹 Nettoyage..."
	rm -f presentation/*.aux presentation/*.log presentation/*.nav presentation/*.out presentation/*.snm presentation/*.toc
	rm -rf code/__pycache__
	@echo "✅ Nettoyage terminé!"
