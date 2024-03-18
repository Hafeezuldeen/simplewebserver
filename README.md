# EX01 Developing a Simple Webserver
## Date:28-02-2024

## AIM:
To develop a simple webserver to serve html pages.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Serving the HTML pages.

### Step 5:
Testing the webserver.

## PROGRAM:
```
from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html>
<head>
<title>SOFTWARE COMPANY</title>
</head>
<body bgcolor="sky blue">
	<table border="10" cellspacing="10" height="240" width="150" >
<caption>TOP SOFTWARE COMPANIES WITH REVENUE</caption>
		<tr>
			<th>COMPANY</td>
			<th>REVENUE</td>
			<th>PERCENTAGE</td>
		</tr>
		<tr>
			<td>APPLE</td>
			<td>265694999</td>
			<td>1</td>
		</tr>

		<tr>
			<td>LOUIS VUTTION</td>
			<td>554594848</td>
			<td>2</td>
		</tr>

		<tr>
			<td>MICROSOFT</td>
			<td>581849</td>
			<td>3</td>
		</tr>
	</table>
	</body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()
```


## OUTPUT:
![alt text](<Screenshot 2024-03-12 113345.png>)
![Screenshot 2024-03-12 113630](https://github.com/Hafeezuldeen/simplewebserver/assets/144979314/b523be15-6748-47bb-b3fc-329383d8105e)


## RESULT:
The program for implementing simple webserver is executed successfully.
