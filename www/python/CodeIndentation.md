# Code Indentation
- Python uses indentation levels rather than the braces used by other languages to demarcate code blocks.
- By convention, contemporary Python code is indented by four spaces for each level.
- All code blocks in Python code are easily identifiable and everyone writes them the same way.

# Whitespace is significant
In Python whitespace is significant. Block starts with **significant white space**, The block ends when the indentation becomes smaller (less).
```Python
print("Code Indentation Demo")
if True:
    print("Begin of Block")
print("Not part of if block") # Less indentation , not a part of block
```
Even below code style is correct but not recommended. Having four spaces is preferable
```Python
print("Code Indentation Demo")
if True:
 print("Begin of Block")
print("Not part of if block") # Less indentation , not a part of block

```
# Significant Whitespace Rules
- Prefer four spaces
- Never mix spaces and tabs
- Be consistent on consecutive lines
- Only deviate to improve readability

# PEP 8(Python Enhancement Proposals)
 PEP 8 - Style Guide for Python Code.

# [Python Home](index.html) 
