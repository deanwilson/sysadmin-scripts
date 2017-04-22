# sysadmin-scripts

## py-prioritise

A script to help you prioritise a list of things (such as tasks)
interactively.

    $ cat objectives
    top
    middle
    above bottom
    bottom

Run the script and answer the 'simple' question of which of the two
things are the most important. Repeatedly.

    $ py-prioritise objectives
    Is middle more important than top ('y' for yes)? n
    Is above bottom more important than top ('y' for yes)? n
    Is bottom more important than top ('y' for yes)? y
    Is middle more important than top ('y' for yes)? n
    Is above bottom more important than top ('y' for yes)? y
    Is middle more important than top ('y' for yes)? y
    The most important task is: bottom
    The final ordering is ['bottom', 'above bottom', 'middle', 'top']

We end up with an ordered list of items and the first one to start on.
