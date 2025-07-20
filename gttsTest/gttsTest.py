from gtts import gTTS

tts = gTTS('Ich habe keine Zeit. Entschuldigung!', lang='de')
tts.save('hello.mp3')