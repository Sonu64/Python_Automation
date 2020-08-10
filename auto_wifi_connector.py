# Importing required modules
import os, sys

# Getting all the Saved networks and showing them. read() function helps in storing that
savedProfiles = os.popen("netsh wlan show profiles").read()
print("ALL SAVED NETWORKS\n"+savedProfiles)

# Getting all the Available networks and showing them
availableProfiles = os.popen("netsh wlan show networks").read()
print("\nALL AVAILABLE NETWORKS\n"+availableProfiles)

# Getting preferred connection from the user
preferredSSID = input("Enter the preferred WiFi for your connection: ")
# Disconnecting from all other connections
response = os.popen("netsh wlan disconnect").read()

# If the preferred SSID is not saved in System, then notify and exit
if preferredSSID not in savedProfiles:
    print("Profile for " + preferredSSID + " is not saved in your system!")
    print("Sorry, But I can't connect to this network :(")
    input("Press the ENTER key to exit...")
    sys.exit()

# Otherwise continue to check untill a saved network is found ON
# You can add extra variables to check only for 10 minutes or whatever
while True:
    avail = os.popen("netsh wlan show networks").read()
    # If the preffered SSID is available to connect to
    if preferredSSID in avail:
        # just showing that the network is found, i.e., It is Turned ON or whatever !
        print("Network Found!")
        # No need to check for available networks any more
        break;

# Printing a decoraive text
print("Connecting....")
# Running the command to connect to that network via netsh
connectionResponse = os.popen('netsh wlan connect name = '+'"'+preferredSSID+'"').read()
# If you wish, print it
print(connectionResponse)
        
