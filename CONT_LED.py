import network
import socket
from time import sleep
from machine import PWM ,Pin as pin
ssid='TT_DE28'
password ='imed@2024'
led = pin(26 , pin.OUT)
import utime

def connect () :
	wlan = network.WLAN(network.STA_IF)
	wlan.active(True)
	wlan.connect(ssid,password)
	while not wlan.isconnected():
		print('waiting for connection')
		sleep(0.1)
	print(wlan.ifconfig())
	ip = wlan.ifconfig()[0]
	print(ip)
	return ip

def open_socket(ip):
	address = (ip,80)
	connection = socket.socket()
	connection.bind(address)
	connection.listen(1)
	return connection

def web_page():
	html = """<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Home automation</title>
</head>
<body>
	<form action="/ON">
		<input type="submit" value="ON " name=""/>
	</form>
	<form action="/OFF" >
		<input type="submit"value="OFF " name="">
	</form>

</body>
</html>"""
	return str(html)

def ultrason( ):
    v = 0.034
    dis = temp = x2 = x = 0
    trig.on()
    utime.sleep_us(150)
    trig.off()
    while echo.value() == 0 :
        x= utime.ticks_us()
        
    while echo.value() == 1 :
        x2 = utime.ticks_us()
    temp = x2 - x
    print(temp,'temp')
    dis = int( temp * v /2) 
    print(dis,"distance")
    return (dis)

def serve (connection):
	while True :
		client = connection.accept()[0]
		request = client.recv(1024)
		request = str(request)
		if'/OFF' in request:
			in1.off()
			in2.off()
		if '/ON' in request :
			dis = ultrason()    
			if dis < 400 :
				print("///////")
				in1.on()
				in2.off()
				sleep(2)
				
				
			
			
	
		
		html = web_page()
		reponse = "HTTP/1.1 200 OK\r\n"
		reponse +="Content-Type: text/html\r\n\n"
		reponse += html
		
		client.send(reponse)
		client.close()

try:
	ip = connect()
	connection = open_socket(ip)
	serve(connection)
except KeyboardInterrupt:
	machine.reset()
			
		