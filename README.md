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

## show-process-environment

Show the environment of another process in a prettier way than `cat`ting
`/proc/$pid/environ`. If no process id is provided it defaults to the current
process.

    show-process-environment 34234 | grep QT

    QTDIR == /usr/lib64/qt-3.3
    QTINC == /usr/lib64/qt-3.3/include
    QTLIB == /usr/lib64/qt-3.3/lib
