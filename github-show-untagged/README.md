# gh-show-untagged #

`gh-show-untagged` is a very simple command line tool that will query
each of the given users source repos and list those that do not
have any tags.

While the only required argument is `username`, which can be passed with
`-u` or as a bare argument, you should also set a GitHub Personal
access token in the `GITHUB_TOKEN` environment variable otherwise you'll
very quickly find your requests throttled by GitHub

    Usage:
      gh-show-untagged <username>
      gh-show-untagged <-u username>

      -u, --user USER                  github user to query.
      -h, --help

## Installation ##

The install is currently both simple and very manual:

    git clone https://github.com/deanwilson/sysadmin-scripts.git
    cd github-show-untagged

    bundle install
    bundle exec ruby gh-show-untagged -h

    # set GITHUB_TOKEN as above if you plan to use it much.

## Notes ##

This is a very quick play with the github api gem and lacks things like
exception handling around the remote calls and confirming the auth
worked. I expect to return and add those once I've played with the gem
some more.

### Author ###
[Dean Wilson](http://www.unixdaemon.net)
