import sys

# Vérifier qu'un fichier est donné en argument
if len(sys.argv) < 2:
    print("Usage : python execute_moncode.py fichier.moncode")
    sys.exit(1)

# Lire le fichier .moncode
nom_fichier = sys.argv[1]
try:
    with open(nom_fichier, "r", encoding="utf-8") as fichier:
        code_python = fichier.read()
        exec(code_python)  # Exécute le code Python traduit
except Exception as e:
    print(f"Erreur lors de l'exécution : {e}")
