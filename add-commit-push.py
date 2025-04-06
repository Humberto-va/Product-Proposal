import subprocess
import sys

def run_git_command(command):
    """Executes a git command, prints the command, and displays the results."""
    print(f"Running: {' '.join(command)}\n")
    result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    print(f"Result:\n{result.stdout}\n")
    return result.stdout

def git_status():
    """Prints the results of git status."""
    print("Running git status...")
    status = run_git_command(["git", "status"])
    print(f"git status:\n{status}")

def git_add():
    """Add all changes to staging area (including deletions)."""
    print("Queueing: git add -A")
    return ["git", "add", "-A"]

def git_commit(commit_message):
    """Queue a commit command."""
    print(f"Queueing: git commit -m \"{commit_message}\"")
    return ["git", "commit", "-m", commit_message]

def git_push():
    """Queue a push command."""
    print("Queueing: git push")
    return ["git", "push"]

def print_and_execute(command):
    """Print and execute a git command, then display its results."""
    print(f"Command to execute: {' '.join(command)}")
    result = run_git_command(command)
    return result

def main():
    # Step 1: Print the git status
    git_status()

    # Step 2: Queue the git commands
    commit_message = input("Enter the commit message: ")
    add_command = git_add()
    commit_command = git_commit(commit_message)
    push_command = git_push()

    # Step 3: Confirm with the user to execute or skip
    force_flag = "-f" in sys.argv  # Check if -f (force) flag is passed

    if force_flag or input(f"Do you want to proceed with these commands? (y/n): ").lower() == 'y':
        print_and_execute(add_command)
        print_and_execute(commit_command)
        print_and_execute(push_command)
    else:
        print("Operation aborted.")
        sys.exit(0)

if __name__ == "__main__":
    main()
