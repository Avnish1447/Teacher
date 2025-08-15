import os
import subprocess
import sys

# Emojis
SOLUTION_EMOJI = "💾"

# Get the root directory of the Git repository
try:
    ROOT_DIR = subprocess.check_output(['git', 'rev-parse', '--show-toplevel']).strip().decode('utf-8')
except subprocess.CalledProcessError:
    print("Error: This does not appear to be a git repository.")
    sys.exit(1)

# Ignore files and directories
# Using a set for efficient lookups
IGNORE_LIST = {".git", ".vscode", "commit_all.py", "tempCodeRunnerFile.py", ".DS_Store", ".gitignore"}

# Only commit these file types
COMMIT_FILE_EXTENSIONS = {".py", ".md", ".txt"}

def git(*args):
    """A simple wrapper for running a Git command."""
    return subprocess.run(['git'] + list(args), check=True, capture_output=True, text=True)

def commit_file(path):
    """Stages a single file and commits it if it has changes."""
    # Check for unstaged changes to this specific file
    status_result = git('status', '--porcelain', path)
    if not status_result.stdout.strip():
        print(f"No changes detected for {os.path.basename(path)}. Skipping.")
        return

    print(f"Staging {path}...")
    git('add', path)
    
    relative_path = os.path.relpath(path, ROOT_DIR)
    message = f"{SOLUTION_EMOJI} Add solution: {relative_path}"
    
    print(f"Committing with message: \"{message}\"")
    git('commit', '-m', message)

def main(push=False):
    """Walks the directory and commits each valid file individually."""
    # Walk through all directories and files starting from the root
    for root, dirs, files in os.walk(ROOT_DIR):
        # Modify dirs in-place to prevent os.walk from traversing ignored directories
        dirs[:] = [d for d in dirs if d not in IGNORE_LIST]
        
        for filename in sorted(files):
            if filename in IGNORE_LIST:
                continue

            _, ext = os.path.splitext(filename)
            if ext not in COMMIT_FILE_EXTENSIONS:
                continue

            file_path = os.path.join(root, filename)
            commit_file(file_path)

    if push:
        print("\nPushing all commits to remote...")
        try:
            git('push', 'origin', 'main')
            print("✅ Successfully pushed to origin main.")
        except subprocess.CalledProcessError as e:
            print(f"❌ Error during push: {e.stderr}")

if __name__ == "__main__":
    # Check if '--push' argument was passed
    push_flag = '--push' in sys.argv
    main(push=push_flag)