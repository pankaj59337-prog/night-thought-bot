@echo off
powershell -NoProfile -Command "Get-CimInstance Win32_Process | Where-Object { $_.CommandLine -like '*instagram bot*main.py*' } | ForEach-Object { Stop-Process -Id $_.ProcessId -Force; Write-Host ('Stopped Night Bot PID: ' + $_.ProcessId) }"
echo Night Thought Bot stopped cleanly!
ping 127.0.0.1 -n 2 >nul
