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