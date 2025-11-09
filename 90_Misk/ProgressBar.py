import time
import sys
from rich.progress import Progress

def progress_bar(progress, total, color='\033[92m'):  # 92 = 緑
    bar_length = 40
    percent = progress / total
    filled = int(bar_length * percent)
    bar = '█' * filled + '-' * (bar_length - filled)
    sys.stdout.write(f'\r{color}|{bar}| {percent*100:5.1f}%\033[0m')
    sys.stdout.flush()

for i in range(101):
    progress_bar(i, 100)
    time.sleep(0.03)

with Progress() as progress:
    task = progress.add_task("[cyan]Installing modules...", total=100)
    for i in range(100):
        time.sleep(0.03)
        progress.update(task, advance=1)
