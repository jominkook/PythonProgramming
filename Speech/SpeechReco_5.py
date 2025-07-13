import speech_recognition as sr

recognizer = sr.Recognizer()
with sr.Microphone() as source:
    print("음성을 입력하세요:")
    audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio, language="ko-KR")
        print("인식 결과:", text)
    except sr.UnknownValueError:
        print("음성을 인식하지 못했습니다.")
    except sr.RequestError:
        print("API 요청 실패")