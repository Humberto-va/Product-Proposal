import subprocess
import sys

def run_git_command(command):
    """Helper function to run a git command in the terminal."""
    try:
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print(f"Command '{' '.join(command)}' executed successfully.")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr}")
        sys.exit(1)

def git_add():
    """Add all changes to staging area (including deletions)."""
    print("Running git add -A")
    run_git_command(["git", "add", "-A"])

def git_commit(commit_message):
    """Commit changes with a message."""
    print(f"Running git commit -m \"{commit_message}\"")
    run_git_command(["git", "commit", "-m", commit_message])

def git_push():
    """Push changes to the remote repository."""
    print("Running git push")
    run_git_command(["git", "push"])

def main():
    # Define the commit message
    commit_message = input("Enter the commit message: ")

    # Execute the git commands
    git_add()
    git_commit(commit_message)
    git_push()

if __name__ == "__main__":
    main()

      