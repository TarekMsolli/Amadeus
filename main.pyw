import time
from text_to_speech import text_to_speech
from katakana_mentor import KatakanaMentorManager
import threading

def mentor_display_loop(mentor_manager):
    while True:
        katakana_mentor_thread = threading.Thread(target=mentor_manager.show_random_katakana_mentor)
        katakana_mentor_thread.start()
        time.sleep(60 * 5)

def main():
    time.sleep(30)

    voice_id = 0
    text_to_speech("Welcome, User", voice_id=voice_id)

    threading.Thread(target=mentor_display_loop(KatakanaMentorManager())).start()

if __name__ == "__main__":
    main()


