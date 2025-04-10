import speech_recognition as sr
import subprocess


def script(scriptSh):
    subprocess.run(['bash', './script/' + scriptSh], check=True)

recognizer = sr.Recognizer()

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

                if "ouvre youtube" in text.lower():
                    script('openYoutube.sh')
                elif "ouvre météo" in text.lower():
                    script('openMeteo.sh')
                elif "ouvre copilot" in text.lower():
                    script('openCopilot.sh')
                elif "ferme-toi" in text.lower():
                    program = False
                else:
                    print(f"Le mot {text} n'a pas été trouvé.")

            except sr.UnknownValueError:
                print("Je n'ai pas pu comprendre ce que vous avez dit.")
            except sr.RequestError:
                print("Erreur de connexion.")

listen_for_test()