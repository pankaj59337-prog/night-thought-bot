@echo off
set "PATH=D:\tools\ffmpeg\bin;%LOCALAPPDATA%\Programs\Python\Python312;%PATH%"
cd /d "D:\aryafeed bot"
"%LOCALAPPDATA%\Programs\Python\Python312\python.exe" start_bot.py
echo AryaFeed Bot started in background!
ping 127.0.0.1 -n 2 >nul
