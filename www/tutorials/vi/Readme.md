# vi Tutorial
# Introduction
Quick cheat sheet to use VI editor
# Starting Vi
Start editing existing file using
    # vi file-name
Create new file
    # vi new-file-name
Strat editing from line 90
    # vi +90 file-name
# Closing
Quit editor
    # :q
Force full quit of editor
    # :q!
# Modes
When you start vi, you are placed in command mode
## Command Mode
You can run commands in command Mode. You can search in command mode


    h - move left one character
    j - move down one character
    k - move up one character
    l - move right one character  

## Input Mode
    Press i for input mode
    Press esc to back into command mode
# Most used commands

    dd - for deleting file
    yy - for copying line
    p  - for pasting
    :r file-name - For reading text from another file
    /search-text - For searching from top to bottom
    ?search-text - For searching from bottom to top
    n - for next search item text top to bottom
    N - for next search item text from bottom to top
    O or o- To insert a new line above our below the current line
    r - for replacing the text under cursor
