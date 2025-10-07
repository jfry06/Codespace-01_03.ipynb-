# Python Virtual Environment Setup

To create and activate a Python virtual environment for this project:

## 1. Create the virtual environment

```bash
python -m venv .venv
```

## 2. Activate the environment (every new terminal session)

- **macOS / Linux:**
  ```bash
  source .venv/bin/activate
  ```

- **Windows CMD:**
  ```cmd
  .venv\Scripts\activate.bat
  ```

- **Windows PowerShell:**
  ```powershell
  .venv\Scripts\Activate.ps1
  ```

---

After activation, you can install project dependencies as needed:

```bash
pip install -r requirements.txt
```