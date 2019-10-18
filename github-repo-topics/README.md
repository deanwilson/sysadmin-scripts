# GitHub Repository Topics

Tools to allow easier bulk viewing of GitHub Repository topics

## Installing

 * Clone this repository
    - `cd sysadmin-scripts/github-repo-topics`
 * Enable python3 virtual environments
    - `python3 -m venv venv`
 * Active the virtual environment
    - `source venv/bin/activate`
 * Install the dependencies
    - `pip install -r requirements.txt`

## get-topics.py

Get topics fetches a list of repositories for each specified organisation and prints them as comma separated values ready for importing to Google Sheets or Excel

To run the command, first set your GitHub auth token

    export GITHUB_AUTH_TOKEN=aaaaa7a2333345677883456898347845677

And then run the command, specifying the organisation to query.

    ./get-topics.py -o deanwilson

By default it will not include archived repos in the output. You can
include them by specifying the `--archived` flag.

You can optionally exclude repositories that contain one of a given set
of labels. This can help you identify repos that do not match your
metadata scheme. This example will skip any repos that have a topic of
`function` or `terraform`

    ./get-topics.py -o deanwilson -e function terraform

## edit-topics.py

This small script allows you to specify one or more repositories, in the
`orgname/reponame` format and set their labels to the values you provide.

    ./edit-topics.py --dry-run --topics ansible automated --repos deanwilson/ansible-plugins --verbose

The `--dry-run` option specified in the command above will show the before and possible after
state of running without actually making the change.

*WARNING* by default this script does not add to the existing topics, it
completely replaces them. You can specify the `--preserve` flag to add
your supplied values to the existing topics When running under verbose
`edit-topics.py` outputs the topics before they are overwritten which
may allow you to remedy any mistakes.

