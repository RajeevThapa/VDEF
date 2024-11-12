# Vulnerability Scan Report

## Nmap Scan Results
# Nmap 7.94SVN scan initiated Tue Nov 12 17:34:22 2024 as: nmap -sV --script vuln -oN /home/rajeev/User_rajeev/AAU/AVDEF/scans/nmap/testhtml5.vulnweb.com_nmap.txt testhtml5.vulnweb.com
Nmap scan report for testhtml5.vulnweb.com (44.228.249.3)
Host is up (0.21s latency).
rDNS record for 44.228.249.3: ec2-44-228-249-3.us-west-2.compute.amazonaws.com
Not shown: 999 filtered tcp ports (no-response)
PORT   STATE SERVICE VERSION
80/tcp open  http    nginx 1.19.0
| http-dombased-xss: 
| Spidering limited to: maxdepth=3; maxpagecount=20; withinhost=testhtml5.vulnweb.com
|   Found the following indications of potential DOM based XSS: 
|     
|     Source: document.write('<div class="fb-comments" data-num-posts="4" data-width="470"  data-href="'+window.location.href+'"></div>')
|_    Pages: http://testhtml5.vulnweb.com:80/static/app/post.js
|_http-stored-xss: Couldn't find any stored XSS vulnerabilities.
| http-csrf: 
| Spidering limited to: maxdepth=3; maxpagecount=20; withinhost=testhtml5.vulnweb.com
|   Found the following possible CSRF vulnerabilities: 
|     
|     Path: http://testhtml5.vulnweb.com:80/
|     Form id: loginform
|_    Form action: /login
| http-enum: 
|   /admin/: Possible admin folder (401 UNAUTHORIZED)
|_  /samples/: Sample scripts

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Tue Nov 12 17:42:06 2024 -- 1 IP address (1 host up) scanned in 464.05 seconds
## ZAP Scan Results
Authentication required

## Nikto Scan Results
- Nikto v2.1.5/2.1.5
+ Target Host: testhtml5.vulnweb.com
+ Target Port: 80
+ GET /: The anti-clickjacking X-Frame-Options header is not present.
+ GET /: Uncommon header 'access-control-allow-origin' found, with contents: *
+ GET /favicon.ico: Server leaks inodes via ETags, header found with file /favicon.ico, fields: 0x51e79f63 0x37e 
+ OPTIONS /: Allowed HTTP Methods: HEAD, OPTIONS, GET 
+ -3092: GET /samples/: /samples/: This might be interesting...
- Nikto v2.1.5/2.1.5
+ Target Host: testhtml5.vulnweb.com
+ Target Port: 80
+ GET /: The anti-clickjacking X-Frame-Options header is not present.
+ GET /: Uncommon header 'access-control-allow-origin' found, with contents: *
+ GET /favicon.ico: Server leaks inodes via ETags, header found with file /favicon.ico, fields: 0x51e79f63 0x37e 
+ OPTIONS /: Allowed HTTP Methods: HEAD, OPTIONS, GET 
+ -3092: GET /samples/: /samples/: This might be interesting...
- Nikto v2.1.5/2.1.5
+ Target Host: testhtml5.vulnweb.com
+ Target Port: 80
+ GET /: The anti-clickjacking X-Frame-Options header is not present.
+ GET /: Uncommon header 'access-control-allow-origin' found, with contents: *
+ GET /favicon.ico: Server leaks inodes via ETags, header found with file /favicon.ico, fields: 0x51e79f63 0x37e 
+ OPTIONS /: Allowed HTTP Methods: HEAD, OPTIONS, GET 
- Nikto v2.1.5/2.1.5
+ Target Host: testhtml5.vulnweb.com
+ Target Port: 80
+ GET /: The anti-clickjacking X-Frame-Options header is not present.
+ GET /: Uncommon header 'access-control-allow-origin' found, with contents: *
+ GET /favicon.ico: Server leaks inodes via ETags, header found with file /favicon.ico, fields: 0x51e79f63 0x37e 
+ OPTIONS /: Allowed HTTP Methods: HEAD, OPTIONS, GET 
+ -3092: GET /samples/: /samples/: This might be interesting...
