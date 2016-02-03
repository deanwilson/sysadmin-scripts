# forge-lister #

## Introduction ##

forge-lister is a simple command line tool that will fetch all
the modules for the given user and display their names, newest release
and the date that release was uploaded. The dates are colour coded
to show releases older than 'now - threshold' in days.

The only required argument is `username`, which can be passed with
`-u` or as a bare argument.

    Usage:
      forge-lister username [options]
      forge-lister -u username [options]

      forge-lister -u deanwilson -t 120
      -a, --agent AGENT          User agent string sent to puppetforge
      -u, --user USER            puppetforge user to query.
      -s, --score SCORE          module score threshold we consider acceptable. Defaults to 4.0
      -t, --threshold THRESHOLD  in days. Defaults to 30
      -h, --help                 Show this message

## Output ##

An example run against my current modules looks like this (without colour) -

    bundle exec ruby forge-lister deanwilson -t 120

    deprecate 0.0.2 2015-11-27
    hiera_envvar 1.0.0 2015-03-30
    ip_in_range 0.0.3 2015-11-27
    ipv4_octet 0.0.3 2015-11-27
    liquidtemplates 0.0.4 2015-11-27
    multitemplate 1.0.2 2015-11-27
    surround 1.0.0 2015-11-27
    validate_json_schema 0.0.1 2015-11-27

### Author ###
[Dean Wilson](http://www.unixdaemon.net)
