"""
Analyse exploratoire et preprocessing du dataset bancaire
Prédiction des moments de vie
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import warnings
warnings.filterwarnings('ignore')

# Configuration graphiques
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

def load_data():
    """Charge les données"""
    print("📂 Chargement des données...")
    clients_df = pd.read_csv('../data/clients_data.csv')
    life_events_df = pd.read_csv('../data/life_events.csv')
    print(f"   ✓ {len(clients_df)} clients chargés")
    print(f"   ✓ {len(life_events_df)} événements chargés")
    return clients_df, life_events_df

def exploratory_analysis(clients_df, life_events_df):
    """Analyse exploratoire des données"""
    print("\n📊 ANALYSE EXPLORATOIRE")
    print("=" * 70)
    
    # 1. Vue d'ensemble
    print("\n1. Vue d'ensemble des données clients:")
    print(clients_df.describe())
    
    print("\n2. Distribution des CSP:")
    print(clients_df['csp'].value_counts())
    
    print("\n3. Distribution des situations familiales:")
    print(clients_df['situation_familiale'].value_counts())
    
    # 2. Analyse des moments de vie
    print("\n4. Distribution des moments de vie:")
    event_counts = life_events_df['moment_de_vie'].value_counts()
    print(event_counts)
    
    # 3. Corrélations
    print("\n5. Analyse des corrélations (features numériques):")
    numeric_cols = clients_df.select_dtypes(include=[np.number]).columns
    correlation_matrix = clients_df[numeric_cols].corr()
    print("\nTop 10 corrélations les plus fortes:")
    # Extraire les corrélations sans la diagonale
    corr_pairs = []
    for i in range(len(correlation_matrix.columns)):
        for j in range(i+1, len(correlation_matrix.columns)):
            corr_pairs.append({
                'feature1': correlation_matrix.columns[i],
                'feature2': correlation_matrix.columns[j],
                'correlation': abs(correlation_matrix.iloc[i, j])
            })
    corr_df = pd.DataFrame(corr_pairs).sort_values('correlation', ascending=False)
    print(corr_df.head(10))
    
    return correlation_matrix

def create_target_variable(clients_df, life_events_df, target_event='achat_immobilier'):
    """Crée la variable cible pour un moment de vie spécifique"""
    print(f"\n🎯 Création de la variable cible pour: {target_event}")
    
    # Identifier les clients ayant vécu cet événement
    target_clients = life_events_df[
        life_events_df['moment_de_vie'] == target_event
    ]['client_id'].unique()
    
    # Créer la variable cible
    clients_df['target'] = clients_df['client_id'].isin(target_clients).astype(int)
    
    # Distribution de la cible
    target_dist = clients_df['target'].value_counts()
    print(f"   Distribution de la cible:")
    print(f"   - Classe 0 (pas d'événement): {target_dist[0]} ({target_dist[0]/len(clients_df)*100:.1f}%)")
    print(f"   - Classe 1 (événement): {target_dist[1]} ({target_dist[1]/len(clients_df)*100:.1f}%)")
    
    return clients_df

def preprocess_data(clients_df):
    """Preprocessing des données"""
    print("\n🔧 Preprocessing des données...")
    
    # 1. Séparer features et target
    if 'target' not in clients_df.columns:
        raise ValueError("La variable target doit être créée avant le preprocessing")
    
    target = clients_df['target']
    features_df = clients_df.drop(['client_id', 'target'], axis=1)
    
    # 2. Encoder les variables catégorielles
    categorical_cols = features_df.select_dtypes(include=['object']).columns
    print(f"   Encodage de {len(categorical_cols)} variables catégorielles...")
    
    le_dict = {}
    for col in categorical_cols:
        le = LabelEncoder()
        features_df[col] = le.fit_transform(features_df[col])
        le_dict[col] = le
    
    # 3. Normalisation des features numériques
    print("   Normalisation des features numériques...")
    scaler = StandardScaler()
    features_scaled = scaler.fit_transform(features_df)
    features_df_scaled = pd.DataFrame(features_scaled, columns=features_df.columns)
    
    print(f"   ✓ Dataset preprocessé: {features_df_scaled.shape}")
    
    return features_df_scaled, target, le_dict, scaler

def build_baseline_model(X, y):
    """Construit un modèle de base pour évaluer la prédictibilité"""
    print("\n🤖 Construction d'un modèle baseline (Random Forest)...")
    
    # Split train/test
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42, stratify=y
    )
    
    print(f"   Train set: {X_train.shape[0]} samples")
    print(f"   Test set: {X_test.shape[0]} samples")
    
    # Entraînement
    print("   Entraînement du modèle...")
    rf_model = RandomForestClassifier(
        n_estimators=100,
        max_depth=10,
        random_state=42,
        class_weight='balanced'  # Pour gérer le déséquilibre
    )
    rf_model.fit(X_train, y_train)
    
    # Prédictions
    y_pred = rf_model.predict(X_test)
    
    # Évaluation
    print("\n   📈 Performance du modèle:")
    print(classification_report(y_test, y_pred, target_names=['Pas d\'événement', 'Événement']))
    
    # Feature importance
    print("\n   🔍 Top 10 features les plus importantes:")
    feature_importance = pd.DataFrame({
        'feature': X.columns,
        'importance': rf_model.feature_importances_
    }).sort_values('importance', ascending=False)
    print(feature_importance.head(10).to_string(index=False))
    
    return rf_model, feature_importance

def generate_visualizations(clients_df, life_events_df, correlation_matrix, feature_importance):
    """Génère les visualisations"""
    print("\n📊 Génération des visualisations...")
    
    fig, axes = plt.subplots(2, 3, figsize=(18, 12))
    fig.suptitle('Analyse Exploratoire - Prédiction des Moments de Vie', fontsize=16, fontweight='bold')
    
    # 1. Distribution des âges
    axes[0, 0].hist(clients_df['age'], bins=30, edgecolor='black', alpha=0.7)
    axes[0, 0].set_title('Distribution des âges')
    axes[0, 0].set_xlabel('Âge')
    axes[0, 0].set_ylabel('Fréquence')
    axes[0, 0].grid(True, alpha=0.3)
    
    # 2. Distribution des CSP
    csp_counts = clients_df['csp'].value_counts()
    axes[0, 1].bar(range(len(csp_counts)), csp_counts.values)
    axes[0, 1].set_title('Distribution des CSP')
    axes[0, 1].set_xticks(range(len(csp_counts)))
    axes[0, 1].set_xticklabels(csp_counts.index, rotation=45, ha='right')
    axes[0, 1].set_ylabel('Nombre de clients')
    axes[0, 1].grid(True, alpha=0.3)
    
    # 3. Distribution des moments de vie
    event_counts = life_events_df['moment_de_vie'].value_counts()
    axes[0, 2].barh(range(len(event_counts)), event_counts.values)
    axes[0, 2].set_title('Distribution des moments de vie')
    axes[0, 2].set_yticks(range(len(event_counts)))
    axes[0, 2].set_yticklabels(event_counts.index)
    axes[0, 2].set_xlabel('Nombre d\'événements')
    axes[0, 2].grid(True, alpha=0.3)
    
    # 4. Revenus vs Épargne
    axes[1, 0].scatter(clients_df['revenu_mensuel'], clients_df['epargne_totale'], 
                      alpha=0.5, s=10)
    axes[1, 0].set_title('Revenus vs Épargne')
    axes[1, 0].set_xlabel('Revenu mensuel (€)')
    axes[1, 0].set_ylabel('Épargne totale (€)')
    axes[1, 0].grid(True, alpha=0.3)
    
    # 5. Heatmap des corrélations (top features)
    top_features = feature_importance.head(10)['feature'].tolist()
    if all(feat in correlation_matrix.columns for feat in top_features):
        corr_subset = correlation_matrix.loc[top_features, top_features]
        sns.heatmap(corr_subset, annot=True, fmt='.2f', cmap='coolwarm', 
                   center=0, ax=axes[1, 1], cbar_kws={'label': 'Corrélation'})
        axes[1, 1].set_title('Corrélations (Top 10 features)')
    else:
        axes[1, 1].text(0.5, 0.5, 'Corrélations non disponibles', 
                       ha='center', va='center', transform=axes[1, 1].transAxes)
        axes[1, 1].set_title('Corrélations')
    
    # 6. Feature importance
    top_10_features = feature_importance.head(10)
    axes[1, 2].barh(range(len(top_10_features)), top_10_features['importance'])
    axes[1, 2].set_title('Top 10 Features Importantes')
    axes[1, 2].set_yticks(range(len(top_10_features)))
    axes[1, 2].set_yticklabels(top_10_features['feature'])
    axes[1, 2].set_xlabel('Importance')
    axes[1, 2].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('../data/analyse_exploratoire.png', dpi=300, bbox_inches='tight')
    print("   ✓ Visualisations sauvegardées: analyse_exploratoire.png")
    
    plt.close()

def main():
    """Fonction principale"""
    print("🏦 ANALYSE EXPLORATOIRE - PRÉDICTION DES MOMENTS DE VIE")
    print("=" * 70)
    
    # 1. Charger les données
    clients_df, life_events_df = load_data()
    
    # 2. Analyse exploratoire
    correlation_matrix = exploratory_analysis(clients_df, life_events_df)
    
    # 3. Créer la variable cible (exemple: achat immobilier)
    clients_df = create_target_variable(clients_df, life_events_df, target_event='achat_immobilier')
    
    # 4. Preprocessing
    X, y, le_dict, scaler = preprocess_data(clients_df)
    
    # 5. Modèle baseline
    model, feature_importance = build_baseline_model(X, y)
    
    # 6. Visualisations
    generate_visualizations(clients_df, life_events_df, correlation_matrix, feature_importance)
    
    # 7. Sauvegarder les résultats
    print("\n💾 Sauvegarde des résultats...")
    feature_importance.to_csv('../data/feature_importance.csv', index=False)
    print("   ✓ feature_importance.csv")
    
    print("\n✅ Analyse terminée avec succès!")
    print("\n📋 Prochaines étapes recommandées:")
    print("   1. Tester différents modèles (XGBoost, LightGBM, Neural Networks)")
    print("   2. Optimiser les hyperparamètres")
    print("   3. Créer des features d'interaction")
    print("   4. Implémenter une validation croisée stratifiée")
    print("   5. Analyser les erreurs de prédiction")

if __name__ == "__main__":
    main()
