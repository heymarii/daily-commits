# 📅 Daily Commits

> Building the habit of shipping every day. This repo tracks my daily commit streak with scripts, tools, and notes for staying consistent.

## The Goal

A green square every day on my GitHub contribution graph. Not just for the aesthetic — for the discipline.

## What's in Here

```
daily-commits/
├── streak/          ← Daily log entries (one file per day)
├── scripts/         ← Automation scripts to help maintain the streak
├── github-actions/  ← Automated workflows
└── ideas/           ← Backlog of things to work on when I'm stuck
```

## Streak Rules (My Personal Rules)

1. At least **one meaningful commit** per day
2. "Meaningful" means: new content, a fixed bug, an improved doc — not just whitespace
3. Streak resets at midnight in my local timezone
4. Travel/vacation = write a TIL or update the ideas backlog

## Current Streak

Started: **March 27, 2026**  
Current streak: **1 day** 🔥  

*(Updated manually each week — or via the GitHub Actions workflow)*

---

## How to Use the Scripts

```bash
# Start your day — creates today's log file
python3 scripts/new-day.py

# Check your streak
python3 scripts/streak-check.py
```
