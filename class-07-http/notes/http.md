# HTTP
The Hyper Text Transfer Protocol (HTTP) is a stateless request-response application layer protocol. HTTP is used to build distributed, collaborative, hypermedia information systems. HTTP is the foundation for the world wide web. Applications built using HTTP subscribe to the client-server computing model. In the client-server computing model a host designed to provide a service is called a server and clients are hosts that make requests to the service. The HTTP specification defines how requests and responses should be formatted, but not what a service should represent. HTTP is often associated with serving `.html` files but is also used to transfer images, videos, json, xml, binary executables, and much more.

#### HTTP Requests
A HTTP/1.1 request is formatted in text and transferred using TCP. The first line of the request contains the `METHOD`, `URL`, and `HTTP VERSION`. The following lines are the request `HEADERS`. Each header is separated by a newline character. A header is a key value pair separated using a colon. Headers containing more than one value separate each value using a semicolon. The header section of the request is terminated with an empty line. An optional body follows the header section.


|HTTP Method	| Request Has Body	| Response Has Body |	Safe	| Idempotent	| Cacheable | Function |
| --- | --- | --- | --- | --- | --- | --- |
| GET	    | No	      | Yes	| Yes | Yes	| Yes | Retrieve a resource |
| HEAD	  | No	      | No	| Yes | Yes	| Yes | Like GET but headers only |
| POST	  | Yes	      | Yes	| No	| No	| Yes | Create a resource |
| PUT	    | Yes	      | Yes	| No	| Yes	| No | Update a resource |
| DELETE	| No	      | Yes	| No	| Yes	| No | Delete a resource |
| CONNECT	| Yes	      | Yes	| No	| No	| No | Create TCP/IP tunnel |
| OPTIONS	| Optional	| Yes	| Yes | Yes	| No | Returns supported methods for a URL |
| TRACE 	| No	      | Yes	| Yes | Yes	| No | Echos retrieved request |
| PATCH  	| Yes	      | Yes	| No	| No	| No | Partial modification of resource |

`Safe` methods should only be used for information retrieval and should not change the server state.
`Idempotent` methods means if two identical requests are made they should get an identical response.
`Cacheable` means the client should be able to cache the response.

###### Example HTTP Request
```
POST /api/note HTTP/1.1
Host: api.example.com
Origin: www.example.com
Authorization: Bearer bHVsIHRoaXMgaXMgYSBmYWtlIHNlY3JldCB0b2tlbg==
Accept: application/json
Content-Type: application/json; charset=UTF-8
Content-Length: 58

{"title":"kata","content":"get 100 points on hacker rank"}
```

#### HTTP Response
A HTTP/1.1 response is also formatted in text and transferred using TCP. The first line of the response contains the `HTTP VERSION`, `STATUS CODE`, and `STATUS MESSAGE`. The following lines are the request headers and are formatted exactly the same way as the request headers. The header section of the request is terminated with an empty line. An optional body follows the header section.

###### Example HTTP Response
```
HTTP/1.1 200 OK
Date: Tue, 22 Aug 2017 06:34:16 GMT
Content-Type: application/json; charset=UTF-8
Content-Encoding: UTF-8
Content-Length: 82
Last-Modified: Mon, 21 Aug 2017 12:10:38 GMT
Server: Apache/1.3.3.7 (Unix) (Red-Hat/Linux)
ETag: "3f80f-1b6-3e1cb03b"
Connection: close

{"id":"1234123412341324","title":"kata","content":"get 100 points on hacker rank"}
```


## Python's HTTP Module


Let's take a quick look at how easily we can create a simple server using Python 3s built-in HTTP module.
```sh
# Server shell session
$ python3 -m http.server 8000 --bind 127.0.0.1

Serving HTTP on 127.0.0.1 port 8000 (http://127.0.0.1:8000/) ...
```
Notice the similarities in establishing a server instance and binding an endpoint (address, port) to that instance with the TCP socket server we created yesterday. We're working on an abstraction layer at this point, and while still lower level than a framework like Django or Pyramid, this is quite a bit easier than having to manually define and configure socket connections.


Now that we have an active server running in the shell, unconfigured as it is, we have the ability to make a simple GET request to that endpoint, which will return a HTTP response with a status code of `200 OK`.

_Note: If you examine the results of that HTML response, you'll notice that a valid request will provide a listing of the current working directory where the server is running. *That is a problem!* You own protecting your server from such access, so this is something we would validate and account for when building a server from scratch with the HTTP module._

```sh
# Client shell session

# This is our HTTPie request. HTTPie is an installable CLI tool that allows some nice, simple commands for making http requests in the terminal.
$ http localhost:8000?key=value

# These are the response headers received from our server.
HTTP/1.0 200 OK  # Notice that we're operating on an HTTP/1.0 version? That means that this is the only line ACTUALLY required in these headers
Content-Length: 573  # Content length... self explanatory? This is the length of the body of the response.
Content-type: text/html; charset=utf-8  # Content type provides a way for the req/res cycle to predetermine the type of data sent and received: i.e. JSON, HTML, Plain text, etc...
Date: Tue, 03 Apr 2018 01:22:33 GMT  # Datetime stamp
Server: SimpleHTTP/0.6 Python/3.6.4  # Server process information

# This is the actual body of the request sent back from the server.
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<title>Directory listing for /?key=value</title>
</head>
<body>
<h1>Directory listing for /?key=value</h1>
<hr>
<ul>
<li><a href="FACILITATOR.md">FACILITATOR.md</a></li>
<li><a href="LAB.md">LAB.md</a></li>
<li><a href="lecture/">lecture/</a></li>
<li><a href="notes/">notes/</a></li>
<li><a href="README.md">README.md</a></li>
<li><a href="solutions/">solutions/</a></li>
</ul>
<hr>
</body>
</html>
```
After we've run our HTTP request from the 'client shell' we can see that in our 'server shell' there's now a log of that request made to our server!
```sh
# Server shell session
$ python3 -m http.server 8000 --bind 127.0.0.1

Serving HTTP on 127.0.0.1 port 8000 (http://127.0.0.1:8000/) ...

# ...previous output above & server receiving request from client below
127.0.0.1 - - [02/Apr/2018 18:22:33] "GET /?key=value HTTP/1.1" 200 -
```
