# ISM2411 — Python for Business

**Name:** Talmer Brown

**Semester:** Fall 2026

## About This Repo

This repository contains my weekly lab submissions for ISM2411.
Each weekly folder holds the work for the corresponding module.

## Modules

- `week07/` — Functions: `calculate_tax`, `apply_discount`, and `final_price`, with examples of order processing, debugging, and scope.
- Module 8 — Git and GitHub: repository setup, `.gitignore`, commits, documentation, and reflection.

## How to Run

From the repository root, run the Module 7 script with Python 3:

```bash
python3 week07/functions.py
```

The script prints tax calculations, tiered discounts, final order prices, sales totals, and scope examples.

## Reflection

### 1. Commit history and what it communicates

The following is the output of `git log --oneline` after the three main lab changes, before adding this reflection:

```text
db27d68 add README with module listing and run instructions
64654af add module 7 functions: calculate_tax, apply_discount, final_price
aec902d add .gitignore for Python and OS files
450b27e Initial commit
```

To a hiring manager, this history would show that I organize changes into focused steps and use descriptive messages to explain their purpose. Separating the ignore rules, Python script, and documentation makes the work easier to review and gives each change a clear place in the project's history.

### 2. How Git changes my editing process

Using Git encourages me to make one focused change at a time, run the script to check the result, and review the difference before committing. Instead of mixing several edits into one large update, I would save small working checkpoints with descriptive messages so I can compare versions or recover an earlier version if something breaks.

### 3. An additional ignore rule

I added `.venv/` for a local Python virtual environment. It contains installed packages and files tied to the local Python setup, which can be large and vary between computers; those files should be recreated locally rather than tracked with the source code.
