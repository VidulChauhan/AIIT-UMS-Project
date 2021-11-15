from datetime import *

now = datetime.now()

CurDate = date.today()

CurTime = now.strftime("%H:%M:%S")

def openLogFile():
    global LogFile
    LogFile=open("Resources/App/Logs/errorLogFile.log","a")

def closeLogFile():
    LogFile.close()
    
def createLog(type='App Executed',Log='Proceeding to Start Screen.'):

    openLogFile()

    LogFile.write("{}, {} , {} , {}\n".format(CurDate,CurTime,type,Log))
    
    closeLogFile()
