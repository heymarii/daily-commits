#!/usr/bin/env python3
"""
new-day.py — Creates today's streak log file with a template.
Run this each morning before you start work.
"""

import os
from datetime import datetime

today = datetime.now()
year = today.strftime("%Y")
month = today.strftime("%m")
date_str = today.strftime("%Y-%m-%d")
day_num = today.strftime("%B %d, %Y")

# Create directory
dir_path = f"streak/{year}/{month}"
os.makedirs(dir_path, exist_ok=True)

file_path = f"{dir_path}/{date_str}.md"

if os.path.exists(file_path):
    print(f"Today's log already exists: {file_path}")
else:
    template = f"""# {day_num}

**Streak:** ? days  
**Mood:** ...  
**Time committed:** ...

## What I Did Today

- 

## What I Learned

## Tomorrow's Plan

- 

---

*One day at a time.*
"""
    with open(file_path, "w") as f:
        f.write(template)
    print(f"Created: {file_path}")
    print("Now open it, fill it in, and commit!")
