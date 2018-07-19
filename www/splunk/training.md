# Splunk Training

Can we use Splunk for BigData Analytic tools?
- Because of License cost it is discouraged
Splunk vs ELK?
Splunk has support for all the major log types (i.e) The logs that are received from different log systems

# Splunk has following capabilities

- Dashboard
- Alerting
- Reporting

One of the Key Feature of Splunk that unique from other products  **Operational Intelligence**
ELK is best competitor for splunk.  -- Splunk supports many formats readily available.
Predictive Analysis is available in Splunk
----------------
Splunk has agents to JVMs in competition with Appydnamics /Dynatrace

Routers -> cloud- > app-> web

Splunk doesn't have appliance. It has to be installed using installer

--------
Splunk Enterprise

Splunk receives logs

Majority of file formats doesn't have meta data of log file
# Splunk Components

-  Data Input
-  Source Type (Data inputs find the source type), if appropriate source type is found than appropriate parses are called
- Splunk store all the data in **index**

# Lab   
192.168.2.221
minimum log is 86 KB for splunk to identify source type as Apache webserver

# index
- When to create a new index
- Continuous monitoring

# SPL (Splunk Processing Language)

Total number
index=web clientip="192.168.2.142"| stats sum(bytes)
# Data types
a - Alpha numeric
/# - Numeric
# interact with Splunk three ways
- WebUI
- cli (Scripts)
- API (Developers)

Roles
- Splunk Admin
- Reporting (Splunk Analsys)
- Splunk Developers
- Splunk Apps

All the configurations of splunk is stored on **file**

Python app server runs in python

/opt/splunk/etc/system/default
/opt/splunk/etc/system/local - Contains customization
local is preferred first

Index is folder in Back end
/opt/splunk/var/lib/splunk/web-all

DB Contains
/opt/splunk/var/lib/splunk/web-all

# Enable splunk at start up

./splunk enable boot-start

# Ports
- Splunk Engine/Indexer Runs on 8089 (Management)
- Splunk WebUI 8000
- Document Search engine use **inverted search index algorithm**
- API and CLI uses 8089 port
- Python process or app server 8065

- Sys log can configured to write logs to central log server
# Splunk agents
Agents can be used to forward logs. It is also known as universal forwarder (UF)
Forwarders are not available for all the platforms for example CISCO Routers, Juniper devices etc
- Data input can acts as pull ,to pull data from databases.
- Data input can  be NoSQL,SQL,XL,CSV.
- DBConnect is app used to pull data
# Data input
# Source types
- Splunk automatically detects source types
# Buckets
Index has buckets to control data retention policy etc
# License
The charge based on through put . For example 1 GB per day means through put of 1 GB
# create custom parser

# Dashboard location
/opt/splunk/etc/users/admin/search/local/data/ui/views
HTML Dashboard
/opt/splunk/etc/users/admin/search/local/data/ui/html
# SPL
Search Processing Language

Filter
index=web clientip="192.168.2.142" |
Operations
stats

index=web clientip="192.168.2.142" | stats sum(bytes)

index=web clientip="192.168.2.142"  OR clientip="192.168.2.161"   |  stats count

index=web status=404  AND  (  clientip="192.168.2.176" OR  clientip="192.168.2.110" )

**by default space  is and**

index=web bytes> 200

Projection

index=web bytes>= 200 AND bytes<=250 | table clientip

index=web | table clientip status bytes
## Table
index=web | table clientip, status, bytes
# Remove duplicates
index=web| table clientip | dedup clientip
# Finding unique clients
index=web| table clientip | dedup clientip | stats count
# Group By
index=web | stats sum(bytes) BY clientip

index=web | stats count BY clientip

index=web | stats count BY clientip | where count >=100
# Find by client ip
index=web | stats count BY clientip | where count >=100 | table clientip

# Eval
Create a new field
index=web |table clientip, method, status , bytes  | eval remarks=if(status==200,"OK","NOT OK")
# Remove a column from out put

- **_internal** index is used for trouble shoot , it contains all the information about every event that happend on splunk server
#fillnull
fill all the colums
index=\_internal | table status, method , bytes| fillnull value=NULL
Fills only specific column

index=\_internal | table status, method , bytes| fillnull value=NULL ,method
# Rename Alias column
index=web |stats sum(bytes) AS SUM
# Aggregation
index=web  |  stats sum(bytes) AS SUM, avg(bytes) AS AVG, min(bytes) AS MIN, max(bytes) AS MAX by clientip
# Eval
index=web  |  eval bytes=bytes/1024 ."KB"
- Round Function
index=web  |  eval bytes=round(bytes/1024,2)."KB"| table bytes
- replace elements in column
index="web" | table method| replace GET with DOWNLOAD in method
# Rename field names
index="web" | table method, clientip| rename clientip AS src_ip
This is not equivalent to **AS**
# Create a permanent Alias

# Multiple Aggregation
index=web | stats sum(bytes) AS SUM BY clientip,file| where SUM > 700
# chart
index=web | chart sum(bytes) AS SUM BY clientip,file
# Aggregate result by time
timechart
index=web | timechart count by clientip
Span
index=web | timechart span=1m count by clientip
index=web | timechart span=1s count by clientip
# Field extraction
index=\_internal| table referer | dedup referer | rex field=referer https://.*/(?<path>.*)
# sed
index=web| rex field=\_raw mode=sed s/GET/DOWNLOAD/
As a complete string
index=login "Failed password for"
index=login Failed password for
event types and tags needs to be created. Before using them
# event types
index=login  eventtype="critical-event"
# Tags
index=web tag=vm1
# Save search
# Macro
function fun-byte(arg1)
{
  index=web clientip="$arg1$" | stats sum(bytes)
}
fun-byte(arg1)
- Call Macro
`fun-byte(arg1)`
`fun-byte(192.168.2.142)`
# CSV File or input look supports
| inputlookup   db.csv  | where remarks="ok"
| inputlookup   db.csv | where name="balaji"
Use lookup under setting to input file
# MV Filter
index=\_internal| table uri| dedup uri| eval field=mvfilter(match(uri,"messages"))
# head and tail
index=\_internal| table message| dedup message| head 100
# Sub Query
Search is basic command behind
search index=net
index=web [ search index=net virus | table host | dedup host | head 1 ]  | stats sum(bytes)
event persecond
index=\_internal sourcetype=splunkd | stats avg(eps)
# Spark line
index=\_internal sourcetype=splunkd | stats sparkline(avg(eps))
# Splunk Apps
/opt/splunk/etc/apps/Splunk_TA_nix

# Splunk agent
Universal Forwarders
Agents run at 
