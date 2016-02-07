# gh-ordered-issues #

`gh-ordered-issues` is a small command line tool that will query each of
the given users repos and list all the open issues and pull requests
against them in chronological order, newest to oldest.

While the only required configuration is `username`, which can be passed
with `-u`, as a bare argument or set by the `GITHUB_USER` environment
variable, you should also set a GitHub Personal access token in the
`GITHUB_TOKEN` environment variable otherwise you'll very quickly find
your requests throttled by GitHub.

Sample output:

    puppet-lint-no_symbolic_file_modes-check  Issue     2016-01-29 13:19:59
    puppet-scripts                            PR        2015-11-03 09:25:47
    puppet-scripts                            Issue     2015-06-19 14:53:51
    puppet-scripts                            PR        2014-07-31 04:00:07
    puppet-scripts                            Issue     2014-07-29 16:06:21
    puppet-scripts                            PR        2014-03-12 10:27:16
    puppet-scripts                            PR        2013-02-11 16:50:29
    puppet-scripts                            PR        2012-10-02 14:48:55
    yum-transaction-json                      PR        2012-06-14 21:11:22
    puppet-scripts                            PR        2011-03-29 21:07:44

Limitations:
 * Currently only works for a users own repos, not those from an organisation.

Usage:

    -u, --user USER                  github user to query.
    -h, --help                       Show this message


## Installation ##

The install is currently both simple and very manual:

    git clone https://github.com/deanwilson/sysadmin-scripts.git
    cd sysadmin-scripts/github-ordered-issues

    bundle install
    bundle exec gh-ordered-issues deanwilson

    # set GITHUB_USER=username as above if you plan to use it much.
    # set GITHUB_TOKEN as described above if you plan to use it much.

## Notes ##

This is a very quick play with the github api gem and lacks things like
exception handling around the remote calls and confirming the auth
worked. I expect to return and add those once I've played with the gem
some more.

### Author ###
[Dean Wilson](http://www.unixdaemon.net)
