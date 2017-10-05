# Forwarders
Splunk forwarders consume data and send it to an indexer. Forwarders require minimal resources and have little impact on performance, so they can usually reside on the machines where the data originates

For example, if you have a number of Apache Web servers that generate data that you want to search centrally, you can set up forwarders on the Apache hosts. The forwarders take the Apache data and send it to your Splunk deployment for indexing, which consolidates, stores, and makes the data available for searching. Because of their reduced resource footprint, forwarders have minimal performance impact on the Apache servers

There are two types of forwarders
- Universal Forwarder
- Heavy Forwarder
- Light Forwarder (It is deprecated as of Splunk 6.0)

## Universal Forwarder
Its main objective is move data from one machine to another machine

- No Alerts
- No Indexing
- Limited Parsing of Data
- CLI Configuration

## Heavy Forwarder
It is equivalent to full blown instance of splunk
- Full SplunkInstance
- Disable Features
- Web/CLI Configuration

# Benefits of Forwarding
- Helps splunk to run in distribute environment
- Encryption - Data is send in encrypted format
- Compression- Data is compressed while send to have better performance

# Using Forwarder
- Download Forwarder
- Run install
- Change directories
- Start Forwarder
- Change Config

# Installing splunk forwarder on ubuntu

```bash
sudo dpkg -i splunkforwarder-6.6.2-4b804538c686-linux-2.6-amd64.deb

Selecting previously unselected package splunkforwarder.                                     
(Reading database ... 64016 files and directories currently installed.)                      
Preparing to unpack splunkforwarder-6.6.2-4b804538c686-linux-2.6-amd64.deb ...               
Unpacking splunkforwarder (6.6.2) ...                                                        
Setting up splunkforwarder (6.6.2) ...                                                       
complete                                                                                     
```
# Starting Splunk Forwarder
 Change to forwarder installation /opt/splunkforwarder/bin directory and run as root
```bash
$ sudo ./splunk start

All preliminary checks passed.              

Starting splunk server daemon (splunkd)...  
Done                                        
```
# Config forward servers

```bash
$ sudo splunk add forward-server airavath:9997
```
- airavath is the host on which splunk server is running
- It prompts for username and password  , provide splunk server username and password. by default they are admin/changeme

# Stop splunk forwarders
```bash
mario@myclient:/opt/splunkforwarder/bin$ sudo ./splunk stop
```
# status of splunk forwarders
```bash
mario@myclient:/opt/splunkforwarder/bin$ sudo ./splunk status
splunkd is running (PID: 1665).
splunk helpers are running (PIDs: 1666).
```
### [index](index.html)
