import os
import subprocess
import sys

bot_dir = os.path.dirname(os.path.abspath(__file__))
flags = 0x08000000 | 0x00000200  # CREATE_NO_WINDOW | CREATE_NEW_PROCESS_GROUP
python_bin = sys.executable

env = os.environ.copy()
if r"D:\tools\ffmpeg\bin" not in env.get("PATH", ""):
    env["PATH"] = r"D:\tools\ffmpeg\bin;" + env.get("PATH", "")

# Ensure any previously running main.py python processes are terminated to prevent 409 Conflict
try:
    import psutil
    for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
        pname = (proc.info.get('name') or '').lower()
        cmd = proc.info.get('cmdline') or []
        if 'python' in pname and any(c.strip().endswith('main.py') for c in cmd) and proc.pid != os.getpid():
            try:
                proc.kill()
            except Exception:
                pass
except Exception:
    subprocess.run(
        ["powershell", "-NoProfile", "-Command", "Get-CimInstance Win32_Process | Where-Object { $_.Name -like '*python*' -and $_.CommandLine -match '\\bmain\\.py\\b' } | ForEach-Object { Stop-Process -Id $_.ProcessId -Force -ErrorAction SilentlyContinue }"],
        capture_output=True,
    )

console_log = open(os.path.join(bot_dir, "bot_console.log"), "a", encoding="utf-8")

p = subprocess.Popen(
    [python_bin, "main.py"],
    cwd=bot_dir,
    env=env,
    stdin=subprocess.DEVNULL,
    stdout=console_log,
    stderr=console_log,
    creationflags=flags,
    close_fds=True,
)

with open(os.path.join(bot_dir, "aryafeed_bot.pid"), "w", encoding="utf-8") as f:
    f.write(str(p.pid))

print(f"AryaFeed Bot successfully detached with PID: {p.pid}")
