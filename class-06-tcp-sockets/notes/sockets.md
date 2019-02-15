# Sockets

The Application Layer needs not and does not know about the functionality of the lower layers. Given that data needs to be communicated through the Application layer though, Sockets provide a way for that communication to occur.

A Socket is a representation in software of several key components from layers within the OSI model:
- Internet layer provides an **IP Address**
- Transport layer provides the concept of a **Port**
- Application layer doesn't care about the lower layers, but allows the data communication through an **Endpoint (IP:Port)**

Opening a socket creates the ability for sending and/or receiving of bytes at a given **Endpoint**

## Sockets in Python
Python provides a standard built-in module for working with sockets, called `socket`. The module is a wrapper around the system's implementation of [BSD Sockets](https://en.wikipedia.org/wiki/Berkeley_sockets){:target="_blank"}. Below is a brief introduction to working with the `socket` module:
```python
In [2]: import socket
# Create a socket by using the `.socket` method provided by the module. It takes three _optional_ arguments: Family, Type, and Proto.
In [3]: foo = socket.socket()
In [4]: foo
Out[4]: <socket.socket fd=11, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('0.0.0.0', 0)>
```

To evaluate the default values provided by creating a new Socket, we can simply evaluate those properties on `foo`:
```python
In [5]: foo.family
Out[5]: <AddressFamily.AF_INET: 2>

In [6]: foo.type
Out[6]: <SocketKind.SOCK_STREAM: 1>

In [7]: foo.proto
Out[7]: 0
```

## Socket Families
The `family` of the socket corresponds back to the _addressing system_ (IPv4/IPv6) it uses for connecting. Families defined in the socket library are prefixed with `AF_` (AddressFamily):
```python
# Note that you may see a slightly different output if you were to review the AddressFamily constants on `socket`.
{<AddressFamily.AF_UNSPEC: 0>: 'AF_UNSPEC',
 <AddressFamily.AF_UNIX: 1>: 'AF_UNIX',
 <AddressFamily.AF_INET: 2>: 'AF_INET',
 <AddressFamily.AF_SNA: 11>: 'AF_SNA',
 12: 'AF_DECnet',
 <AddressFamily.AF_APPLETALK: 16>: 'AF_APPLETALK',
 <AddressFamily.AF_ROUTE: 17>: 'AF_ROUTE',
 <AddressFamily.AF_LINK: 18>: 'AF_LINK',
 <AddressFamily.AF_IPX: 23>: 'AF_IPX',
 <AddressFamily.AF_INET6: 30>: 'AF_INET6',
 <AddressFamily.AF_SYSTEM: 32>: 'AF_SYSTEM'}
```

Of that list, there are two that we need to generally keep in mind: `2` and `30`, or `AF_INET` and `AF_INET6`. These two families allow our sockets to connect via IP addressing and Ports. You may also find it useful to issue socket process communications from the same machine, which would require the use of `1` or `AF_UNIX`. The default family is IPv4.

## Socket Types
The socket type determines how that socket will function before, during, and after communications; allow for two-way data flow; remain open, close immediately; etc.  Types defined in the socket library are prefixed with `SOCK_`:
```python
{<SocketKind.SOCK_STREAM: 1>: 'SOCK_STREAM',
 <SocketKind.SOCK_DGRAM: 2>: 'SOCK_DGRAM',
 <SocketKind.SOCK_RAW: 3>: 'SOCK_RAW',
 <SocketKind.SOCK_RDM: 4>: 'SOCK_RDM',
 <SocketKind.SOCK_SEQPACKET: 5>: 'SOCK_SEQPACKET'}
 ```

 The most common types of sockets are `1` and `2`, or `Stream Communications (TCP)` and `Datagram communications (UDP)`. The default type is TCP.

 ## Socket Protocols
Each socket is provided a default protocol of `0` or `IPPROTO_IP`. The protocol, not just the default, controls which internet layer protocol will be used to wrap and unwrap data through a socket. Protocols defined in the socket library are prefixed with `IPPROTO_`:
```python
{0: 'IPPROTO_IP',
 1: 'IPPROTO_ICMP',
 2: 'IPPROTO_IGMP',
 3: 'IPPROTO_GGP',
 4: 'IPPROTO_IPV4',
 6: 'IPPROTO_TCP',
 8: 'IPPROTO_EGP',
 12: 'IPPROTO_PUP',
 17: 'IPPROTO_UDP',
 22: 'IPPROTO_IDP',
 29: 'IPPROTO_TP',
 36: 'IPPROTO_XTP',
 41: 'IPPROTO_IPV6',
 43: 'IPPROTO_ROUTING',
 44: 'IPPROTO_FRAGMENT',
 46: 'IPPROTO_RSVP',
 47: 'IPPROTO_GRE',
 50: 'IPPROTO_ESP',
 51: 'IPPROTO_AH',
 58: 'IPPROTO_ICMPV6',
 59: 'IPPROTO_NONE',
 60: 'IPPROTO_DSTOPTS',
 63: 'IPPROTO_HELLO',
 77: 'IPPROTO_ND',
 80: 'IPPROTO_EON',
 103: 'IPPROTO_PIM',
 108: 'IPPROTO_IPCOMP',
 132: 'IPPROTO_SCTP',
 255: 'IPPROTO_RAW',
 256: 'IPPROTO_MAX'}
```

## Communicating with other sockets
Given that the purpose of one socket is to communicate with other sockets, you need to design your socket to match the communication profile of the socket you're trying to interact with. The `socket` module provides a useful method for gathering information about that other socket in question: `getaddrinfo()`, which takes two arguments.

The first argument is either an IP address or a hostname. If you use a hostname, DNS (when available) will be used to resolve the IP address. If DNS is unavailable, it will throw an error.

The second argument is either a port number or a protocol name. If you use the name of a protocol, if will be replaced with the most common port number used for that protocol. For example, `http` will be replaced with `80`, and `https` will be replaced with `443`.
```python
In [19]: socket.getaddrinfo('www.codefellows.com', 'http')
Out[19]:
[(<AddressFamily.AF_INET: 2>,
  <SocketKind.SOCK_STREAM: 1>,
  6,
  '',
  ('13.32.178.10', 80)),
 (<AddressFamily.AF_INET: 2>,
  <SocketKind.SOCK_STREAM: 1>,
  6,
  '',
  ('13.32.178.179', 80)),
  # ......
```
The return value seen above will contain a list of 0 or more tuples. The contents of each tuple are ordered by the following:
- Socket Family
- Socket Type
- Socket Protocol
- Canonical Name (generally empty)
- Socket Address (IP, Port)
