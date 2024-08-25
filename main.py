import os, playsound

from threading import Thread
from time import sleep as delay

from util.TTS import TTS
from util.STT import STT
from util.API import LMM

from secret import OPENAI_API_KEY


tts = TTS()
stt = STT(device_index=0)
lmm = LMM(api_key=OPENAI_API_KEY)

call_sign = [["화해", "Hi", "하이", "파이", "싸이", "소리", "카이"], ["내용", "네", "메모"]]
enable_listen = True


def main():
    if not os.path.isdir('tmp'): os.makedirs('tmp')
    
    t = Thread(target=always_listen, daemon=True)
    t.start()

def always_listen():
    global enable_listen

    while True:
        if enable_listen:
            print("call sign listening...")
            query = stt.listen(timeout=4, phrase_time_limit=4)

            query_tmp = query.replace(" ", "")
            print(query_tmp)

            for sign_i in call_sign[0]:
                if sign_i in query_tmp:
                    for sign_j in call_sign[1]:
                        if sign_j in query_tmp:
                            enable_listen = False
                            request()
        else:
            print("waiting...")

def __request_feedback__():
    playsound.playsound("res/call.mp3")

def request():
    global enable_listen
    t = Thread(target=__request_feedback__)
    t.start()

    print("request listening...")
    query = stt.listen(phrase_time_limit=15)
    if query:
        playsound.playsound("res/think.mp3")
        result = lmm.text_request(query)
        print("result :", result)
        tts.speak(result, thread=False)
        enable_listen = True
    else:
        request()

if __name__ == '__main__':
    main()
    while True: pass