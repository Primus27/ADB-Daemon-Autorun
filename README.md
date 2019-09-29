# Android Debug Bridge Autorun

## Features
 - Automatically runs adb daemon in the correct directory when started.
 - Output messages and errors to log file.

## Requirements and Installation
 - [Python 3.6+](https://www.python.org/)
 - [Download Android SDK platform tools](https://developer.android.com/studio/releases/platform-tools.html)
    - Extract platform tools to system drive. E.g. `c:\android sdk\platform-tools`
 - **Change directory of platform-tools in `connect_adb.py` (line 14)**
 - Ensure that android device has USB debugging enabled
    - `Settings` -> `System` -> `About phone`
        - Tap `Build number` 7x (seven) times (this may be under `Software info`)
        - Developer options now enabled
    - `Settings` -> `System` -> `Developer options`
        - Enable `Android debugging` and/or `USB debugging`
        - Enable `Debugging notify` (optional)

## Usage
 - Connect android device to windows system
     - Set `USB Mode` to `PTP` or `USB for photo transfer`
        - Found in notification bar 
        - Found in `Settings` -> `Connected Devices`
     - Allow `Enable USB Debugging on this computer`
 - Run `connect_adb.py`

## Changelog
#### Version 1.0 - Initial release
 - ADB Autorun command for Windows.
