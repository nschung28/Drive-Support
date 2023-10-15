import speech_recognition as sr
import pyttsx3 
import numpy as np;
import librosa
import librosa.display
 
# Initialize the recognizer 
r = sr.Recognizer() 
 
def SpeakText(command):
    engine = pyttsx3.init()
    engine.say(command) 
    engine.runAndWait()

def is_whistling(sample_rate, audio_data): #tester will build off into sirens iff works

    audio_data = audio_data.astype(np.float32) / 32767.0

    mfccs = librosa.feature.mfcc(y = audio_data, sr = sample_rate, n_mfcc = 13)

    mean_mfccs = np.mean(mfccs, axis=1)
    print(mean_mfccs[1])
    low_pitch_threshold = 60 #may need to adjust here and line 20
    high_pitch_threshold = 15

    if low_pitch_threshold < mean_mfccs[1] < high_pitch_threshold:
        return True
    else:
        return False

while(True):    
     
    print("Listening")
    try:
         
        with sr.Microphone() as source2:
            
            r.adjust_for_ambient_noise(source2, duration=.75)
            audio = r.listen(source2)
            sample_rate = audio.sample_rate
        
        audio_data = np.frombuffer(audio.frame_data, dtype = np.int16)
        print(type(audio_data))

        if (is_whistling(sample_rate, audio_data)):
            print("WHISTLING")
        else:    
            MyText = r.recognize_google(audio)
            MyText = MyText.lower()
 
            print("Did you say ",MyText)
            SpeakText(MyText)
             
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
         
    except sr.UnknownValueError:
        print("unknown error occurred")