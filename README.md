A demonstration of Shor's algorithm attacking RSA keys.

Requires Python 3.5 and up.

Installation:

 1. `pip install -r requirements.txt`
 2. Clone https://github.com/CapacitorSet/qiskit-fast-shor in the subfolder `qiskit_fast_shor`

Usage:

  1. Start the sniffing tool: `sudo python sniff.py`
  2. Start the server: `python server.py`
  3. Start the client: `python client.py`
  4. Send some fictitious credentials.
  4. The sniffing tool should intercept the public key, factor it with Shor's algorithm, and decrypt the emails and credentials.

Options:

 * `--debug` enables debug-level logging.
 * `--aer` (for sniff.py) uses the Aer backend. If this flag is not given, the default is the IBMQ QASM simulator.
 * `--cache` (for sniff.py) uses cached jobs.
