import speech_recognition as sr
import pyttsx3 
import numpy as np;
import librosa
import librosa.display
 

r = sr.Recognizer() 
 
def SpeakText(command):
    engine = pyttsx3.init()
    engine.say(command) 
    engine.runAndWait()

# def is_(sample_rate, audio_data): #tester will build off into sirens iff works
#     audio_data = audio_data.astype(np.float32) / 32767.0

#     fft_result = np.fft.fft(audio_data)
#     frequencies = np.fft.fftfreq(len(fft_result), 1 / sample_rate)
#     curr_frequency = np.abs(frequencies[np.argmax(np.abs(fft_result))])

#     print(curr_frequency)

#     low_freq = 1000  # Adjust this value based on your use case
#     high_freq = 3500  # Adjust this value based on your use case

#     if low_freq < curr_frequency < high_freq:
#         return True
#     else:
#         return False
    
def is_siren(sample_rate, audio_data): #tester will build off into sirens iff works
    audio_data = audio_data.astype(np.float32) / 32767.0

    frequencies = np.fft.fftfreq(len(np.fft.fft(audio_data)), 1 / sample_rate)
    curr_frequency = np.abs(frequencies[np.argmax(np.abs(np.fft.fft(audio_data)))])

    print(curr_frequency)

    low_freq = 1000  # Adjust this value based on your use case
    high_freq = 3000  # Adjust this value based on your use case

    if low_freq < curr_frequency < high_freq:
        return True
    else:
        return False
    
def is_honk(sample_rate, audio_data): #tester will build off into sirens iff works
    audio_data = audio_data.astype(np.float32) / 32767.0

    frequencies = np.fft.fftfreq(len(np.fft.fft(audio_data)), 1 / sample_rate)
    curr_frequency = np.abs(frequencies[np.argmax(np.abs(np.fft.fft(audio_data)))])

    print(curr_frequency)

    low_freq = 600  # Adjust this value based on your use case
    high_freq = 900  # Adjust this value based on your use case

    if low_freq < curr_frequency < high_freq:
        return True
    else:
        return False

while(True):    
     
    print("Listening")
    try:
         
        with sr.Microphone() as source2:
            
            r.adjust_for_ambient_noise(source2, duration=.4)
            audio = r.listen(source2)
            sample_rate = audio.sample_rate
        
        audio_data = np.frombuffer(audio.frame_data, dtype = np.int16)

        if (is_siren(sample_rate, audio_data)):
            print("SIREN DETECTED")
        elif (is_honk(sample_rate, audio_data)) :
            print("HONK DETECTED")
        else:    
            print("SPEECH DETECTED")
             
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
         
    except sr.UnknownValueError: #weird sound
        print("sound not detected")