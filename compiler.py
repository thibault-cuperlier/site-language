import sys
import tkinter as tk
from tkinter import filedialog, messagebox

def executer_fichier(nom_fichier):
    """Lit et exécute le fichier .moncode"""
    try:
        with open(nom_fichier, "r", encoding="utf-8") as fichier:
            code_python = fichier.read()
            print("\n🔹 Exécution du fichier :", nom_fichier)
            exec(code_python)  # Exécuter le code traduit
            print("\n✅ Exécution terminée avec succès.")
    except Exception as e:
        print(f"\n❌ Erreur lors de l'exécution : {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Exécution par glisser-déposer
        fichier_moncode = sys.argv[1]
        executer_fichier(fichier_moncode)
    else:
        # Si le script est lancé sans argument, afficher une boîte de sélection
        root = tk.Tk()
        root.withdraw()  # Masquer la fenêtre principale Tkinter

        messagebox.showinfo("Instructions", 
            "👉 Pour exécuter un fichier :\n"
            "- Glissez-déposez un fichier .moncode sur ce script\n"
            "OU\n"
            "- Sélectionnez un fichier manuellement en cliquant sur OK"
        )

        fichier_moncode = filedialog.askopenfilename(
            title="Sélectionnez un fichier .moncode",
            filetypes=[("Fichiers MonCode", "*.moncode")]
        )

        if fichier_moncode:
            executer_fichier(fichier_moncode)
        else:
            print("\nℹ️ Aucune action effectuée. Aucun fichier sélectionné.")
