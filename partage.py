import tkinter as tk
from tkinter import messagebox
from urllib.parse import urlsplit
import webbrowser


def preparer_invitation():
    lien = champ_lien.get().strip()

    try:
        adresse = urlsplit(lien)
        domaine = adresse.hostname or ""
    except ValueError:
        domaine = ""

    if not lien.startswith("https://") or not (
        domaine == "tiktok.com" or domaine.endswith(".tiktok.com")
    ):
        messagebox.showerror("Lien invalide", "Colle un lien TikTok en https://.")
        return

    invitation = f"🔴 Je suis en LIVE sur TikTok ! Passe dire bonjour 😊\n{lien}"
    fenetre.clipboard_clear()
    fenetre.clipboard_append(invitation)
    statut.set("Invitation copiée. Garde cette fenêtre ouverte jusqu’au collage.")
    webbrowser.open(lien)


fenetre = tk.Tk()
fenetre.title("Partager mon LIVE TikTok")

tk.Label(fenetre, text="Colle le lien de ton LIVE TikTok").pack(padx=16, pady=(16, 6))

champ_lien = tk.Entry(fenetre, width=55)
champ_lien.pack(padx=16)
champ_lien.focus()

tk.Button(
    fenetre,
    text="Copier l’invitation et ouvrir le LIVE",
    command=preparer_invitation,
).pack(pady=12)

statut = tk.StringVar()
tk.Label(fenetre, textvariable=statut, wraplength=350).pack(padx=16, pady=(0, 12))

fenetre.mainloop()