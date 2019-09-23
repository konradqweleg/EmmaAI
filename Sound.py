from pathlib import Path



class Sound:
    def __init__(self,nameSound):
        self.localeRecordLearnFolder=Path("Record\Sound"+nameSound+"\Learn")
        self.localeRecordTestFolder=Path("Record\Sound"+nameSound+"\Test")
        self.settingsRecordLearnSound=Path("StatisticsOfRecordSound"+"\Sound_"+nameSound+"\LernSet.txt")
        self.settingsRecordTestSound = Path("StatisticsOfRecordSound" + "\Sound_" + nameSound + "\TestSet.txt")
        self.nameSound=nameSound