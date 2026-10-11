Set WshShell = CreateObject("WScript.Shell")
WshShell.CurrentDirectory = "D:\instagram bot"
WshShell.Run """C:\Python314\pythonw.exe"" main.py", 0, False
