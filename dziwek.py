import sounddevice as sd
from scipy.io.wavfile import write
import Sounds

SOUND_RECORD = {
    "Emma":Sounds.Sound("Emma")

}




#def recordSound(nameSound):
   # fileNumberActualSaveRecord=open(SOUND_RECORD
  #  print(fileNumberActualSaveRecord.readline())




sounde = SOUND_RECORD["Emma"]
sounde.addNewRecord()
print(sounde)

#recordSound__Emma()


#fs = 44100  # Sample rate
#seconds = 3  # Duration of recording

#myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
#sd.wait()  # Wait until recording is finished
#write('output.wav', fs, myrecording)  # Save as WAV file