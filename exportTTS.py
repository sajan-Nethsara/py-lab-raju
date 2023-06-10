import csv
from gtts import gTTS


def TextToSpeech(text, outputFile):
    tts = gTTS(text=text, lang='ko')
    tts.save(outputFile)
    print(f"{outputFile} successfully created.")


def printFunction(reader, _max):
    header = next(reader)
    Game = 0
    Sentences = 1
    for row in reader:
        dialogLine = int(row["conversation_id"])

        if dialogLine == 1:
            Game += 1
            Sentences = 1
            if Game == _max + 1:
                print("Done! all MP3 created")
                return
            fillName = f"MP3/G{Game}S{Sentences}.mp3"
            text = row['kor_sent']
            print("---")
            print(f"Generating {text}")
            TextToSpeech(text, fillName)
        else:

            Sentences += 1
            fillName = f"MP3/G{Game}S{Sentences}.mp3"
            text = row['kor_sent']
            print(f"Generating {text}")
            TextToSpeech(text, fillName)


def main():
    with open('conversations.csv', 'r', encoding='utf-8-sig') as data_file:
        reader = csv.DictReader(
            data_file, ["date", "conversation_id", "kor_sent", "eng_sent"])
        printFunction(reader, 20)


main()
