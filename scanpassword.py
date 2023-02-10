import wmi


def get_wifi_password(ssid):
    # Connect to the WMI service
    c = wmi.WMI()

    # Query the WMI service for available wireless networks
    networks = c.Win32_NetworkAdapterConfiguration(IPEnabled=True)

    # Loop over the list of networks and find the desired network
    for network in networks:
        if network.SSID and network.SSID.strip("'") == ssid:
            password = network.GetPassword()
            break
    else:
        raise Exception("Network not found")

    # Return the password for the desired network
    return password


if __name__ == "__main__":
    ssid = input("Enter the SSID of the network: ")
    password = get_wifi_password(ssid)
    print("Password: {}".format(password))
