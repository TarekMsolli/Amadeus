import pyttsx3

def text_to_speech(text, voice_id=0):
    engine = pyttsx3.init()

    if voice_id:
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[voice_id].id)

    engine.say(text)
    engine.runAndWait()
    
def print_available_voices():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    for idx, voice in enumerate(voices):
        print(f"Voice {idx}: {voice.name}")