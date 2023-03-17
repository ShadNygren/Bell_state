# Import necessary libraries
from qiskit import QuantumCircuit, Aer, transpile, assemble
from qiskit.visualization import plot_histogram

# Create a quantum circuit with 2 qubits and 2 classical bits
qc = QuantumCircuit(2, 2)

# Apply a Hadamard gate to the first qubit
qc.h(0)

# Apply a CNOT gate with the first qubit as control and the second qubit as target
qc.cx(0, 1)

# Measure both qubits and store the results in the classical bits
qc.measure([0, 1], [0, 1])

# Visualize the quantum circuit
print(qc)

# Choose the Qiskit simulator
simulator = Aer.get_backend('qasm_simulator')

# Transpile and assemble the circuit for the simulator
transpiled_circuit = transpile(qc, simulator)
qobj = assemble(transpiled_circuit)

# Run the simulation and collect the results
result = simulator.run(qobj).result()

# Get the counts (results) of the simulation
counts = result.get_counts(qc)

# Visualize the results as a histogram
plot_histogram(counts)
