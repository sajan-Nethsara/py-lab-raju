from gtts import gTTS

text = "아니요, 회사원이 아니에요. 의사예요."

# Create gTTS object and specify language
tts = gTTS(text=text, lang='ko')

# Save the generated speech as an MP3 file
output_file = "MP3/output.mp3"
tts.save(output_file)

print("MP3 file saved successfully.")

def TextToSpeach (text , outputFile):
    tts = gTTS(text=text, lang='ko')
    tts.save(outputFile)
    print(f"{outputFile} successfully saved.")