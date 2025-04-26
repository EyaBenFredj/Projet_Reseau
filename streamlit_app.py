import streamlit as st
import pandas as pd
from app.models.model_inference import predict_strategy

# Titre de l'application
st.title("🌐 MultiSync AI - Assistant de Synchronisation Réseau")

st.subheader("🎯 Prédisez la meilleure stratégie de synchronisation réseau")

# --- Section 1: Prédiction manuelle avec sliders ---
st.header("🔧 Entrée Manuelle")

# Entrées utilisateur
bandwidth = st.slider('Bande Passante (Mbps)', min_value=1, max_value=100, value=50)
usage = st.slider('Utilisation du réseau (%)', min_value=0.0, max_value=1.0, value=0.5)
latency = st.slider('Latence (ms)', min_value=1, max_value=300, value=100)

# Bouton pour prédire
if st.button('Prédire la Stratégie'):
    prediction = predict_strategy(bandwidth, usage, latency)
    st.success(f"La stratégie recommandée est : **{prediction}**")

# --- Séparation visuelle ---
st.markdown("---")

# --- Section 2: Prédiction avec un fichier CSV ---
st.header("📄 Prédictions à partir d'un fichier CSV")

st.write("""
Vous pouvez uploader un fichier CSV contenant les colonnes suivantes :
- `bandwidth`
- `usage`
- `latency`
""")

# Uploader un fichier
uploaded_file = st.file_uploader("Choisissez un fichier CSV", type=["csv"])

if uploaded_file is not None:
    try:
        # Lire le fichier CSV
        data = pd.read_csv(uploaded_file)

        # Vérifier que les colonnes nécessaires sont présentes
        expected_columns = {"bandwidth", "usage", "latency"}
        if not expected_columns.issubset(set(data.columns)):
            st.error(f"Le fichier doit contenir les colonnes suivantes : {expected_columns}")
        else:
            st.success("Fichier correctement chargé 🎉")

            # Appliquer la prédiction pour chaque ligne
            predictions = []
            for idx, row in data.iterrows():
                pred = predict_strategy(row['bandwidth'], row['usage'], row['latency'])
                predictions.append(pred)

            # Ajouter les prédictions dans le DataFrame
            data['predicted_strategy'] = predictions

            # Afficher les résultats
            st.dataframe(data)

            # Proposer un téléchargement du résultat
            csv = data.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="📥 Télécharger les résultats en CSV",
                data=csv,
                file_name='predictions.csv',
                mime='text/csv',
            )

    except Exception as e:
        st.error(f"Erreur lors du traitement du fichier : {e}")