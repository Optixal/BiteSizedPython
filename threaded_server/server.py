#!/usr/bin/python3

# Basic Multi-Threaded Server
# Optixal

import socket, sys, time, datetime
import coloredstatus as cs
from time import sleep
from _thread import *

if len(sys.argv) != 2:
    print(cs.status, "Usage:", sys.argv[0], "[port]")
    sys.exit(1)

host = '0.0.0.0'
port = int(sys.argv[1])

log_location = "log.txt"
timeout = 10

# Custom Exception
class ServerError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

# Get Current Time
def gettime():
    return '{0:%d/%m/%y %H:%M:%S}'.format(datetime.datetime.now()) + " -"

# Log
def log(host, port, loginfo):
    with open(log_location, "a") as f:
        f.write(gettime() + " " + loginfo + " - " + host + ':' + str(port) + "\n")

# Client Thread
def client(conn, addr):
    print(cs.openlabel, gettime(), "New connection from", addr[0] + ':' + str(addr[1])) 
    #log(addr[0], addr[1], "Joined")
    
    conn.send(str.encode(cs.good + " Welcome to the Server!\n"))
    conn.send(str.encode(cs.good + " By Optixal\n\n"))
    sleep(0.2)
    
    conn.settimeout(timeout)

    try:
        while True:
            # Send
            conn.sendall(str.encode(cs.status + " Hello!\n" + cs.status + " Input: "))
            
            # Receive
            data = conn.recv(2048).decode("UTF-8").strip()
            if not data:
                raise ServerError("null data")
            #log(addr[0], addr[1], "Received: " + data)

            # Process
            conn.sendall(str.encode(cs.status + " You said: " + data + "\n\n"))
    
    except socket.timeout:
        conn.send(str.encode("\n" + cs.error + " You were kicked for timing out!\n"))
        print(cs.kicklabel, gettime(), "Kicked", addr[0] + ':' + str(addr[1]), "for being timed out")
    except ServerError as se:
        try:
            conn.send(str.encode("\n" + cs.error + " You were kicked from the server for " + se.value + "!\n"))
            print(cs.kicklabel, gettime(), "Kicked", addr[0] + ':' + str(addr[1]), "for", se.value)
        except BrokenPipeError:
            print(cs.closelabel, gettime(), "Connection closed from", addr[0] + ':' + str(addr[1]), "due to broken pipe") 
    except (BrokenPipeError, ConnectionResetError):
        print(cs.closelabel, gettime(), "Connection closed from", addr[0] + ':' + str(addr[1]), "due to broken pipe") 
    except:
        conn.send(str.encode("\n" + cs.error + " You were kicked for bad input!\n"))
        print(cs.closelabel, gettime(), "Connection closed from", addr[0] + ':' + str(addr[1]), "due to an error")
    finally:
        conn.close()
        print(cs.closelabel, gettime(), "Connection closed from", addr[0] + ':' + str(addr[1]))

# Server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_start_time = time.time()

try:
    s.bind((host, port))
    print(cs.good, gettime(), "Server started on", host + ':' + str(port) + '!')
except socket.error as e:
    print(str(e))

s.listen(128)
print(cs.status, gettime(), "Waiting for connections...")

try:
    while True:
        conn, addr = s.accept()
        start_new_thread(client, (conn, addr))
except KeyboardInterrupt:
    print("\n" + cs.status, gettime(), "Stopping server...")
finally:
    s.close()
    server_end_time = int(time.time() - server_start_time)
    print(cs.good, gettime(), "Server stopped!")
    print(cs.status, gettime(), "Ran for", str(server_end_time // 86400) + "days", str(server_end_time % 86400 // 3600) + "hrs", str(server_end_time % 3600 // 60) + "min", str(server_end_time % 60) + "sec")

