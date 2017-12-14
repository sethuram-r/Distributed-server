
################################# Imported Packages #############################################

import socket
import place_holder

#################################################################################################


messages = [place_holder.RETURN_FILE_DATA, place_holder.RETURN_FILE_DETAILS, place_holder.SUCCESS, place_holder.FAILURE]


# Used to send the request to the desired server

def send_req(ip, port, data):
    # connect server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port)) 
    s.settimeout(2)
    s.sendall(data)
    print "Sent: \"" + data.rstrip('\n') + "\""
    return capture_received_reponse(s.recv(2048))

# Used to capture the response from the server

def capture_received_reponse(msg):
    temp = []
    for i in msg.split("\n"):
        if i != "":
            c = i.split(":")
            temp.append(c[1])
    return temp




print "##################################Command Line Client Interface############################"

name = raw_input("Enter Client Name: ")

# Get the file Details from the Directory Server
response = send_req("localhost", place_holder.DIR_SERVER, place_holder.REQUEST_FILE_DETAILS.format("test.txt", "Desktop", "WRITE"))
if response:
    file_id = response[0]
    file_ip = response[1]
    file_port = int(response[2])
raw_input("Press Enter to continue...\n")



# Wriring file to the Server by use of Replication
file = open('test.txt', 'r')
send_req(file_ip, file_port, place_holder.WRITE_FILE.format(file_id, name, file.read()))
raw_input("Press Enter to continue...\n")

# Establishing Lock on a File
send_req("localhost", place_holder.LOCK_SERVER, place_holder.REQUEST_LOCK.format(file_id, name))
raw_input("Press Enter to continue...\n")

# Reading the file from the server
send_req(file_ip, file_port, place_holder.READ_FILE.format(file_id, name))
raw_input("Press Enter to continue...\n")

# Removing the lock from the file
send_req("localhost", place_holder.LOCK_SERVER, place_holder.REQUEST_UNLOCK.format(file_id, name))
raw_input("Press Enter to continue...\n")

