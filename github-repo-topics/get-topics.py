#!/usr/bin/env python3
"""Query GitHub for repos and their topics and generate CSV from the results."""
import argparse
import os
import sys
import time

from github import Github


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

    org_repos = {}
    count = 0

    for org in args.org:
        org_repos[org] = {}

        for repo in g.search_repositories(query=f"user:{org}"):
            count += 1

            if args.size:
                if count % args.size == 0:
                    time.sleep(args.delay)

            if repo.archived and not args.archived:
                continue

            topics = repo.get_topics()

            if set(args.exclude).intersection(topics):
                continue

            org_repos[org][repo.name] = {}
            org_repos[org][repo.name]["topics"] = topics
            org_repos[org][repo.name]["url"] = repo.html_url

    print("Github_Organisation, Repository_name, Repository_URL, topics")
    for org in org_repos:
        for repo in sorted(org_repos[org]):
            url = org_repos[org][repo]["url"]
            topics = org_repos[org][repo]["topics"]
            topics.sort()

            print(f"""{org}, {repo}, {url}, {", ".join(topics)}""")


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Query GitHub for repo topics")

    parser.add_argument(
        "--archived",
        default=False,
        action="store_true",
        help="Include archived repos in the results. Defaults to false.",
    )

    parser.add_argument(
        "--size",
        "--batch-size",
        type=int,
        default=None,
        help="Split requests into groups of this size to avoid API limits",
    )

    parser.add_argument(
        "--delay",
        "--batch-delay",
        type=int,
        default=3,
        help="Number of seconds to sleep between batches",
    )

    parser.add_argument(
        "-e",
        "--exclude",
        nargs="+",
        default=[],
        help="Exclude any repos with topics matching the supplied values",
    )

    parser.add_argument(
        "-o",
        "--org",
        nargs="+",
        help="One or more GitHub organisation names",
        required=True,
    )

    args = parser.parse_args()

    main(args)
