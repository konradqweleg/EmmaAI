from pathlib import Path
import sounddevice as sd
from scipy.io.wavfile import write



HOW_IS_LEARN_SET=6

SAMPLE_RATE = 44100  # Sample rate
DURATION_RECORD = 5  # Duration of recording




class Sound:
    def __init__(self,nameSound):
        self.__localeRecordLearnFolder=Path("Record\Sound"+nameSound+"\Learn\ ")
        self.__localeRecordTestFolder=Path("Record\Sound"+nameSound+"\Test\ ")
        self.__settingsRecordLearnSound=Path("StatisticsOfRecordSound"+"\Sound_"+nameSound+"\LearnSet.txt")
        self.__settingsRecordTestSound = Path("StatisticsOfRecordSound" + "\Sound_" + nameSound + "\TestSet.txt")
        self.__nameSound=nameSound


    @property
    def recordLaern(self):
        return self.__localeRecordLearnFolder

    @property
    def recordTest(self):
        return self.__localeRecordTestFolder

    @property
    def nameSound(self):
        return self.__nameSound

    def __addNewLearnRecord(self):
        learnFileNumberSoundRead=open(self.__settingsRecordLearnSound)
        counterSound=int(learnFileNumberSoundRead.readline())
        counterSound+=1
        learnFileNumberSoundRead.close()
        learnFileNumberSoundSave = open(self.__settingsRecordLearnSound,"w")
        learnFileNumberSoundSave.write(str(counterSound))
        learnFileNumberSoundSave.close()

        myrecording = sd.rec(int(DURATION_RECORD * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=2)
        sd.wait()
        write(str(self.__localeRecordLearnFolder)+str(counterSound)+".wav", SAMPLE_RATE, myrecording)

    def __addNewTestRecord(self):
        testFileNumberSoundRead = open(self.__settingsRecordTestSound)
        counterSound = int(testFileNumberSoundRead.readline())
        counterSound += 1
        testFileNumberSoundRead.close()
        testFileNumberSoundSave = open(self.__settingsRecordTestSound, "w")
        testFileNumberSoundSave.write(str(counterSound))
        testFileNumberSoundSave.close()

        myrecording = sd.rec(int(DURATION_RECORD * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=2)
        sd.wait()
        write(str(self.__localeRecordTestFolder)+str(counterSound) + ".wav", SAMPLE_RATE, myrecording)


    def __QuantitySoundRecord(self):
        learnFileNumberSoundRead = open(self.__settingsRecordLearnSound)
        counterSoundLearn = int(learnFileNumberSoundRead.readline())
        testFileNumberSoundRead = open(self.__settingsRecordTestSound)
        counterSoundTest = int(testFileNumberSoundRead.readline())
        testFileNumberSoundRead.close()
        learnFileNumberSoundRead.close()
        return counterSoundLearn,counterSoundTest



    def addNewRecord(self):
        howRecords=sum(self.__QuantitySoundRecord())

        if (howRecords %HOW_IS_LEARN_SET == 0 ):
            self.__addNewTestRecord()
        else:
            self.__addNewLearnRecord()


    def __str__(self):
        return "Ilość próbek dzwięku  "+self.__nameSound+"\n"+"Zbiór uczący   " + str(self.__QuantitySoundRecord()[0]) + "\n"+"Zbiór testowy  " +str( self.__QuantitySoundRecord()[1])+ "\n"




SOUND_RECORD = {
    "Emma":Sound("Emma"),
    "Pogoda": Sound("Pogoda")

}

