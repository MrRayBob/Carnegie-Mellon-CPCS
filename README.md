# CPCS

The following instructions to install and run work for any CPCS Creative Task.

## Apps

### Unit 3

- Creative Task #1 [Car Simulator](https://github.com/MrRayBob/Carnegie-Mellon-CPCS/blob/main/Car.py)
- Creative Task #1 [Solar System Simulator](https://github.com/MrRayBob/Carnegie-Mellon-CPCS/blob/main/Solar%20System.py)

## Prerequisites

- Python 3.8+ installed
- pip available

## Install requirements

Install the Python dependencies listed in `requirements.txt`:

```
python3 -m pip install -r requirements.txt
```

**Optional (recommended): create and activate a virtual environment first:**

```
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
```

## Run the apps

To run `Car.py`:

```
python3 Car.py
```

To run `Solar System.py` (note the space in the filename):

```
python3 "Solar System.py"
```

## Files

- `Car.py` — simple car simulator
- `Solar System.py` — solar system app showing inner planets at realistic velocities.
- `requirements.txt` — Python dependencies
