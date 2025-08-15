import os
import subprocess

# Root path of your repo
repo_root = os.path.abspath(".")

# Define month folders
months = ["07", "08"]

# Files to ignore
ignore_files = ["tempCodeRunnerFile.py"]
ignore_extensions = [".png", ".jpg", ".jpeg"]

def git_add_commit(path, message):
    subprocess.run(["git", "add", path])
    subprocess.run(["git", "commit", "-m", message])

day_counter = 1

for month in months:
    month_path = os.path.join(repo_root, month)
    if not os.path.exists(month_path):
        continue
    
    # Commit month folder
    git_add_commit(month_path, f"📆 {month} Challenge")

    # Traverse day folders inside month
    for day_folder in sorted(os.listdir(month_path)):
        day_path = os.path.join(month_path, day_folder)
        if not os.path.isdir(day_path):
            continue

        # Commit day folder
        git_add_commit(day_path, f"🗓️ Day {day_counter} — {day_folder}")

        # Traverse problem folders
        for problem_folder in sorted(os.listdir(day_path)):
            problem_path = os.path.join(day_path, problem_folder)
            if not os.path.isdir(problem_path):
                continue

            # Commit problem folder
            git_add_commit(problem_path, f"📂 {problem_folder}")

            # Commit solution.py files inside problem folder
            for file in os.listdir(problem_path):
                file_path = os.path.join(problem_path, file)
                if file in ignore_files or os.path.splitext(file)[1] in ignore_extensions:
                    continue
                if file.endswith(".py"):
                    git_add_commit(file_path, f"💻 Solution for Day {day_counter} — {problem_folder}")

        day_counter += 1

print("All commits done! You can now push using 'git push origin main'")