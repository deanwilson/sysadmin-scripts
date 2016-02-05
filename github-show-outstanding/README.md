# gh-show-outstanding #

`gh-show-outstanding` is a small command line tool that will query each
of the given users repos and list those that have either or both an
issue or pull request raised against them. have any tags.

While the only required argument is `username`, which can be passed with
`-u` or as a bare argument, you should also set a GitHub Personal access
token in the `GITHUB_TOKEN` environment variable otherwise you'll very
quickly find your requests throttled by GitHub

Usage:
  -a, --all                        show all repos
  -H, --no-header                  do not display the output header
  -u, --user USER                  github user to query.
  -h, --help                       Show this message


Sample output:

    Reponame                                Issues   PRs
    puppet-lint-no_symbolic_file_modes-check     1     0
    puppet-scripts                               2     6
    yum-transaction-json                         0     1


Limitations:
  Currently only works for a users own repos, not those from an
  organisation.

## Installation ##

The install is currently both simple and very manual:

    git clone https://github.com/deanwilson/sysadmin-scripts.git
    cd github-show-outstanding

    bundle install
    bundle exec gh-show-outstanding deanwilson

    # set GITHUB_TOKEN as above if you plan to use it much.

## Notes ##

This is a very quick play with the github api gem and lacks things like
exception handling around the remote calls and confirming the auth
worked. I expect to return and add those once I've played with the gem
some more.

### Author ###
[Dean Wilson](http://www.unixdaemon.net)
