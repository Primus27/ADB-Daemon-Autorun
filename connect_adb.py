"""
Title: Application to run the Android Debug Bridge daemon
Author: Primus27
Version: 1.1
"""

# Import packages
import subprocess
import os
import logging

# Specify path of platform tools (adb directory)
path = r"C:\Android SDK\platform-tools".lower()
# Specify whether to output log to a file (True / False)
log = False

# Set default logging params
if log:
    logging.basicConfig(filename="adb.log", level=logging.INFO,
                        format="%(asctime)s : %(levelname)s : %(message)s")
else:
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s : %(levelname)s : %(message)s")


def main():
    """
    Main method.
    Looks to see whether computer and device are connected. If not
        connected, start daemon to connect.
	Logs output if logging enabled.
    """
    # If platform tools path exists
    if os.path.isdir(path):
        # Run adb command
        adb_process = subprocess.run(["adb", "devices"], cwd=path,
                                     capture_output=True, text=True,
                                     shell=True)
        # Logging enabled
        if log:
            if adb_process.returncode == 0:  # Command was successfully run
                # Format command output
                adb_process_out = str(adb_process.stdout).replace(
                    "\tdevice", "(device)").replace(
                    "attached", "attached:").replace(
                    "\n", " ")[:-2]

                if adb_process_out == "List of devices attached:":
                    logging.warning("No devices attached")
                else:
                    logging.info(adb_process_out)
            else:
                logging.error(str(adb_process.stderr).replace("\n", " ")[:-2])
    elif log:
        logging.critical("Could not find platform tools directory")


if __name__ == "__main__":
    main()
