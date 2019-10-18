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
