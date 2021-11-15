import os
from win10toast import ToastNotifier
nt=ToastNotifier()

try:
    def conn():
        os.system('cmd/c "pip install mysql-connector-python"')
    def twil():
        os.system('cmd/c "pip install twilio"')
    conn()
    twil()
except:
    print('Error.......')
else:
    nt.show_toast("AIIT ERP","External modules are installed successfully.",duration=5,icon_path="Nicon.ico")
