python -m venv .venv
# Windows PowerShell: .venv\\Scripts\\Activate.ps1
# macOS/Linux: source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install jupyterlab numpy matplotlib scipy sympy pandas
python -m jupyter lab
