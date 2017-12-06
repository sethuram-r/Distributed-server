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

#Writing the file to server
file = open('test.txt', 'r')
#send_request(' 0.0.0.0',6008,data = place_holder.requested_file_details.format("test.txt","Desktop","write"))

send_request(file_ip, file_port,data = place_holder.write_file.format(file_id, name, file.read()))

