import network, time
import MyKeys

wlan = network.WLAN(network.STA_IF)

def connect(timeout_s=10):
    if not wlan.active():     # Activate WLAN
        wlan.active(True)
    if wlan.isconnected():    # If already open, shut down before attempting connection
        wlan.disconnect()
        time.sleep(0.5)

    # Connection attempt: can take several seconds. Fails if time exceeds timeout_s
    print(f"Attempting Wifi connection to {MyKeys.SSID}...")
    wlan.connect(MyKeys.SSID, MyKeys.KEY)
    start_time = time.time()
    while wlan.status() in (network.STAT_IDLE, network.STAT_CONNECTING, 2):
        if (time.time() - start_time) > timeout_s:
            break
        print('.', end='')
        time.sleep(0.5)

    # If successful, print confirmation and return True
    if wlan.isconnected():
        print(f"\nWifi connected in {time.time() - start_time:.2f}s.")
        print(f"IP: {wlan.ifconfig()[0]}")
        return True

    # Fail so try to guess the likely problem(s) before returning False
    print("\n\nConnection failed scanning for cause...")
    try:
        # Look for all SSIDs in range and check that the specified one is there
        scanned_ssids = [s[0].decode('utf8') for s in wlan.scan()]        
        if MyKeys.SSID in scanned_ssids:
            # We know the network is visible, so the password is likely the issue
            print(f"\nSSID '{MyKeys.SSID}' was found in the scan")
            print("The most likely cause of failure is an incorrect password.")
        else:
            # The network is not visible - could be several reasons...
            print(f"\nSSID '{MyKeys.SSID}' was NOT found in the scan.")
            print("The SSID may be wrong, the router may be off, or the device is out of range.")
    
    except Exception as e:
        print(f"An error occurred during scanning: {e}")

    wlan.active(False)
    return False
