import subprocess

def run_script(script_name):
    try:
        result = subprocess.run(["python", script_name], check=True, capture_output=True, text=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error running {script_name}:\n{e.stderr}")

if __name__ == "__main__":
    scripts = ["async_task.py", "multiprocessing_task.py", "threading_task.py"]
    for script in scripts:
        run_script(script)
