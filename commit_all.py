import os
import subprocess

# CONFIGURATION
BASE_DIR = os.getcwd()  # assuming you run script from repo root
IGNORE_FILES = ['tempCodeRunnerFile.py']
MONTH_EMOJI = "📂"
DAY_EMOJI = "📅"
PROBLEM_EMOJI = "📝"
SOLUTION_EMOJI = "💻"

# Helper to run git commands
def git(*args):
    return subprocess.run(['git'] + list(args), check=True)

# Commit a path with a message
def commit_path(path, message):
    git('add', path)
    git('commit', '-m', message)

# Traverse months
for month in sorted(os.listdir(BASE_DIR)):
    month_path = os.path.join(BASE_DIR, month)
    if not os.path.isdir(month_path) or month.startswith('.'):
        continue

    # Commit month folder
    commit_path(month_path, f"{MONTH_EMOJI} {month} Challenge")

    # Traverse days inside month
    for day in sorted(os.listdir(month_path)):
        day_path = os.path.join(month_path, day)
        if not os.path.isdir(day_path):
            continue

        # Commit day folder
        commit_path(day_path, f"{DAY_EMOJI} Day {day}")

        # Traverse problems inside day
        for problem in sorted(os.listdir(day_path)):
            problem_path = os.path.join(day_path, problem)
            if not os.path.isdir(problem_path):
                continue

            # Commit problem folder
            commit_path(problem_path, f"{PROBLEM_EMOJI} {problem} in {day}")

            # Commit solution files inside problem
            for file in sorted(os.listdir(problem_path)):
                file_path = os.path.join(problem_path, file)
                if not os.path.isfile(file_path) or file in IGNORE_FILES:
                    continue
                if file.endswith('.py'):
                    commit_path(file_path, f"{SOLUTION_EMOJI} Solution for {problem} on {day}")

# Push everything
git('push', 'origin', 'main')

print("✅ All commits pushed successfully!")