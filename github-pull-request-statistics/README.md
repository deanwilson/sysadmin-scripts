# GitHub Pull Request statistics

Show a short summary of the Pull Request statistics in a repository

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


    Summary for ['gds-operations/puppet-graphite']
    ==========
    pull_requests == 20
    longest == 535
    shortest == 2
    Median duration == 20.0
    75 percentile == 89.75
    95 percentile == 149.3000000000003

## Notes

The output does not include pull requests raised and closed in a single
day in its statistics.

The script currently only reports on pull request that have been merged
into master. It does not include those that were closed instead.
