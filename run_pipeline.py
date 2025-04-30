import subprocess
import time
import os

# Fonction pour exécuter un script
def run_script(script_path):
    print(f"🚀 Exécution de {script_path}...")
    result = subprocess.run(["python", script_path], capture_output=True, text=True)
    if result.returncode != 0:
        print("❌ Erreur :")
        print(result.stderr)
    else:
        print("✅ Succès :")
        print(result.stdout)

# Étape 1 : Générer le dataset
generate_dataset_script = os.path.join("data", "generate_dataset.py")
run_script(generate_dataset_script)

# Petite pause pour la lisibilité
time.sleep(1)

# Étape 2 : Entraîner le modèle
train_model_script = os.path.join("model", "train_model.py")
run_script(train_model_script)

# Petite pause pour la lisibilité
time.sleep(1)

# Étape 3 : Lancer Streamlit (ne pas capturer output ici pour voir l'interface)
streamlit_app_script = "streamlit_app.py"
print("🌐 Lancement de l'application Streamlit...")
subprocess.run(["streamlit", "run", streamlit_app_script])