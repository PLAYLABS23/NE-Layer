import speech_recognition as stt

class STT:
    def __init__(self, device_index: int = 0) -> None:
        self.Recognizer = stt.Recognizer()
        self.mic = stt.Microphone(device_index=device_index)

    def listen(self, timeout: int = 4, phrase_time_limit: int = 8) -> str:
        try:
            with self.mic as source:
                self.Recognizer.adjust_for_ambient_noise(source)
                audio = self.Recognizer.listen(source, timeout=timeout, phrase_time_limit = 10)
                result = self.Recognizer.recognize_google(audio, language='ko-KR')
                return result
        except Exception as e:
            print("Failed to listen")
            return ""