import playsound, pyttsx3, os

from threading import Thread
from gtts import gTTS


class TTS:
    """
    # NeoTTS
    - NeoTTS is an easy and comfortable voice conversion module designed for NEOEYES.
    """

    def __init__(self) -> None:
        self.sub_engine = pyttsx3.init()

    def __speak__(self, message: str) -> bool:
        """
        # __speak__
        - Voice conversion main engine (gTTS)

        Args:
            message (str): Enter the text that you want to convert to voice.
        """

        try:
            result = gTTS(text=message, lang="ko")
            result.save("tmp/speak.mp3")
            playsound.playsound("tmp/speak.mp3")
            os.remove("tmp/speak.mp3")
            return True
        except Exception as e:
            print("Failed to output audio to the main engine.\nAttempt to output to the sub engine.", e, sep="\n")
            return self.__sub_speak__(message)
    
    def __sub_speak__(self, message: str) -> bool:
        """
        # __sub_speak__
        - Voice conversion sub engine (pyttsx3)

        Args:
            message (str): Enter the text that you want to convert to voice.
        """

        try:
            self.sub_engine.say(message)
            self.sub_engine.runAndWait()
            return True
        except Exception as e:
            print("sub engine output failed.", e, sep="\n")
            return False

    def speak(self, message: str, thread: bool = True) -> None:
        """
        # speak
        - Voice conversion engine (gTTS, pyttsx3)

        Args:
            message (str): Enter the text that you want to convert to voice.
        """
        if thread:
            t = Thread(target=self.__speak__, args=(message, ), daemon=False)
            t.start()
        else:
            self.__speak__(message)