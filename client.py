import socket
import place_holder


def send_request(ip,port,data):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip,port))
    sock.sendall(data)
    print "Sent: \"" + data.rstrip('\n') + "\""
    response = sock.recv(2048)
    print(response)
    return capture_received_reponse(response)



def capture_received_reponse(msg):
    temp = []
    for i in msg.split("\n"):
        if i != "":
            c = i.split(":")
            temp.append(c[1])
    return temp



# Getting File location
print "Enter Client Information"
name = raw_input("Enter Client Name")
info = send_request("localhost",place_holder.directory_server,data = place_holder.requested_file_details.format("test.txt","Desktop","write"))
file_id = info[0]
file_ip = info[1]
file_port = int(info[2])
print("file_id",file_id)
print("file_ip",file_ip)
print("file_port",file_port)
raw_input("Press Enter to continue...\n")

# write file to server
file = open('test.txt', 'r')
send_req(file_ip, file_port, config.WRITE_FILE.format(file_id, name, file.read()))
raw_input("Press Enter to continue...\n")

# get lock on file
send_req("localhost", config.LOCK_SERVER, config.REQUEST_LOCK.format(file_id, name))
raw_input("Press Enter to continue...\n")

# read file from server
send_req(file_ip, file_port, config.READ_FILE.format(file_id, name))
raw_input("Press Enter to continue...\n")

# unlock file
send_req("localhost", config.LOCK_SERVER, config.REQUEST_UNLOCK.format(file_id, name))
raw_input("Press Enter to continue...\n")


