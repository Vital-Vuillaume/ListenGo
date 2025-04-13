import speech_recognition as sr
import pyttsx3
import subprocess
import time

recognizer = sr.Recognizer()
engine = pyttsx3.init()

engine.setProperty('rate', 150)

voix = engine.getProperty('voices')

for voix_dispo in voix:
    if 'fr-ch' in voix_dispo.languages:
        engine.setProperty('voice', voix_dispo.id)


def Script(scriptSh):
    subprocess.run(['bash', './script/' + scriptSh], check=True)

def Reader(read):
    engine.say(read)
    time.sleep(5)
    engine.runAndWait()

def listen_for_test():
    with sr.Microphone() as source:
        print("Dites quelque chose...")
        recognizer.adjust_for_ambient_noise(source)

        program = True

        while program:
            try:
                audio = recognizer.listen(source)
                text = recognizer.recognize_google(audio, language='fr-FR')

                print(f"Vous avez dit : {text}")

                if text.lower().startswith("ouvre"):
                    if "ouvre youtube" in text.lower():
                        Script('openYoutube.sh')
                    elif "ouvre météo" in text.lower():
                        Script('openMeteo.sh')
                    elif "ouvre copilot" in text.lower():
                        Script('openCopilot.sh')
                elif text.lower().startswith("question"):
                    with open('./script/question.txt', 'w', encoding='utf-8') as fichier:
                        fichier.write(text)
                    Script('questionIA.sh')
                    with open("./script/reponse.txt", "r") as fichier:
                        reponse = fichier.read()
                    Reader(reponse)
                elif "ferme-toi" in text.lower():
                    program = False
                else:
                    Reader(f"Le mot {text} n'a pas été trouvé.")
                    print(f"Le mot {text} n'a pas été trouvé.")

            except sr.UnknownValueError:
                Reader(f"Je n'ai pas pu comprendre ce que vous avez dit.")
                print("Je n'ai pas pu comprendre ce que vous avez dit.")
            except sr.RequestError:
                print("Erreur de connexion.")

listen_for_test()