import sounddevice as sd
from scipy.io.wavfile import write
import Sound

SOUND_RECORD = {
    "Emma":Sound("Emma")

}




def recordSound__Emma():
    fileNumberActualSaveRecord=open(SOUND_RECORD["Emma_Settings"]+"\LearnSet.txt")
    print(fileNumberActualSaveRecord.readline())


recordSound__Emma()


#fs = 44100  # Sample rate
#seconds = 3  # Duration of recording

#myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
#sd.wait()  # Wait until recording is finished
#write('output.wav', fs, myrecording)  # Save as WAV file