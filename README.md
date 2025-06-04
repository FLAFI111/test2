# BestApp - Simple TODO Manager

This repository contains a small command line TODO manager written in Python.

## Usage

```
# Add a new task
python -m bestapp.cli add "Buy milk"

# List tasks
python -m bestapp.cli list

# Mark task as done (task numbering starts at 1)
python -m bestapp.cli done 1

# Remove a task
python -m bestapp.cli remove 1
```

Tasks are stored in `tasks.json` in the current directory.

## Running Tests

```
pytest -q
```
