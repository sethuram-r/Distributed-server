# servers
FILE_SERVER = 6000
DIR_SERVER = 6001
LOCK_SERVER = 6002
REP_SERVER = 6003

# variables
LOCK_ATTEMPTS = 1
REP_SERVERS = 2
REP_SERVER_COPIES = 1

# client and directory server communication
REQUEST_FILE_DETAILS = 'REQUEST_FILE_DETAILS: {}\nDIRECTORY: {}\nACTION: {}\n\n'
RETURN_FILE_DETAILS = 'RETURN_FILE_DETAILS: {}\nIP: {}\nPORT: {}\n\n'

# client/replication server and lock server communication
REQUEST_LOCK = 'REQUEST_LOCK: {}\nCLIENT: {}\n\n'
REQUEST_USE = 'REQUEST_USE: {}\nCLIENT: {}\n\n'
REQUEST_UNLOCK = 'REQUEST_UNLOCK: {}\nCLIENT: {}\n\n'

# client and replication server communication
WRITE_FILE = 'WRITE_FILE: {}\nCLIENT: {}\nDATA: {}\n\n'
READ_FILE = 'READ_FILE: {}\nCLIENT: {}\n\n'
DELETE_FILE = 'DELETE_FILE: {}\nCLIENT: {}\n\n'
RETURN_FILE_DATA = 'RETURN_FILE_DATA: {}\n\n'

# status messages
SUCCESS = 'SUCCESS: {}\n\n'
FAILURE = 'FAILURE: {}\n\n'
ERROR_MSG = 'ERROR: {}\n\n'
