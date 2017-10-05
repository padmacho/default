# Splunk Architecture

# Terms
To Visualize a log file
- Ingest log
- Index log
- Visualize Data
Ingest log is feed the log files to Splunk
Index the log file on timestamp
Visualize it using charts ..etc

# Architecture

## Splunk
It is Ingest engine of splunk

## Splunk Server
Splunk web is using to Visualize the Data
Splunk cli can also be used

# index
The index is the repository for Splunk Enterprise data. Splunk Enterprise transforms incoming data into **events**, which it stores in indexes.
# events
Event is a single entity

# Search
Search for the events

# Pivot
It is a visualization it can be chart , table ..etc. The data for the Pivot comes from the search

# Dashboard
It is the Collection of pivots

# Forwarder
It is a script which transfers the data from one device to splunk server

Splunk Universal Forwarder collects data from a data source or another forwarder and sends it to a forwarder or a Splunk deployment



### [index](index.html)
