# GitHub Pull Request statistics

Show a short summary of the Pull Request statistics in a repository

## Introduction

Run the command against a repo

    ./github-pr-timings.py gds-operations/puppet-graphite

    Closed summary for ['gds-operations/puppet-graphite']
    ==========
    Total Pull Requests == 10
    Longest time before closing == 535
    Shortest time before closing == 2
    75 Percentile of days before closing == 104.75
    95 Percentile of days before closing == 352.30
    Median days before closing == 94.5
    
    Merged summary for ['gds-operations/puppet-graphite']
    ==========
    Total Pull Requests == 10
    Longest time before closing == 28
    Shortest time before closing == 2
    75 Percentile of days before closing == 10.00
    95 Percentile of days before closing == 20.80
    Median days before closing == 8.0


## Installing

 * Clone this repository
    - `cd sysadmin-scripts/github-pull-request-statistics`
 * Enable python3 virtual environments
    - `python3 -m venv venv`
 * Active the virtual environment
    - `source venv/bin/activate`
 * Install the dependencies
    - `pip install -r requirements.txt`

## Running github-pr-timings.py

To run the command, first set your GitHub auth token

    export GITHUB_AUTH_TOKEN=aaaaa7a2333345677883456898347845677

And then run the command, specifying the repository to query.

    ./github-pr-timings.py gds-operations/puppet-graphite

The command will query all the pull requests related to that repository
and display a short summary of some interesting statistics.

## Notes

The output does not include pull requests raised and closed in a single
day in its statistics.

The script currently only reports on pull request that have been merged
into master. It does not include those that were closed instead.
