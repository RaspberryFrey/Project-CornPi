import socket
import sys
import time
import datetime
import RPi.GPIO as GPIO

from Adafruit_LED_Backpack import SevenSegment
# ===========================================================================

segment = SevenSegment.SevenSegment(address=0x70)

print ("Project CornPi developed by Jordan Frey")
print ("Press CTRL+Z to exit")

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('192.168.0.33',  5545)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)
segment.begin()

a = ['0a', '1a', '2a', '3a', '4a', '5a', '6a', '7a', '8a', '9a', '10', '11a', '12a', '13a', '14a', '15a', '16a', '17a', '18a', '19a', '20a', '21a']
b = ['0b', '1b', '2b', '3b', '4b', '5b', '6b', '7b', '8b', '9b', '10', '11b', '12b', '13b', '14b', '15b', '16b', '17b', '18b', '19b', '20b', '21b']

while True:
    # Wait for a connection
    print >>sys.stderr, 'waiting for a connection'
    connection, client_address = sock.accept()
      
    try:
        print >>sys.stderr, 'connection from', client_address
        
        # Receive the data in small chunks and retransmit it
        while True:
            
            data = connection.recv(1024)
            
            dataA0 = data.replace('0a', '', 100)
            dataA1 = dataA0.replace('1a', '')
            dataA2 = dataA1.replace('2a', '')
            dataA3 = dataA2.replace('3a', '')
            dataA4 = dataA3.replace('4a', '')
            dataA5 = dataA4.replace('5a', '')
            dataA6 = dataA5.replace('6a', '')
            dataA7 = dataA6.replace('7a', '')
            dataA8 = dataA7.replace('8a', '')
            dataA9 = dataA8.replace('9a', '')
            dataA10 = dataA9.replace('10a', '')
            dataA11 = dataA10.replace('11a', '')
            dataA12 = dataA11.replace('12a', '')
            dataA13 = dataA12.replace('13a', '')
            dataA14 = dataA12.replace('14a', '')
            dataA15 = dataA14.replace('15a', '')
            dataA16 = dataA15.replace('16a', '')
            dataA17 = dataA16.replace('17a', '')
            dataA18 = dataA17.replace('18a', '')
            dataA19 = dataA18.replace('19a', '')
            dataA20 = dataA19.replace('20a', '')
            dataA21 = dataA20.replace('21a', '')

            dataB0 = data.replace('0b', '', 100)
            dataB1 = dataB0.replace('1b', '')
            dataB2 = dataB1.replace('2b', '')
            dataB3 = dataB2.replace('3b', '')
            dataB4 = dataB3.replace('4b', '')
            dataB5 = dataB4.replace('5b', '')
            dataB6 = dataB5.replace('6b', '')
            dataB7 = dataB6.replace('7b', '')
            dataB8 = dataB7.replace('8b', '')
            dataB9 = dataB8.replace('9b', '')
            dataB10 = dataB9.replace('10b', '')
            dataB11 = dataB10.replace('11b', '')
            dataB12 = dataB11.replace('12b', '')
            dataB13 = dataB12.replace('13b', '')
            dataB14 = dataB13.replace('14b', '')
            dataB15 = dataB14.replace('15b', '')
            dataB16 = dataB15.replace('16b', '')
            dataB17 = dataB16.replace('17b', '')
            dataB18 = dataB17.replace('18b', '')
            dataB19 = dataB18.replace('19b', '')
            dataB20 = dataB19.replace('20b', '')
            dataB21 = dataB20.replace('21b', '')
            
        
            dataAA = dataB21.replace('a', '')
            dataA = dataAA.replace('a', '')
            DATAAA = dataA
            
            dataBB = dataA21.replace('b', '')
            dataB = dataBB.replace('b', '')
            DATABBB = dataB

            if "21" in DATAAA:
                DATAAA = "21"
            elif "20" in DATAAA:
                DATAAA = "20"
            elif "19" in DATAAA:
                DATAAA = "19"
            elif "18" in DATAAA:
                DATAAA = "18"
            elif "17" in DATAAA:
                DATAAA = "17"
            elif "16" in DATAAA:
                DATAAA = "16"
            elif "15" in DATAAA:
                DATAAA = "15"
            elif "14" in DATAAA:
                DATAAA = "14"
            elif "13" in DATAAA:
                DATAAA = "13"
            elif "12" in DATAAA:
                DATAAA = "12"
            elif "11" in DATAAA:
                DATAAA = "11"
            elif "10" in DATAAA:
                DATAAA = "10"
            elif "9" in DATAAA:
                DATAAA = "9"
            elif "8" in DATAAA:
                DATAAA = "8"
            elif "7" in DATAAA:
                DATAAA = "7"
            elif "6" in DATAAA:
                DATAAA = "6"
            elif "5" in DATAAA:
                DATAAA = "5"
            elif "4" in DATAAA:
                DATAAA = "4"
            elif "3" in DATAAA:
                DATAAA = "3"
            elif "2" in DATAAA:
                DATAAA = "2"
            elif "1" in DATAAA:
                DATAAA = "1"
            elif "0" in DATAAA:
                DATAAA = "0"
                
            if "21" in DATABBB:
                DATABBB = "21"
            elif "20" in DATABBB:
                DATABBB = "20"
            elif "19" in DATABBB:
                DATABBB = "19"
            elif "18" in DATABBB:
                DATABBB = "18"
            elif "17" in DATABBB:
                DATABBB = "17"
            elif "16" in DATABBB:
                DATABBB = "16"
            elif "15" in DATABBB:
                DATABBB = "15"
            elif "14" in DATABBB:
                DATABBB = "14"
            elif "13" in DATABBB:
                DATABBB = "13"
            elif "12" in DATABBB:
                DATABBB = "12"
            elif "11" in DATABBB:
                DATABBB = "11"
            elif "10" in DATABBB:
                DATABBB = "10"
            elif "9" in DATABBB:
                DATABBB = "9"
            elif "8" in DATABBB:
                DATABBB = "8"
            elif "7" in DATABBB:
                DATABBB = "7"
            elif "6" in DATABBB:
                DATABBB = "6"
            elif "5" in DATABBB:
                DATABBB = "5"
            elif "4" in DATABBB:
                DATABBB = "4"
            elif "3" in DATABBB:
                DATABBB = "3"
            elif "2" in DATABBB:
                DATABBB = "2"
            elif "1" in DATABBB:
                DATABBB = "1"
            elif "0" in DATABBB:
                DATABBB = "0"
                
            if len(DATAAA) < 2:
                DATAAA = DATAAA[:1]
                
            if len(DATABBB) < 2:
                DATABBB = DATABBB[:1] 
            #dataA = float(dataA)
            #dataB = float(dataB)
            
            #print float(dataB)
            #print (dataA)
                
            segment.clear()
	    segment.print_number_str((DATAAA), justify_right=False)
	    time.sleep(.1)
	    segment.print_number_str((DATABBB), justify_right=True)
            time.sleep(.1)
            segment.set_colon(True)
            segment.write_display()
#           time.sleep(.2) #

    finally:
        # Clean up the connection
        connection.close()
        
