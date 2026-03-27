# Scripts

Automation helpers to support the daily commit habit.

## Scripts

### `new-day.py`
Creates a new day log file in `streak/YYYY/MM/` with today's date. Run it each morning.

```bash
python3 scripts/new-day.py
```

### `streak-check.py`  
Reads the streak log and reports your current streak length.

```bash
python3 scripts/streak-check.py
```

### `commit-helper.sh`
Quick commit + push shortcut. Add a message and it stages, commits, and pushes.

```bash
./scripts/commit-helper.sh "Add TIL on Python decorators"
```
