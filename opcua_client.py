
# Minimal OPC-UA client skeleton (educational)
# Requires: pip install opcua
from opcua import Client
import time

SERVER_URL = "opc.tcp://127.0.0.1:4840/freeopcua/server/"
NODE_CMD = "ns=2;i=2"   # placeholder
NODE_TELE = "ns=2;i=3"  # placeholder

def main():
    client = Client(SERVER_URL)
    try:
        client.connect()
        print("Connected to OPC-UA server")
        cmd_node = client.get_node(NODE_CMD)
        tele_node = client.get_node(NODE_TELE)
        cmd_node.set_value("MOVE_PICK")
        time.sleep(0.5)
        print("Telemetry:", tele_node.get_value())
    finally:
        client.disconnect()

if __name__ == "__main__":
    main()
