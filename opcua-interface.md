
# OPC-UA Interface (Excerpt)

- Objects:
  - /Objects/Robot/Commands (String): accepted commands: MOVE_PICK, MOVE_PLACE, HOME
  - /Objects/Robot/Telemetry (JSON String): { "state": "...", "pos": [x,y,z], "timestamp": ... }

- Contract:
  - Commands are idempotent; responses reflected in Telemetry within 500 ms (simulated).
  - Safety interlocks handled in KRC; demo assumes dry-run.
