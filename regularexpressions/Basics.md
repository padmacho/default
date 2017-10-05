# Basics
- Pattern
- Regex
- Subject


# grep
grep is a command-line utility for searching plain-text data sets for lines that match a regular expression. Its name comes from the ed command g/re/p (globally search a regular expression and print)

g/<regular expression>/p

# Regex Standards
- BRE (POSIX) Basic Regular expression
- ERE (POSIX) Extended Regular expression
- PCRE Perl Compatible Regular expression
 POSIX - Portable Operating System Interface for uniX

## Pattern
Determine the Pattern that you want to match
## Regex
Create a rule that matches your Pattern
## Subject
Input to expression normally text string or group of text strings
## Function
Takes regex and input and is given a input to regex engine
## Engine
executes regular expressions
## Result
Result of evaluation
There are three types
- Boolean - Does it match?
- Integer - How may matches have been found?
- Array - What are the matches ?

# First regular expressions
Validate html color code when it is givn as input
## Rules for html color code
Now what pattern does an HTML hex color code follow? It generally starts with a hash and is then followed by six characters. Each of these characters has to be within the range A to F and 0 to 9, and the three sets of two characters together build up the color in red, green, and blue. In this case, every single combination of characters between #000000 and #FFFFFF is valid
- Valid color codes
 - #000000
 - #FFFFF
 - #ABC
- Invalid
 - #GAB

## Lets use grep
```bash
grep -o
```
 Print only the matched (non-empty) parts of a matching line, with each such part on a separate output line
 Lets try to match ABCDEF chars in a given string

```bash
dragon@airavath ~                             
$ echo "ABCDEF" | grep -o ABCDEF              
ABCDEF                                        

dragon@airavath ~                             
$ echo "ABCDEF123ABCDEF" | grep -o ABCDEF     
ABCDEF                                        
ABCDEF                                        

dragon@airavath ~                             
$ echo "ABCDEF" | grep -o ABCDEF              
ABCDEF                                        

dragon@airavath ~                             
$ echo "ABC" | grep -o ABCDEF                 

```
The pattern ABCDEF is matched from the string

```bash

```
