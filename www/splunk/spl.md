# SPL (Splunk Processing Language)

SPL is not lucene. SPL is Splunk proprietary Language

# Filtering Results
Allows user to filter Results in queries

```Splunk
source="WinEventLog:*" host="airavath" | search EventCode =100
```
It shows all the events with event code 100

# Remove duplicates
Remove duplicates from search Results

```Splunk
source="WinEventLog:*" host="airavath" | dedup EventCode
```
The above search gets events with unique event code

# Show first ten Results
Use head to get top Results

```Splunk
source="WinEventLog:*" host="airavath" | head 10
```
The above command gets top ten Results from the search

# Show last ten Results
Get last ten Results
```Splunk
source="WinEventLog:*" host="airavath" | tail 10
```

# Reversing the order
```Splunk
source="WinEventLog:*" host="airavath" | reverse
```
# Sort
Sorting in ascending order
```Splunk
source="WinEventLog:*" host="airavath" | sort -EventCode
```
Sort in descending order
```Splunk
source="WinEventLog:*" host="airavath" | sort EventCode
```
# Statistics
Top 10 event codes

```Splunk
source="WinEventLog:*" host="airavath" | top 10 EventCode
```
It gets top 10 event codes

### [index](index.html)
