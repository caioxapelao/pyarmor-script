from pyfiglet import figlet_format
from pystyle import System, Colorate, Colors
import subprocess
import msvcrt
logo = figlet_format("PyArmor Obfuscator")
print(Colorate.Vertical(Colors.rainbow, logo))
for i in range(5):
    print()
file_path = input(Colorate.Horizontal(Colors.cyan_to_green, "[+] Drag ur Python file -> "))
System.Clear()
pyarmor_logs = subprocess.run(["pyarmor", "gen", file_path.replace('"', '')], capture_output=True, text=True)
for line in pyarmor_logs.stderr.splitlines():
    line = line[9:]
    line_upd = "[+] " + line
    print(Colorate.Horizontal(Colors.rainbow, line_upd))
print(Colorate.Horizontal(Colors.red_to_blue, "[+] Done Obfuscating"))
msvcrt.getch()