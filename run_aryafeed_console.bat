@echo off
title AryaFeed Engine Bot (@aryafeed_engine_bot)
set "PATH=D:\tools\ffmpeg\bin;%LOCALAPPDATA%\Programs\Python\Python312;%LOCALAPPDATA%\Programs\Python\Python312\Scripts;%PATH%"
cd /d "D:\aryafeed bot"
echo ========================================================
echo   Starting AryaFeed Engine Bot (@aryafeed_engine_bot)
echo   Connected to: @aryafeed.in (Viral News / Cards / Reels)
echo   Press Ctrl+C to stop.
echo ========================================================
"%LOCALAPPDATA%\Programs\Python\Python312\python.exe" main.py
pause
