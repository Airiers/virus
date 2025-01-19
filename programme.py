import keyboard
import time
import sys
import os
import shutil
import tkinter as tk
from tkinter import simpledialog, messagebox
from tkinter.ttk import *
import pkg_resources
from PIL import Image, ImageTk

# Définir les codes ANSI pour les couleurs
RESET = "\033[0m"  # Réinitialiser la couleur
GREEN = "\033[32m"  # Vert
RED = "\033[31m"  # Rouge

def print_colored(text, color):
    print(f"{color}{text}{RESET}")

def error(error):
    erreur1 = "Erreur : "
    erreur2 = error
    erreur = erreur1 + erreur2
    print_colored(erreur, RED)

print_colored("Ce texte est en vert.", GREEN)
print_colored("Ce texte est en rouge.", RED)
print('')
error("Rien ne va")

def executer_commande():
    commande = my_entry.get()
    print(commande)
    if commande.startswith("new_file"):
        parts = commande.split(maxsplit=1)
        if len(parts) == 2:
            chemin_fichier = parts[1]
            try:
                with open(chemin_fichier, 'w') as f:
                    f.write("")
                print(f"Fichier '{chemin_fichier}' créé avec succès.")
            except OSError as e:
                print(f"{RED}Erreur lors de la création du fichier : {e}{RESET}")
        else:
            print(f"{RED}Erreur, utilisation incorrecte de la commande 'new_file'. Utilisation : new_file <chemin_du_fichier>{RESET}")

    if commande.startswith("write_file"):
        parts = commande.split(maxsplit=2)
        if len(parts) == 3:
            chemin_fichier = parts[1]
            try:
                with open(chemin_fichier, 'w') as f:
                    f.write(parts[2])
                print(f"Fichier '{chemin_fichier}' créé avec succès.")
            except OSError as e:
                print(f"{RED}Erreur lors de la création du fichier : {e}{RESET}")
        else:
            print(f"{RED}Erreur, utilisation incorrecte de la commande 'new_file'. Utilisation : new_file <chemin_du_fichier>{RESET}")

    if commande.startswith("del_file"):
        parts = commande.split(maxsplit=1)
        if len(parts) == 2:
            chemin_fichier = parts[1]
            try:
                os.remove(chemin_fichier)
                print(f"Fichier '{chemin_fichier}' supprimé avec succès.")
            except OSError as e:
                print(f"{RED}Erreur lors de la suppression du fichier : {e}{RESET}")
        else:
            print(f"{RED}Erreur, utilisation incorrecte de la commande 'del_file'. Utilisation : del_file <chemin_du_fichier>{RESET}")

    if commande.startswith("add_in_file"):
        parts = commande.split(maxsplit=2)
        if len(parts) == 3:
            chemin_fichier = parts[1]
            try:
                with open(chemin_fichier, 'a') as f:
                    f.write(parts[2])
                print(f"Fichier '{chemin_fichier}' modifié avec succès.")
            except OSError as e:
                print(f"{RED}Erreur lors de la création du fichier : {e}{RESET}")
        else:
            print(f"{RED}Erreur, utilisation incorrecte de la commande 'add_in_file'. Utilisation : add_in_file <chemin_du_fichier>{RESET}")

    if commande.startswith("view_file"):
        parts = commande.split(maxsplit=1)
        if len(parts) == 2:
            chemin_fichier = parts[1]
            try:
                file = open(chemin_fichier, 'r')
                liste=file.readlines()
                print(liste)
                print(f"Fichier '{chemin_fichier}' lancé.")
            except OSError as e:
                print(f"{RED}Erreur lors de la création du fichier : {e}{RESET}")
        else:
            print(f"{RED}Erreur, utilisation incorrecte de la commande 'add_in_file'. Utilisation : add_in_file <chemin_du_fichier>{RESET}")

    elif commande == "help":
        print("Les commandes disponibles sont : help, new_file, del_file, write_file, add_in_file")
    elif commande.strip() == "":
        # Ignorer les commandes vides
        pass
    else:
        print(f"{RED}Erreur, commande inconnue : {commande}{RESET}")

    # Ajouter la commande à l'historique
    history_text.insert(tk.END, commande + "\n")

def copy_to_clipboard():
    selected_text = history_text.get(tk.SEL_FIRST, tk.SEL_LAST)
    root.clipboard_clear()
    root.clipboard_append(selected_text)

class CustomDialog(simpledialog.Dialog):
    def __init__(self, parent, title, prompt, **kwargs):
        self.prompt = prompt
        self.icon_path = icon_path  # Sauvegarde du chemin de l'icône
        super().__init__(parent, title=title, **kwargs)

    def body(self, master):
        # Définir l'icône après la création de la fenêtre
        self.iconbitmap(self.icon_path)

        tk.Label(master, text=self.prompt).grid(row=0)
        self.entry = tk.Entry(master)
        self.entry.grid(row=1)
        return self.entry

    def apply(self):
        self.result = self.entry.get()

def create_file():
    dialog = CustomDialog(root, title="Créer un fichier", prompt="Entrez le nom du fichier :")
    filename = dialog.result
    if filename:
        try:
            with open(filename, 'w') as f:
                f.write("")
            print(f"Fichier '{filename}' créé avec succès.")
            history_text.insert(tk.END, f"new_file {filename}\n")
        except OSError as e:
            messagebox.showerror("Erreur", f"Erreur lors de la création du fichier : {e}")

def delete_file():
    dialog = CustomDialog(root, title="Supprimer un fichier", prompt="Entrez le nom du fichier :")
    filename = dialog.result
    if filename:
        try:
            with open(filename, 'w') as f:
                os.remove(filename)
            print(f"Fichier '{filename}' supprimé avec succès.")
            history_text.insert(tk.END, f"delete_file {filename}\n")
        except OSError as e:
            messagebox.showerror("Erreur", f"Erreur lors de la création du fichier : {e}")

def write_file():
    dialog = CustomDialog(root, title="Écrire un fichier", prompt="Entrez le nom du fichier :")
    filename = dialog.result
    if filename:
        dialog = CustomDialog(root, title="Écrire un fichier", prompt="Entrez le contenu du fichier :")
        content = dialog.result
        try:
            with open(filename, 'w') as f:
                f.write(content)
            print(f"Fichier '{filename}' créé avec succès.")
            history_text.insert(tk.END, f"write_file {filename} {content}\n")
        except OSError as e:
            messagebox.showerror("Erreur", f"Erreur lors de la création du fichier : {e}")

def edit_file():
    dialog = CustomDialog(root, title="Modifier un fichier", prompt="Entrez le nom du fichier :")
    filename = dialog.result
    if filename:
        dialog = CustomDialog(root, title="Modifier un fichier", prompt="Entrez le contenu du fichier :")
        content = dialog.result
        try:
            with open(filename, 'a') as f:
                f.write(content)
            print(f"Fichier '{filename}' édité avec succès.")
            history_text.insert(tk.END, f"add_in_file {filename} {content}\n")
        except OSError as e:
            messagebox.showerror("Erreur", f"Erreur lors de la création du fichier : {e}")

# Utiliser pkg_resources pour obtenir le chemin du fichier icon.ico
icon_path = pkg_resources.resource_filename(__name__, "icon.ico")
file_icon_path = pkg_resources.resource_filename(__name__, "icon-file.png")

# Vérifier si le fichier icon.ico existe
if not os.path.exists(icon_path):
    error(f"Le fichier {icon_path} n'existe pas.")
    sys.exit(1)

root = tk.Tk()
root.iconbitmap(icon_path)
root.title('Programme.exe')

# Configurer la grille pour que les colonnes s'étendent
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(0, weight=1)

# Créer un cadre pour les entrées et les boutons
input_frame = tk.Frame(root)
input_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

label = tk.Label(input_frame, text="Entrez des commandes")
label.pack(pady=20)
my_entry = Entry(input_frame)
my_entry.pack(fill=tk.X, padx=10)  # Remplir horizontalement

# Ajouter un bouton pour exécuter la commande
execute_button = tk.Button(input_frame, text="Exécuter", command=executer_commande)
execute_button.pack(pady=10)

# Charger et redimensionner l'image
original_image = Image.open(file_icon_path)
resized_image = original_image.resize((20, 20), Image.LANCZOS)  # Redimensionner à 20x20 pixels
file_icon = ImageTk.PhotoImage(resized_image)

# Ajouter un bouton pour créer un fichier avec une icône
create_file_button = tk.Button(input_frame, image=file_icon, text="Créer un fichier", compound=tk.LEFT, command=create_file)
create_file_button.pack(pady=10)

write_file_button = tk.Button(input_frame, image=file_icon, text="Écrire un fichier", compound=tk.LEFT, command=write_file)
write_file_button.pack(pady=10)

write_file_button = tk.Button(input_frame, image=file_icon, text="Modifier un fichier", compound=tk.LEFT, command=edit_file)
write_file_button.pack(pady=10)

write_file_button = tk.Button(input_frame, image=file_icon, text="Supprimer un fichier", compound=tk.LEFT, command=delete_file)
write_file_button.pack(pady=10)

# Créer un cadre pour l'historique des commandes
history_frame = tk.Frame(root)
history_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

history_label = tk.Label(history_frame, text="Historique des commandes")
history_label.pack(pady=10)

history_text = tk.Text(history_frame, height=20, width=50)
history_text.pack(pady=10, fill=tk.BOTH, expand=True)

# Ajouter un menu contextuel pour copier le texte sélectionné
history_text.bind("<Button-3>", lambda event: copy_to_clipboard())

# Démarrer la boucle principale de Tkinter
root.mainloop()
