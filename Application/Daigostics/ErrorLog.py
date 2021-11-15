from datetime import *

now = datetime.now()

CurDate = date.today()

CurTime = now.strftime("%H:%M:%S")

def openLogFile():
    global LogFile
    LogFile=open("Resources/App/Logs/errorLogFile.log","a")

def closeLogFile():
    LogFile.close()
    
def createLog(type='Not Specified',Log='Unexpected System Brick and Stop.'):

    openLogFile()

    LogFile.write("{}, {} , {} , {}\n".format(CurDate,CurTime,type,Log))
    
    closeLogFile()

createLog()
