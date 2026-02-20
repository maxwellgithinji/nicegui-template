# NiceGUI App

A cross-platform NiceGUI application that runs on both Windows and Ubuntu.

## Layout

```
┌─────────────────────────────────────────┐
│              Page Title                 │
│                                         │
│  ┌──────────────┐  ┌──────────────────┐ │
│  │    Form      │  │    Actions       │ │
│  │              │  │  [ Action 1    ] │ │
│  │  Name ____   │  │  [ Action 2    ] │ │
│  │  Email ___   │  └──────────────────┘ │
│  │  Note ____   │  ┌──────────────────┐ │
│  │              │  │   Action Log     │ │
│  └──────────────┘  │  [12:00] entry   │ │
│                    └──────────────────┘ │
└─────────────────────────────────────────┘
```

## Setup

### Ubuntu / macOS

```bash
# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run
python main.py
```

### Windows

```powershell
# Create virtual environment
python -m venv .venv
.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run
python main.py
```

## Usage

Open your browser at **http://localhost:8080**

- Fill in the **Name**, **Email**, and **Note** fields in the Form.
- Click **Action 1** to log the current form values to the Action Log.
- Click **Action 2 — Clear** to reset all form fields.
- The **Action Log** panel records every action with a timestamp.
