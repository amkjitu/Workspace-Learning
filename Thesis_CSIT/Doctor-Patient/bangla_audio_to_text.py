from banglaspeech2text import Speech2Text

stt = Speech2Text(model="base")

# You can use it wihout specifying model name (default model is "base")
stt = Speech2Text()

transcription = stt.recognize("C:/Users/HP 840 G1/Documents/VS Code Projects/Workspace Learning/Thesis_CSIT/Doctor-Patient/Shomoy News Bangla 2 person.wav")
print(transcription)