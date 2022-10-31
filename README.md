# Repro for podman socket issue

## Setup

```bash
python -m venv .venv # Assuming python3 is the default, but it should be!
source .venv/bin/activate
pip install -r requirements.txt
python main.py # Will fail as there is a second object
```
