# 🛠️ Installation Guide for Quantum Computing with Qiskit (QCWQ)

This guide walks you through setting up the environment, installing dependencies, and fixing common errors.

---

## **📌 Prerequisites**
Ensure you have the following installed:

1. **Python 3.8+** (recommended: latest 3.x)

   ```bash
   python3 --version
   ```

    If not installed, install it using:

    ```bash
    sudo apt update
    sudo apt install python3 python3-venv python3-pip
    ```

2. Git (For Cloning the Repository)

    ```bash
    git --version
    ```

    If not installed, install it using:

    ```bash
    sudo apt install git
    ```

3. Jupyter Notebook (For Running the Code)

    ```bash
    jupyter --version
    ```

    If not installed, install it using:

    ```bash
    pip install jupyter
    ```

## **📌 Installation**
Here the step-by-step of the installation:

### 📌 Step 1: Clone the Repository

```bash
git clone https://github.com/SHA888/qcwq.git
cd qcwq
```

### 📌 Step 2: Set Up Virtual Environment

1. Create a virtual environment

    ```bash
    python3 -m venv qiskit_env
    ```

2. Activate the virtual environment

    ```bash
    source qiskit_env/bin/activate
    ```

### 📌 Step 3: Install Dependencies
Run:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

If pip throws *an externally-managed-environment* ***error***, use:

```bash
pip install --break-system-packages -r requirements.txt
```

### 📌 Step 4: Register Jupyter Kernel
Ensure Jupyter recognizes the virtual environment:

```bash
python3 -m ipykernel install --user --name=qiskit_env --display-name "Python (qiskit_env)"
```

### 📌 Step 5: Run Jupyter Notebook
Can be done in Terminal or IDE (e.g., VS Code)
-  Terminal Mode:

    ```bash
    jupyter notebook
    ```
    After running the command above, you’ll see an output like this:
    ```bash
    Jupyter Notebook is running at:
    http://localhost:8888/?token=your-long-token
    ```
    Copy the URL and paste it into your browser to open Jupyter Notebook.

- VS Code Mode:

    - Open VS Code.
    - Open the `qcwq` folder.
    - Open a `.ipynb` file.
    - Click "Open in Browser" when prompted.
    - Click "Run" and select the Python `(qiskit_env) Kernel`.

### Create a New Jupyter Notebook on Your Browser
Once Jupyter Notebook is open:

- Click "New" → "Python 3" to create a new notebook.
- Rename it to anything you want. (e.g., "First_Quantum_Circuit.ipynb") by clicking on the title to rename.
- Select Kernel → Change Kernel → Python (qiskit_env)
- Now you're ready to start coding quantum circuits! 
- 3️Ru the first cell and start experimenting!         🎭

## 🎉 Now You're Ready!



Try this as your first quantum code!
- **Copy and paste** it in your first Jupyter Notebook cell:

    ```python
    import quantum_circuits as qc

    # Create a quantum circuit in superposition
    quantum_circuit = qc.create_superposition_circuit()

    # Draw the circuit using Matplotlib
    quantum_circuit.draw('mpl')
    ```
- **Run** it (Shift + Enter)
- And you should see this output:

    ![alt text](/image.png)

## Congrats! 👏👏👏

> - Your first quantum circuit on Jupyter Notebook ***works***.
> - Otherwise, see the troubleshooting section below or ping us in the Discussion.

## 📌 Common Errors & Fixes

### ❌ ModuleNotFoundError: No module named 'qiskit.providers.aer'
✅ Fix:

```bash
pip install --no-cache-dir qiskit-aer
```

### ❌ MissingOptionalLibraryError: matplotlib
✅ Fix:

```bash
pip install matplotlib
```

### ❌ MissingOptionalLibraryError: pylatexenc
✅ Fix:

```bash
pip install pylatexenc
```

### ❌ Jupyter Notebook Not Detecting Virtual Environment
✅ Fix:

```bash
python3 -m ipykernel install --user --name=qiskit_env --display-name "Python (qiskit_env)"
```

---

# Quantum Computing with Qiskit: Installation Guide

This guide will help you set up your environment for hands-on quantum computing on Windows, macOS, and Linux.

---

## 1. Prerequisites
- **Python 3.8+** (recommended: latest 3.x)
- **Git**
- **pip** (comes with Python)
- **(Optional) Virtual environment tool:**
  - `venv` (standard)
  - `conda` (Anaconda/Miniconda)

---

## 2. Clone the Repository
```bash
git clone https://github.com/SHA888/qcwq.git
cd qcwq
```

---

## 3. Set Up a Virtual Environment (Recommended)

### Using venv (all platforms)
```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### Using conda (if installed)
```bash
conda create -n qcwq python=3.10
conda activate qcwq
```

---

## 4. Install Dependencies
```bash
pip install -r requirements.txt
```

If you want advanced modules, uncomment and install the relevant lines in `requirements.txt` (e.g., Nature, Optimization, ML, Finance, Dynamics).

---

## 5. Verify Your Installation

After installing dependencies, run the validation script:

```bash
python scripts/validate_env.py
```

- This script checks for all required packages and prints their versions.
- Missing packages are clearly reported for troubleshooting.

If validation fails, review the error messages and ensure you have installed all required dependencies.

---

## 6. Launch Jupyter Notebook
```bash
jupyter notebook
```
Open and run `notebooks/first_circuit.ipynb` to verify everything works.

---

## 7. Troubleshooting
- If you encounter issues, ensure you are using the correct Python version and that your virtual environment is activated.
- For help, see the [Qiskit Installation Guide](https://qiskit.org/documentation/getting_started.html) or open an issue in this repo.

---

## 8. Uninstalling
Deactivate and remove your virtual environment:
```bash
deactivate  # or conda deactivate
rm -rf .venv  # or conda env remove -n qcwq
```

---

Happy Quantum Coding!
