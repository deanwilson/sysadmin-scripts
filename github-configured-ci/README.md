# list-configured-ci

Query a user or organisations repositories and display the continuous integration systems it has configured

`list-configured-ci` is a small ruby script that uses the 
[github_api](https://rubygems.org/gems/github_api/) gem
to query the repositories of the provided user or org and list any
continuous integration systems it can detect the configuration files
for.

## Installation

Using this command is currently very manual:

    git clone https://github.com/deanwilson/sysadmin-scripts.git
    cd sysadmin-scripts/github-configured-ci

    bundle install --path vendor/bundle

    # set GITHUB_TOKEN if you hit API rate limits
    bundle exec ruby list-configured-ci --user deanwilson
        ... snip ...
        puppet-lint-yumrepo_gpgcheck_enabled-check
          - Travis CI
          - Jenkins
        puppet-lint_duplicate_class_parameters-check
          - Travis CI
          - Jenkins
        puppet-multitemplate
          - CircleCI
          - Jenkins
        ... snip ...

### Author
 * [Dean Wilson](http://www.unixdaemon.net)
