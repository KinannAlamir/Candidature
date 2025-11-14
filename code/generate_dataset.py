"""
Génération du dataset synthétique pour la prédiction des moments de vie
Banque française - Cas d'étude Data Science

Hypothèses:
- 10,000 clients avec historique transactionnel sur 24 mois
- 8 moments de vie principaux à prédire
- Features: démographiques, comportementales, transactionnelles
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Fixer la seed pour la reproductibilité
np.random.seed(42)
random.seed(42)

# Paramètres
N_CLIENTS = 10000
START_DATE = datetime(2023, 1, 1)
END_DATE = datetime(2024, 12, 31)

# Définition des moments de vie à prédire
MOMENTS_DE_VIE = {
    'mariage': {'prob': 0.03, 'age_range': (25, 40)},
    'naissance': {'prob': 0.04, 'age_range': (25, 45)},
    'achat_immobilier': {'prob': 0.05, 'age_range': (25, 55)},
    'changement_emploi': {'prob': 0.08, 'age_range': (22, 60)},
    'retraite': {'prob': 0.02, 'age_range': (60, 70)},
    'deces_proche': {'prob': 0.03, 'age_range': (30, 80)},
    'divorce': {'prob': 0.02, 'age_range': (30, 60)},
    'creation_entreprise': {'prob': 0.01, 'age_range': (25, 55)}
}

def generate_clients():
    """Génère les données clients de base"""
    
    clients = []
    
    for client_id in range(1, N_CLIENTS + 1):
        age = np.random.normal(45, 15)
        age = max(18, min(85, age))  # Limiter entre 18 et 85 ans
        
        # Génération des caractéristiques démographiques
        client = {
            'client_id': f'CLI_{client_id:06d}',
            'age': int(age),
            'genre': np.random.choice(['H', 'F'], p=[0.48, 0.52]),
            'situation_familiale': np.random.choice(
                ['celibataire', 'marie', 'divorce', 'veuf'], 
                p=[0.35, 0.45, 0.15, 0.05]
            ),
            'nb_enfants': np.random.choice([0, 1, 2, 3, 4], p=[0.35, 0.25, 0.25, 0.10, 0.05]),
            'csp': np.random.choice(
                ['cadre', 'employe', 'ouvrier', 'profession_liberale', 'retraite', 'etudiant'],
                p=[0.20, 0.35, 0.15, 0.10, 0.15, 0.05]
            ),
            'region': np.random.choice(
                ['IDF', 'PACA', 'ARA', 'Occitanie', 'HDF', 'Autre'],
                p=[0.25, 0.12, 0.12, 0.10, 0.10, 0.31]
            ),
            'anciennete_banque_mois': int(np.random.exponential(60) + 6),
        }
        
        # Génération des caractéristiques financières
        if client['csp'] == 'cadre':
            revenu_base = np.random.normal(4500, 1500)
        elif client['csp'] == 'profession_liberale':
            revenu_base = np.random.normal(5500, 2000)
        elif client['csp'] == 'employe':
            revenu_base = np.random.normal(2500, 800)
        elif client['csp'] == 'ouvrier':
            revenu_base = np.random.normal(2000, 600)
        elif client['csp'] == 'retraite':
            revenu_base = np.random.normal(1800, 500)
        else:  # etudiant
            revenu_base = np.random.normal(800, 300)
        
        client['revenu_mensuel'] = max(0, revenu_base)
        client['epargne_totale'] = max(0, np.random.exponential(client['revenu_mensuel'] * 12))
        client['credits_en_cours'] = np.random.choice([0, 1, 2, 3], p=[0.50, 0.30, 0.15, 0.05])
        
        # Génération des comportements bancaires
        client['nb_produits_bancaires'] = np.random.choice([1, 2, 3, 4, 5], p=[0.15, 0.30, 0.30, 0.20, 0.05])
        client['utilise_app_mobile'] = np.random.choice([0, 1], p=[0.30, 0.70])
        client['nb_connexions_mois'] = int(np.random.exponential(15) if client['utilise_app_mobile'] else np.random.exponential(3))
        
        # Moyennes transactionnelles (derniers 6 mois)
        client['montant_moyen_transactions'] = max(0, np.random.normal(1500, 800))
        client['nb_transactions_mois'] = int(np.random.normal(25, 15))
        client['ratio_depenses_revenus'] = min(1.5, max(0.3, np.random.normal(0.75, 0.15)))
        
        # Contacts avec la banque
        client['nb_appels_conseiller_6mois'] = np.random.choice([0, 1, 2, 3, 4, 5], p=[0.40, 0.30, 0.15, 0.08, 0.05, 0.02])
        client['nb_visites_agence_6mois'] = np.random.choice([0, 1, 2, 3], p=[0.50, 0.30, 0.15, 0.05])
        
        clients.append(client)
    
    return pd.DataFrame(clients)

def generate_life_events(clients_df):
    """Génère les moments de vie pour chaque client"""
    
    life_events = []
    
    for _, client in clients_df.iterrows():
        client_age = client['age']
        
        # Pour chaque moment de vie, déterminer si le client le vit
        for event_type, event_params in MOMENTS_DE_VIE.items():
            age_min, age_max = event_params['age_range']
            base_prob = event_params['prob']
            
            # Ajuster la probabilité selon l'âge
            if age_min <= client_age <= age_max:
                prob = base_prob
            else:
                prob = base_prob * 0.1  # Probabilité réduite hors de la tranche d'âge optimale
            
            # Déterminer si l'événement se produit
            if np.random.random() < prob:
                # Date de l'événement (dans les 12 prochains mois)
                days_offset = np.random.randint(0, 365)
                event_date = START_DATE + timedelta(days=days_offset)
                
                life_events.append({
                    'client_id': client['client_id'],
                    'moment_de_vie': event_type,
                    'date_evenement': event_date,
                    'horizon_prediction': '12_mois'  # Horizon de prédiction
                })
    
    return pd.DataFrame(life_events)

def add_behavioral_signals(clients_df, life_events_df):
    """Ajoute des signaux comportementaux liés aux moments de vie"""
    
    # Créer des features additionnelles basées sur les moments de vie à venir
    for _, event in life_events_df.iterrows():
        client_id = event['client_id']
        event_type = event['moment_de_vie']
        
        # Ajouter des signaux faibles dans les données
        idx = clients_df[clients_df['client_id'] == client_id].index[0]
        
        # Signaux spécifiques par type d'événement
        if event_type == 'mariage':
            clients_df.loc[idx, 'recherche_pret_perso_recent'] = 1
            clients_df.loc[idx, 'augmentation_epargne_recente'] = np.random.choice([0, 1], p=[0.3, 0.7])
        
        elif event_type == 'naissance':
            clients_df.loc[idx, 'ouverture_compte_epargne_recent'] = 1
            clients_df.loc[idx, 'consultation_assurance_vie'] = 1
        
        elif event_type == 'achat_immobilier':
            clients_df.loc[idx, 'simulation_pret_immobilier'] = 1
            clients_df.loc[idx, 'augmentation_epargne_recente'] = 1
            clients_df.loc[idx, 'nb_connexions_mois'] = int(clients_df.loc[idx, 'nb_connexions_mois'] * 1.3)
        
        elif event_type == 'changement_emploi':
            clients_df.loc[idx, 'variation_revenus_recente'] = 1
            clients_df.loc[idx, 'nb_appels_conseiller_6mois'] += 1
        
        elif event_type == 'retraite':
            clients_df.loc[idx, 'consultation_placements'] = 1
            clients_df.loc[idx, 'nb_visites_agence_6mois'] += 1
        
        elif event_type == 'creation_entreprise':
            clients_df.loc[idx, 'consultation_pret_pro'] = 1
            clients_df.loc[idx, 'nb_appels_conseiller_6mois'] += 2
    
    # Remplir les NaN pour les nouvelles colonnes
    signal_columns = [
        'recherche_pret_perso_recent', 'augmentation_epargne_recente',
        'ouverture_compte_epargne_recent', 'consultation_assurance_vie',
        'simulation_pret_immobilier', 'variation_revenus_recente',
        'consultation_placements', 'consultation_pret_pro'
    ]
    
    for col in signal_columns:
        if col in clients_df.columns:
            clients_df[col].fillna(0, inplace=True)
        else:
            clients_df[col] = 0
    
    return clients_df

def main():
    """Fonction principale de génération du dataset"""
    
    print("🏦 Génération du dataset bancaire - Prédiction des moments de vie")
    print("=" * 70)
    
    # 1. Générer les clients
    print("\n📊 Génération des données clients...")
    clients_df = generate_clients()
    print(f"   ✓ {len(clients_df)} clients générés")
    
    # 2. Générer les moments de vie
    print("\n🎯 Génération des moments de vie...")
    life_events_df = generate_life_events(clients_df)
    print(f"   ✓ {len(life_events_df)} événements générés")
    
    # Distribution des événements
    print("\n   Distribution des moments de vie:")
    for event, count in life_events_df['moment_de_vie'].value_counts().items():
        print(f"   - {event}: {count} ({count/len(life_events_df)*100:.1f}%)")
    
    # 3. Ajouter des signaux comportementaux
    print("\n🔍 Ajout des signaux comportementaux...")
    clients_df = add_behavioral_signals(clients_df, life_events_df)
    print(f"   ✓ Signaux ajoutés")
    
    # 4. Sauvegarder les datasets
    print("\n💾 Sauvegarde des datasets...")
    clients_df.to_csv('../data/clients_data.csv', index=False)
    life_events_df.to_csv('../data/life_events.csv', index=False)
    print("   ✓ clients_data.csv")
    print("   ✓ life_events.csv")
    
    # 5. Statistiques finales
    print("\n📈 Statistiques du dataset:")
    print(f"   - Nombre de clients: {len(clients_df)}")
    print(f"   - Nombre de features: {len(clients_df.columns)}")
    print(f"   - Nombre d'événements: {len(life_events_df)}")
    print(f"   - Clients avec au moins 1 événement: {life_events_df['client_id'].nunique()}")
    print(f"   - Taux de clients avec événement: {life_events_df['client_id'].nunique()/len(clients_df)*100:.1f}%")
    
    print("\n✅ Dataset généré avec succès!")

if __name__ == "__main__":
    main()
