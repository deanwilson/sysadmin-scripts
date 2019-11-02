#!/usr/bin/env python3
"""Query GitHub repo pull requests and show their life cycles."""
import argparse
import datetime
import numpy
import os
import statistics
import sys
import time

from datetime import date
from github import Github


def get_token():
    """Load the GitHub token from the environment."""
    try:
        "GITHUB_AUTH_TOKEN" in os.environ
    except KeyError:
        print("Please set the environment variable GITHUB_AUTH_TOKEN")
        sys.exit(1)

    return os.environ["GITHUB_AUTH_TOKEN"]


def generate_statistics(pull_requests):
    """Iterate through a dict of PRs and generate statistics."""

    # TODO early return if arg is empty

    durations = []

    merged_summary = {
        "pull_requests": 0,
        "longest": 0,
        "shortest": 100000,
    }

    # TODO: pretty display names
    # "longest": { "duration": 0, "display": "Longest duration (days)" }

    for pull_request in pull_requests:
        pr = pull_requests[pull_request]

        merged_summary["pull_requests"] += 1

        if pr["duration"] > merged_summary["longest"]:
            merged_summary["longest"] = pr["duration"]

        if pr["duration"] < merged_summary["shortest"]:
            merged_summary["shortest"] = pr["duration"]

        durations.append(pr["duration"])

    merged_summary["75_percentile"] = numpy.percentile(durations, 75)
    merged_summary["95_percentile"] = numpy.percentile(durations, 95)

    merged_summary["median"] = statistics.median(durations)

    return(merged_summary)


def main(args):
    token = get_token()

    g = Github(token)

    # Single repo for now. Expect to loop over multiple repos soon
    org_repo = args.repo_name[0]

    repos = g.search_repositories(query=f"repo:{org_repo}")
    repo = repos[0]
    repo_name = repo.name

    pull_requests = {}
    closed_prs = repo.get_pulls(state="closed", sort="created", base="master")
    for closed_pr in closed_prs:
        pr_details = {}

        # PRs created and closed on the same day will show as 0
        pr_duration = closed_pr.closed_at - closed_pr.created_at
        pr_details["duration"] = pr_duration.days

        pr_details["number"] = closed_pr.number
        pr_details["title"] = closed_pr.title

        pr_details["ending"] = "merged" if closed_pr.merged_at else "closed"

        pull_requests[closed_pr.number] = pr_details

    merged_prs = {
    if args.verbose:
        print(f" == Working set of {len(pull_requests)} PRs")

        key: value
        for (key, value) in pull_requests.items()
        if pull_requests[key]["ending"] == "merged"
    }

    if args.verbose:
        print(f" == {len(interesting_prs)} PRs resolved after {args.minimum_days} days")

    merged_prs = {
        key: value
        for (key, value) in pull_requests.items()
        if pull_requests[key]["duration"] > args.minimum_days
    }

    summary = generate_statistics(merged_prs)

    print(f"Summary for {args.repo_name}\n==========")
    for metric in summary:
        print(f"""{metric} == {summary[metric]}""")

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Query GitHub repo pull requests")

    parser.add_argument(
        "--from",
        "--since",
        "--start-date",
        dest="start_date",
        default=date.today() - datetime.timedelta(days=30),
        type=lambda d: datetime.strptime(d, "%Y%m%d").date(),
        help="Include Pull Requests created since this date. Specified in YYYYMMDD format",
    )

    parser.add_argument(
        "--min",
        "--minimum",
        dest="minimum_days",
        default=1,
        type=int,
        help="Don't include pull requests resolved in this many days or less",
    )

    parser.add_argument(
        "--verbose",
        default=False,
        action='store_true',
        help="Display additional information when running",
    )

    parser.add_argument(
        "repo_name", nargs=argparse.REMAINDER, help="GitHub repo name to query"
    )

    args = parser.parse_args()

    main(args)
