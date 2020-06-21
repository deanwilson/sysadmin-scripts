# get-default-github-branch

Query a user or organisations repositories and display the default branch name

`get-default-github-branch` is a small ruby script that uses the 
[github_api](https://rubygems.org/gems/github_api/) gem
to query the repositories of the provided user or org and display the default
branch name for each of them.

## Installation

Using this command is currently very manual:

    git clone https://github.com/deanwilson/sysadmin-scripts.git
    cd sysadmin-scripts/default-github-branch

    bundle install --path vendor/bundle

    # set GITHUB_TOKEN if you hit API rate limits
    bundle exec ruby get-default-github-branch --user deanwilson
    ...
    alexa-skill-registered-domain default branch of master
    alexa-skill-webstatuscode default branch of master
    ...

### Author
 * [Dean Wilson](http://www.unixdaemon.net)
