#!/usr/bin/env python3
"""
Validation script for Quantum Computing with Qiskit environment.
Checks for required packages and prints their versions. Exits with nonzero code if any are missing.
"""
import sys

REQUIRED = [
    ("qiskit", "Qiskit"),
    ("qiskit_aer", "Qiskit Aer"),
    ("numpy", "NumPy"),
    ("matplotlib", "Matplotlib"),
    ("scipy", "SciPy"),
    ("jupyter", "Jupyter"),
]

OPTIONAL = [
    ("qiskit_nature", "Qiskit Nature"),
    ("qiskit_optimization", "Qiskit Optimization"),
    ("qiskit_machine_learning", "Qiskit Machine Learning"),
    ("qiskit_finance", "Qiskit Finance"),
    ("qiskit_dynamics", "Qiskit Dynamics"),
]

def check_package(pkg, label=None):
    try:
        mod = __import__(pkg)
        version = getattr(mod, "__version__", "(no version attr)")
        print(f"[OK] {label or pkg}: {version}")
        return True
    except ImportError:
        print(f"[MISSING] {label or pkg}")
        return False

def main():
    print("\nValidating core environment...\n")
    ok = True
    for pkg, label in REQUIRED:
        if not check_package(pkg, label):
            ok = False
    print("\nChecking optional Qiskit extensions...\n")
    for pkg, label in OPTIONAL:
        check_package(pkg, label)
    if ok:
        print("\nEnvironment validation: SUCCESS\n")
        sys.exit(0)
    else:
        print("\nEnvironment validation: FAILED (see missing above)\n")
        sys.exit(1)

if __name__ == "__main__":
    main()
