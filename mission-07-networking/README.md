# Mission 7 — How computers communicate

## 1. Task / objective
The objective of Mission 7 is to understand computer networks, communication protocols, and Internet infrastructure:
- Explain foundational networking concepts (LAN, MAN, WAN, DNS, Router, Protocol, Packet switching, Client-server) with real-world examples.
- Conduct connectivity and DNS resolution tests from macOS Terminal using `ping` and `nslookup`.
- Detail the end-to-end journey of a web request when opening a website in a browser using precise technical terminology (client, server, DNS, protocol, router, response).

---

## 2. Work completed

### Task 7.1 — Explain network concepts

| Concept | Explain it in your own words | Example |
| :--- | :--- | :--- |
| **LAN (Local Area Network)** | A high-speed network confined to a small, localized physical area such as a single home, classroom, or office building. | A home Wi-Fi network connecting a laptop, phone, and wireless printer. |
| **MAN (Metropolitan Area Network)** | A network covering a larger geographical footprint than a LAN, typically spanning an entire city, municipal area, or sprawling university campus. | A university fiber backbone linking academic departments across a city campus. |
| **WAN (Wide Area Network)** | A telecommunications network that spans vast geographical distances, connecting multiple cities, countries, or continents. | The global public Internet connecting millions of devices worldwide. |
| **DNS (Domain Name System)** | A distributed database system that translates human-friendly website domain names into machine-readable IP addresses. | Translating `example.com` into the IP address `172.66.147.243`. |
| **Router** | A networking device that forwards data packets between different networks by inspecting IP destination headers. | A home Wi-Fi router directing data between household devices and the Internet Service Provider (ISP). |
| **Protocol** | A standardized set of rules and syntax formatting that defines how electronic devices transmit and receive data across a network. | HTTPS (Hypertext Transfer Protocol Secure) for secure, encrypted web browsing. |
| **Packet switching** | A communication method where digital data is divided into small blocks (packets), routed independently across networks, and reassembled at the destination. | Streaming video files or sending emails over the Internet without dedicating a continuous physical line. |
| **Client-server** | A structural computing architecture where client applications request data or services from centralized server machines that fulfill those requests. | A web browser (client) requesting web documents from a remote web hosting server. |

---

### Task 7.2 — Observe network information

#### 1. Connectivity Test (`ping`):
Executed in Terminal:
```bash
ping -c 3 example.com
```
**Observed Output (privacy-safe):**
```text
PING example.com (172.66.147.243): 56 data bytes
64 bytes from 172.66.147.243: icmp_seq=0 ttl=54 time=79.603 ms
64 bytes from 172.66.147.243: icmp_seq=1 ttl=54 time=20.942 ms
64 bytes from 172.66.147.243: icmp_seq=2 ttl=54 time=188.830 ms

--- example.com ping statistics ---
3 packets transmitted, 3 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 20.942/96.458/188.830/69.569 ms
```

#### 2. DNS Lookup Test (`nslookup`):
Executed in Terminal:
```bash
nslookup example.com
```
**Observed Output (privacy-safe):**
```text
Server:		1.1.1.1
Address:	1.1.1.1#53

Non-authoritative answer:
Name:	example.com
Address: 104.20.23.154
Name:	example.com
Address: 172.66.147.243
```

#### Analytical Answers:
- **What a connectivity test helps check:**
  A tool like `ping` tests whether a remote destination host is reachable across the network, verifies that intermediate routing paths are functioning, and measures network latency (round-trip time in milliseconds) and packet loss percentage. However, it cannot verify whether an application service (like a web server or database) is running properly if ICMP traffic is blocked by a firewall.
- **What information a DNS lookup displays:**
  A DNS lookup reveals which IP addresses (both IPv4 and IPv6) are associated with a human-readable domain name, along with the IP address and port of the DNS resolver server that answered the query.
- **The role of DNS when entering a website name in a browser:**
  Humans easily memorize names (like `example.com`), but network routers exclusively route packets using numerical IP addresses (like `172.66.147.243`). DNS serves as the Internet's address directory: before any web content can be requested, the browser queries DNS to find the server's exact IP address.

---

### Task 7.3 — What happens when you open a website?

1. **Client URL Entry:** The user enters a website URL (e.g., `https://example.com`) into the web browser, which acts as the **client**.
2. **DNS Resolution:** The client checks its local cache and queries a **DNS** server to translate `example.com` into the numerical destination IP address (`172.66.147.243`).
3. **Establishing Connection via Protocol:** The client initiates a TCP three-way handshake and TLS cryptographic negotiation over the network to establish a secure, reliable communication channel with the server.
4. **Packet Routing:** Data packets containing the connection request travel across local network equipment and intermediate Internet **routers**, which inspect IP headers to forward packets along the fastest available path.
5. **Client HTTP Request:** The client sends an HTTP GET request **protocol** message asking for the webpage document.
6. **Server Processing and Response:** The destination web **server** receives the request, processes it, and transmits an HTTP **response** packet stream containing a status code (e.g., `200 OK`) and the webpage HTML, CSS, and script assets back through the **routers**.
7. **Client Rendering:** The browser (**client**) receives the response packets, reassembles them, parses the HTML/CSS markup, executes JavaScript, and displays the completed webpage on screen for the user.

---

## 3. Commands / tools used
- `ping -c 3 example.com`: Tested network packet transmission, reachability, and round-trip latency.
- `nslookup example.com`: Performed DNS query to resolve public domain names to IPv4 addresses.

---

## 4. My understanding
- The Internet functions as a network of networks bound together by standardized communication protocols (such as IP, TCP, and HTTP/HTTPS).
- Packet switching is resilient because individual packets can take different physical routes to bypass network congestion before being accurately reassembled by the receiving host.
- DNS is the invisible foundation of the modern web: without automated domain resolution, users would need to memorize numerical IP addresses for every service.

---

## 5. Difficulties faced
- Understanding why a `ping` command might occasionally fail or hang even when a website opens fine in a browser.

---

## 6. How I resolved them
- Discovered that `ping` uses the ICMP protocol, which many corporate and cloud firewalls deliberately drop or block to prevent scanning, whereas web traffic uses TCP on ports 80/443.

---

## 7. Evidence / files
- `mission-07-networking/README.md`: Contains complete networking concepts table, terminal outputs for `ping` and `nslookup`, and the 7-step website request lifecycle.

---

## 8. Commit details
- **Commit message:** `Explain networking concepts and website communication`
- **Branch:** `main`
- **Status:** Ready to stage and commit.
