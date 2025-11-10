import time
import sys
from rich.progress import Progress
from rich.console import Console
from rich.markdown import Markdown
from tqdm import tqdm
from alive_progress import alive_bar


# ──────────────── 各種進捗バー関数 ────────────────
def custom_progress_bar():
    """ANSIカラーで作ったシンプルな進捗バー"""
    for i in range(101):
        bar_length = 40
        percent = i / 100
        filled = int(bar_length * percent)
        bar = '█' * filled + '-' * (bar_length - filled)
        sys.stdout.write(f'\r\033[92m|{bar}| {percent*100:5.1f}%\033[0m')
        sys.stdout.flush()
        time.sleep(0.03)
    print()  # 改行


def rich_progress_bar():
    """Richライブラリの進捗バー"""
    with Progress() as progress:
        task = progress.add_task("[cyan]Installing modules...", total=100)
        for i in range(100):
            time.sleep(0.03)
            progress.update(task, advance=1)


def tqdm_progress_bar():
    """tqdmライブラリの進捗バー"""
    for _ in tqdm(range(100), desc="Loading...", ncols=80):
        time.sleep(0.03)


def alive_progress_bar():
    """alive-progressライブラリの進捗バー"""
    with alive_bar(100, bar='checks', spinner='pulse') as bar:
        for _ in range(100):
            time.sleep(0.03)
            bar()

# ──────────────── メイン関数 ────────────────


def main():
    console = Console()
    with console.status("[bold green]Now Loading...") as status:
        time.sleep(1)

    title = """# Hello, World!"""
    markdown = Markdown(title)
    console.print(markdown)

    print()

    print("\n[1/4] Custom progress bar:")
    custom_progress_bar()

    print("\n[2/4] Rich progress bar:")
    rich_progress_bar()

    print("\n[3/4] tqdm progress bar:")
    tqdm_progress_bar()

    print("\n[4/4] Alive progress bar:")
    alive_progress_bar()

    print("\n✅ All progress bars completed!")


# ──────────────── 実行部 ────────────────
if __name__ == "__main__":
    main()
