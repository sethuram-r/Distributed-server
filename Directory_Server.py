import sys
import place_holder
import random
from TcpServer import TcpServer


class DirectoryServer(TcpServer):
    print(place_holder.requested_file_details)
    messages = {place_holder.requested_file_details}
    folders = {}
    servers = []
    for i in range(place_holder.no_of_replication_servers):
        servers.append(place_holder.replication_server + (i * (place_holder.replication_server_copies + 1)))


    # override request processing function
    def process_req(self, conn, request, vars):
        # requesting file details from directory
        if request == place_holder.requested_file_details:
            try:
                # add folder to directory listing if writing
                if vars[2] == 'write':
                    # check if folder exists in directory listing
                    if vars[1] not in self.folders:
                        # if not then assign folder to random server
                        random_server_port = random.choice(self.servers)
                        self.folders[vars[1]] = {'id': self.hash_str(self.ip + str(random_server_port) + vars[1]),
                                                 'ip': self.ip, 'port': str(random_server_port), 'files': [vars[0]]}

                # return directory id and location
                response = self.folders[vars[1]]

                # check if file in directory
                if vars[0] in response['files']:
                    self.send_msg(conn,
                                  place_holder.returned_file_details.format(response['id'], response['ip'], response['port']))
                else:
                    self.error(conn, "File not found.")

            except KeyError:
                # return file not found if file_id key not in files dict
                self.error(conn, "File not found.")


def main():
    print "Directory Server started on " + str(place_holder.directory_server)
    server = DirectoryServer(place_holder.directory_server)


if __name__ == "__main__": main()