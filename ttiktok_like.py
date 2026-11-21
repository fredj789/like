import sys
import time
import webbrowser
import pyautogui
import pyperclip

LIVE_URL = "https://www.tiktok.com/@jfredj3/live"
TOUCHE_COLLAGE = "command" if sys.platform == "darwin" else "ctrl"


def attendre_position(instruction):
    print(f"{instruction} Tu as 5 secondes.", flush=True)
    time.sleep(0.001)


def envoyer_likes():
    try:
        nombre = int(input("Combien de likes ? "))
    except ValueError:
        print("Entre un nombre entier.")
        return

    if nombre < 1:
        print("Entre un nombre supérieur à zéro.")
        return

    attendre_position("Place la souris sur le cœur.")
    pyautogui.click(clicks=nombre, interval=0.2)


def partager_live():
    print("Dans TikTok, ouvre Partager et choisis ton ami.")
    if input("Tape OUI pour confirmer l’envoi : ").strip().upper() != "OUI":
        return

    attendre_position("Place la souris sur le bouton Envoyer de cet ami.")
    pyautogui.click()


def repondre_commentaire():
    message = input("Écris ta réponse : ").strip()
    if not message:
        return

    pyperclip.copy(message)
    print("Dans TikTok, clique sur Répondre sous le commentaire choisi.")
    attendre_position("Place la souris dans le champ de réponse.")
    pyautogui.click()
    pyautogui.hotkey(TOUCHE_COLLAGE, "v")

    print("Vérifie le commentaire et le texte dans TikTok avant l’envoi.")
    if input("Tape OUI pour envoyer : ").strip().upper() != "OUI":
        return

    attendre_position("Place la souris sur le bouton d’envoi du commentaire.")
    pyautogui.click()


def main():
    webbrowser.open(LIVE_URL)
    actions = {
        "1": envoyer_likes,
        "2": partager_live,
        "3": repondre_commentaire,
    }

    try:
        while True:
            print("\n1. Likes  |  2. Partager  |  3. Répondre  |  0. Quitter")
            choix = input("Ton choix : ").strip()

            if choix == "0":
                break

            action = actions.get(choix)
            if action is None:
                print("Choisis une option de 0 à 3.")
                continue

            try:
                action()
            except pyperclip.PyperclipException:
                print("Presse-papiers indisponible. Saisis la réponse dans TikTok.")
    except (pyautogui.FailSafeException, KeyboardInterrupt):
        print("\nRobot arrêté.")


if __name__ == "__main__":
    main()