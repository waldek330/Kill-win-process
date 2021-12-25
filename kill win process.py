from subprocess import call
import time
import ctypes, sys

ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)

time.sleep(2)
unwanted_process = ["Win32Bridge.Server.exe", "HxCalendarAppImm.exe", "HxTsr.exe", "HxOutlook","Microsoft.Photos.exe", "TiWorker.exe"]
for process in unwanted_process:
    call(['TASKKILL', '/F', '/IM', f'{process}'])
    time.sleep(1)