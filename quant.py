from qiskit_fast_shor import TaggedDAG, Shor
from qiskit import Aer, IBMQ

IBMQ.load_account()

a, N = 2, 21

backend = Aer.get_backend('qasm_simulator')
# provider = IBMQ.load_account()
# backend = provider.get_backend('ibmq_qasm_simulator')

shor = Shor(N, a, quantum_instance=backend)
print("Constructing...")
circuit = shor.construct_circuit()
print("Drawing...")
#if not isProfiler:
#    print(circuit.draw())  # or circuit.draw(output='mpl') for a nicer looking diagram ;)
print("Running...")
if N == 33:
    job_id = "5ecaeb4bd2d11d001a1aaf72"
elif N == 15:
    job_id = "5ecae5ed4f56e200131772af"
else:
    job_id = None
res = shor.run(job_id=job_id)
print(res)