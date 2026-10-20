def validate_title(title):
    if not isinstance(title, str):
        return False
    title = title.strip()
    return 0 < len(title) <= 100

import subprocess

def run_cmd(cmd):
    return subprocess.call(cmd, shell=True)