#!/usr/bin/env python3
"""Set the topics assigned to GitHub repos."""
import argparse
import os
import sys

from github import Github


def valid_topic(topic):
    """Return true if the supplied string is a valid topic."""

    if not topic[0].islower():
        return False

    if len(topic) < 1 or len(topic) > 35:
        return False

    return True


def get_token():
    """Fetch the GitHub Authentication token from the environment."""
    try:
        "GITHUB_AUTH_TOKEN" in os.environ
    except KeyError:
        print("Please set the environment variable GITHUB_AUTH_TOKEN")
        sys.exit(1)

    return os.environ["GITHUB_AUTH_TOKEN"]


def main(args):
    token = get_token()

    g = Github(token)

    for org_repo in args.repos:
        if args.verbose:
            print(f""" == Repo {org_repo}""")

        repos = g.search_repositories(query=f"repo:{org_repo}")
        repo = repos[0]

        combined_topics = repo.get_topics()

        if args.verbose:
            print(f""" >> Repo: {org_repo} has topics {",".join(combined_topics)}""")

        for topic in args.topics:
            combined_topics.append(topic)

        combined_topics.sort()
        unique_topics = set(combined_topics)  # set to remove duplicates

        repo.replace_topics(list(unique_topics))  # set to remove duplicates

        if args.verbose:
            print(f""" << Repo: {org_repo} has topics {",".join(repo.get_topics())}""")


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Set GitHub Repo Tokens")

    parser.add_argument(
        "--verbose",
        default=False,
        action="store_true",
        help="Show additional information while running.",
    )

    parser.add_argument(
        "--repos",
        nargs="+",
        required=True,
        help="Repos to update. Given in the username/reponame format.",
    )

    parser.add_argument(
        "-t",
        "--topics",
        nargs="+",
        help="One or more topics to apply to the GitHub repositories",
        required=True,
    )

    args = parser.parse_args()

    main(args)
