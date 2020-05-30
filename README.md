A demonstration of Shor's algorithm attacking RSA keys. **Work in progress**.

Installation:

    pip install -r requirements.txt

Usage:

  1. Start the sniffing tool: `sudo python sniff.py`
  2. Start the server: `python server.py`
  3. Start the client with some string: `python client.py 'Hello world'`
  4. The sniffing tool should detect the message and decrypt it with Shor's algorithm. (It actually doesn't at the time; the Shor implementation is in `quant.py`).