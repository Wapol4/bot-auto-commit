import os
import random
import subprocess
import time
from datetime import datetime

# Folder project yang akan disimulasikan
PROJECT_DIRS = [
    "terraform",
    "kubernetes",
    "scripts",
    "docs",
]

FILES = {
    "terraform": ["main.tf", "variables.tf", "outputs.tf"],
    "kubernetes": ["deployment.yaml", "service.yaml"],
    "scripts": ["deploy.sh", "backup.sh"],
    "docs": ["infra.md", "notes.md"]
}

COMMIT_TYPES = ["feat", "fix", "docs", "refactor", "chore", "ci"]

MESSAGES = [
    "update configuration",
    "improve deployment",
    "cleanup scripts",
    "update documentation",
    "improve infrastructure",
    "optimize resource config",
    "fix minor issue",
]

def run(cmd):
    subprocess.run(cmd, shell=True, check=True)

def ensure_structure():
    for d in PROJECT_DIRS:
        os.makedirs(d, exist_ok=True)

def random_file_update():
    folder = random.choice(PROJECT_DIRS)
    file = random.choice(FILES[folder])

    path = f"{folder}/{file}"

    if not os.path.exists(path):
        open(path, "w").close()

    with open(path, "a") as f:
        f.write(f"# update {datetime.now()}\n")

def generate_commit_message():
    ctype = random.choice(COMMIT_TYPES)
    scope = random.choice(PROJECT_DIRS)
    msg = random.choice(MESSAGES)

    return f"{ctype}({scope}): {msg}"

def git_commit():
    msg = generate_commit_message()

    run("git add .")

    try:
        run(f'git commit -m "{msg}"')
        run("git push origin main")
    except:
        pass

def simulate_dev_activity():

    commits = random.randint(1, 6)

    print(f"Simulating {commits} commits today")

    for _ in range(commits):

        random_file_update()
        git_commit()

        sleep_time = random.randint(30, 300)
        time.sleep(sleep_time)

def skip_weekend():
    day = datetime.today().weekday()

    # 5 = Saturday, 6 = Sunday
    return day in [5, 6]

def main():

    if skip_weekend():
        print("Weekend detected, skipping commits")
        return

    ensure_structure()

    simulate_dev_activity()

if __name__ == "__main__":
    main()