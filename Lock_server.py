import place_holder
from threading import Lock
from TcpServer import TcpServer

class LockServer(TcpServer):
    locks_mutex = Lock()
    locks = {}

    # override request processing function
    def process_req(self, conn, request, vars):
        file_id = vars[0]
        client = vars[1]

        # lock request
        if request == place_holder.requested_lock:
            try:
                # acquire locks mutex
                self.locks_mutex.acquire()
                # return failure if file is locked and lock owner is different client
                if file_id in self.locks and self.locks[file_id] != client:
                    self.send_msg(conn, place_holder.failure.format("File locked by another client"))
                # otherwise okay to lock file for client and return success
                else:
                    self.locks[file_id] = client
                    self.send_msg(conn, place_holder.success.format("Locked"))
            finally:
                self.locks_mutex.release()

        # unlock request
        elif request == place_holder.requested_unlock:
            try:
                # acquire locks mutex
                self.locks_mutex.acquire()
                # unlock and return success if file is locked and owned by client
                if file_id in self.locks and self.locks[file_id] == client:
                    del self.locks[file_id]
                    self.send_msg(conn, place_holder.success.format("Unlocked"))
                # otherwise return failure if file not in array
                elif file_id not in self.locks:
                    self.send_msg(conn, place_holder.failure.format("File not locked"))
                # otherwise return file locked by another client
                else:
                    self.send_msg(conn, place_holder.failure.format("File locked by another client"))

            finally:
                self.locks_mutex.release()

        # usage request
        elif request == place_holder.requested_use:
            try:
                # acquire locks mutex
                self.locks_mutex.acquire()
                # return disallowed only if file is locked and owned by different client
                if file_id in self.locks and self.locks[file_id] != client:
                    self.send_msg(conn, place_holder.failure.format("Disallowed"))
                # otherwise return allowed to access file
                else:
                    self.send_msg(conn, place_holder.success.format("Allowed"))
            finally:
                self.locks_mutex.release()

def main():
    print "Lock Server started on " + str(place_holder.lock_server)
    LockServer(place_holder.lock_server)
if __name__ == "__main__": main()
