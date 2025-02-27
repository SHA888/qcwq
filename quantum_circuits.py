from qiskit import QuantumCircuit
from qiskit_aer import Aer
from qiskit_aer.backends import AerSimulator
from qiskit.primitives import Sampler
from qiskit import transpile



def create_superposition_circuit():
    """
    Creates a quantum circuit with 1 qubit in superposition.
    """
    qc = QuantumCircuit(1)
    qc.h(0)
    return qc

def simulate_circuit(qc):
    """
    Simulates the given quantum circuit.
    """
    qc.measure_all()
    simulator = Aer.get_backend('qasm_simulator')
    result = execute(qc, simulator, shots=1024).result()
    return result.get_counts()

if __name__ == "__main__":
    qc = create_superposition_circuit()
    print("Quantum Circuit:")
    print(qc)
    results = simulate_circuit(qc)
    print("Measurement Results:", results)
