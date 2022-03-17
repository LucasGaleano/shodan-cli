# shodan-client

## How it works
Create a config file name shodan.conf with this information in the root directory. (there is a example file in the repository)

```
[shodan]
token = tokenKey

[email]
from = example@example.com
to = example@example.com
subject = Subject Testing
server = server.example.com
```
Add the uncommon ports into the file "uncommonPorts"

Don't forget the pip3 install -r requirements.txt

## What it does
Checks the monitoring feature of shodan looking for ports on the configurate networks, will report the new ports, the common ports and the uncommon ports according to "uncommonPorts" file.
The script creates and maintances a database in the "ddbb" file with all the IP and port found by it.
With the --email-vulns parameters the script will send a vulnerability report to an email every time it found a IP with vulnerabilities.

## Logging
The script will log all the events to log.json as a json format and to /var/log/syslog as a syslog format
