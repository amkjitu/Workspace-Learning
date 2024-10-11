#######eta audio file er duration onujayi prokash kore
# import librosa
# import pydub
# from pydub.playback import play
# from pydub.utils import make_chunks
# from pyAudioAnalysis import audioSegmentation
# from pyAudioAnalysis.audioSegmentation import speaker_diarization
# import numpy as np

# # Step 1: Load the audio file
# audio_file = "C:/Users/HP 840 G1/Documents/VS Code Projects/Workspace Learning/Thesis_CSIT/Doctor-Patient/M_0025_11y10m_1.wav"
# audio = pydub.AudioSegment.from_wav(audio_file)

# # Step 2: Split the audio into smaller chunks
# chunk_length_ms = 10000  # 10 seconds
# chunks = make_chunks(audio, chunk_length_ms)

# # Step 3: Speaker Diarization
# diarized_segments = []
# for i, chunk in enumerate(chunks):
#     chunk.export(f"chunk_{i}.wav", format="wav")  # Export each chunk to a WAV file
#     cls, _, _ = speaker_diarization(f"chunk_{i}.wav", n_speakers=2, mid_window=1.0, mid_step=0.1, short_window=0.1, lda_dim=0, plot_res=False)  # Corrected the arguments
#     diarized_segments.append((i, cls))

# # Step 4: Convert to Dialogue
# dialogue = {}
# for i, cls in diarized_segments:
#     speakers = np.unique(cls)
#     for speaker in speakers:
#         if speaker not in dialogue:
#             dialogue[speaker] = []
#         speaker_segments = [j for j, speaker_id in enumerate(cls) if speaker_id == speaker]
#         for seg_index in speaker_segments:
#             start_time = seg_index * chunk_length_ms / 1000
#             end_time = (seg_index + 1) * chunk_length_ms / 1000
#             dialogue[speaker].append((start_time, end_time))

# # Generate dialogue text
# all_segments = [(start, end, speaker) for speaker, segments in dialogue.items() for start, end in segments]
# all_segments.sort(key=lambda x: x[0])  # Sort all segments based on their start time

# dialogue_text = ""
# current_speaker = None
# for start_time, end_time, speaker in all_segments:
#     if speaker != current_speaker:
#         dialogue_text += f"\nSpeaker {speaker}:\n"
#         current_speaker = speaker
#     dialogue_text += f" - Segment from {start_time} to {end_time}\n"

# # Print or save dialogue text
# print(dialogue_text)
# #------------------------------------------------

################ Speaker not showing
import pydub
from pydub.utils import make_chunks
from pyAudioAnalysis.audioSegmentation import speaker_diarization
import speech_recognition as sr
from speech_recognition import UnknownValueError
import numpy as np
import librosa

# Function to extract MFCC features from an audio file
def extract_features(audio_file):
    # Load the audio file
    audio_data, sample_rate = librosa.load(audio_file, sr=None)
    
    # Extract MFCC features
    mfccs = librosa.feature.mfcc(y=audio_data, sr=sample_rate, n_mfcc=13)
    
    # Transpose the MFCC matrix
    mfccs = mfccs.T
    
    return mfccs

# Load the audio file
#audio_file = "C:/Users/HP 840 G1/Documents/VS Code Projects/Workspace Learning/Thesis_CSIT/Doctor-Patient/Shomoy News Bangla 2 person.wav"

audio_file = "C:/Users/HP 840 G1/Documents/VS Code Projects/Workspace Learning/Thesis_CSIT/Doctor-Patient/M_0025_11y10m_1.wav"

audio = pydub.AudioSegment.from_wav(audio_file)

# Split the audio into smaller chunks
chunk_length_ms = 10000  # 10 seconds
chunks = make_chunks(audio, chunk_length_ms)

# Speaker Diarization
diarized_segments = []
for i, chunk in enumerate(chunks):
    chunk.export(f"chunk_{i}.wav", format="wav")  # Export each chunk to a WAV file
    cls, _, _ = speaker_diarization(f"chunk_{i}.wav", n_speakers=2, mid_window=1.0, mid_step=0.1, short_window=0.1, lda_dim=0, plot_res=False)
    diarized_segments.append((i, cls))  # Store the segment index and speaker labels

# Organize segments in chronological order
diarized_segments.sort(key=lambda x: x[0])

# Extract text using Speech Recognition
r = sr.Recognizer()
dialogue_text = ""
for segment_index, cls in diarized_segments:
    speaker = str(cls)  # Convert speaker labels to string
    with sr.AudioFile(f"chunk_{segment_index}.wav") as source:
        try:
            audio_data = r.record(source)  # Read the entire audio file
            text = r.recognize_google(audio_data)  # Use Google Speech Recognition to convert speech to text
            dialogue_text += f"\nSpeaker {speaker}:\n{text}\n"
        except UnknownValueError:
            dialogue_text += f"\nSpeaker {speaker}:\n[Unable to recognize speech]\n"

# Print or save dialogue text
print(dialogue_text)



# import pydub
# from pydub.utils import make_chunks
# from pyAudioAnalysis.audioSegmentation import speaker_diarization
# import speech_recognition as sr
# from speech_recognition import UnknownValueError
# import numpy as np
# import librosa

# # Function to extract MFCC features from an audio file
# def extract_features(audio_file):
#     # Load the audio file
#     audio_data, sample_rate = librosa.load(audio_file, sr=None)
    
#     # Extract MFCC features
#     mfccs = librosa.feature.mfcc(y=audio_data, sr=sample_rate, n_mfcc=13)
    
#     # Transpose the MFCC matrix
#     mfccs = mfccs.T
    
#     return mfccs

# # Load the audio file
# audio_file = "C:/Users/HP 840 G1/Documents/VS Code Projects/Workspace Learning/Thesis_CSIT/Doctor-Patient/Shomoy News Bangla 2 person.wav"
# audio = pydub.AudioSegment.from_wav(audio_file)

# # Split the audio into smaller chunks
# chunk_length_ms = 10000  # 10 seconds
# chunks = make_chunks(audio, chunk_length_ms)

# # Speaker Diarization
# diarized_segments = []
# for i, chunk in enumerate(chunks):
#     chunk.export(f"chunk_{i}.wav", format="wav")  # Export each chunk to a WAV file
#     cls, _, _ = speaker_diarization(f"chunk_{i}.wav", n_speakers=2, mid_window=1.0, mid_step=0.1, short_window=0.1, lda_dim=0, plot_res=False)
#     diarized_segments.append((i, cls))  # Store the segment index and speaker labels

# # Organize segments in chronological order
# diarized_segments.sort(key=lambda x: x[0])

# # Extract text using Speech Recognition
# r = sr.Recognizer()
# dialogue_text = ""
# current_speaker = None
# for segment_index, cls in diarized_segments:
#     speaker = cls[0]  # Get the speaker label for the first segment
#     if speaker != current_speaker:
#         if current_speaker is not None:
#             dialogue_text += "\n"  # Add a new line between speaker segments
#         dialogue_text += f"Speaker {speaker}:\n"
#         current_speaker = speaker
    
#     with sr.AudioFile(f"chunk_{segment_index}.wav") as source:
#         try:
#             audio_data = r.record(source)  # Read the entire audio file
#             text = r.recognize_google(audio_data)  # Use Google Speech Recognition to convert speech to text
#             dialogue_text += f"{text}\n"
#         except UnknownValueError:
#             dialogue_text += "[Unable to recognize speech]\n"

# # Print or save dialogue text
# print(dialogue_text)

