"""
Title: Application to run the Android Debug Bridge daemon
Author: Primus27
Version: 1.0
"""

# Import packages
import subprocess
import os
from datetime import datetime as dt

# Specify path of platform tools
# CHANGE THIS TO YOUR ADB DIRECTORY
path = r"C:\Android SDK\platform-tools".lower()


def get_time():
    """
    Function to get the current time
    :return: Returns current time
    """
    return dt.now().strftime("%d-%m-%Y %H:%M:%S %f")


def format_log_msg(user_msg):
    """
    Function that formats a message w/ current time for logging.
    :param user_msg: User error/message can map to a dict key to return the
        same message consistently
    :return: Formatted error message
    """
    # Declare dictionary that maps user error with an error message
    err_msg_dict = {
        "no_dir": "Could not find specified directory",
        "runtime": "Script run unsuccessfully"
    }

    # If the user error is not in the dictionary, do not try to fetch value
    if user_msg in err_msg_dict.keys():
        msg = err_msg_dict.get(user_msg)
    else:
        msg = user_msg

    # Assign current time
    current_time = get_time()

    # Format message: DATE TIME MESSAGE
    return_msg = f"{current_time}\t {msg}"
    return return_msg


def output_to_log(msg):
    """
    Logs all items in list to a file (log.txt)
    :param msg: List of timecodes and messages
    """
    try:
        with open("log.txt", "a") as f:
            if msg:
                # Add a new line at end of each value in list
                f.writelines("%s\n" % line for line in msg)
    # Inadequate permission to access location / save to location
    except PermissionError:
        print("[*] Error saving log - Permission denied")
    # Could not find path
    except OSError:
        print("[*] Error saving log - Path issues")


def main():
    """
    Main method. Looks to see whether computer and device are connected. If not
        connected, start daemon to connect.
    """
    log_msg = []
    # If path exists
    if os.path.isdir(path):
        # Run adb command
        process1 = subprocess.run(["adb", "devices"], cwd=path,
                                  capture_output=True, text=True, shell=True)
        if process1.returncode == 0:  # Command was successful
            log_msg.append(format_log_msg(process1.stdout))
        else:
            log_msg.append(format_log_msg(process1.stderr))
    else:
        log_msg.append(format_log_msg("no_dir"))

    output_to_log(log_msg)


if __name__ == "__main__":
    main()
