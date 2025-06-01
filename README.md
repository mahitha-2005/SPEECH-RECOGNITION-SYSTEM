## SPEECH-RECOGNITION-SYSTEM

"COMPANY":CODETECH IT SOLUTIONS

"NAME":THUMATI MAHITHA

"INTERN ID":CT04DL756

"DOMAIN NAME ":ARTIFICIAL INTELLIGENCE

"DURATION":4 WEEKS

"MENTOR":NEELA SANTHOSH KUMAR

## I AM DONE WITH THE SPEECH RECOGNITION SYSTEM.THE IMPORTANT LIBRARIES AND THEIR PURPOSES ARE:
 `speech_recognition` : Core library to convert speech to text   
 `sr.Recognizer()`    : Loads and processes audio                
 `recognize_google()` : Uses Google’s API for speech recognition 
## Functionality:
The script takes an audio file (e.g., .wav) as input and converts the spoken words into text using the Google Web Speech API.
## Workflow:
User Input: Prompt user to enter the path of a short audio file.

Audio Loading: Load the file using speech_recognition.AudioFile().

Speech Recognition:

Use the recognizer to record the audio.

Call recognize_google() to transcribe the audio into text.

Output: Print the recognized text or display an error if transcription fails.
## OUTPUT:

Listening...
Transcribing...
Transcription:
Hello, welcome to the speech recognition system.
