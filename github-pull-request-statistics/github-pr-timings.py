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
    durations = []

    merged_summary = {
        "pull_requests": { "amount": 0, "display": "Total Pull Requests" },
        "longest": { "amount": 0, "display": "Longest time before closing" },
        "shortest": { "amount": 100000, "display": "Shortest time before closing" },
        "75_percentile": { "amount": None, "display": "75 Percentile of days before closing" },
        "95_percentile": { "amount": None, "display": "95 Percentile of days before closing" },
        "median": { "amount": None, "display": "Median days before closing" },
    }

    for pull_request in pull_requests:
        pr = pull_requests[pull_request]

        merged_summary["pull_requests"]["amount"] += 1

        if pr["duration"] > merged_summary["longest"]["amount"]:
            merged_summary["longest"]["amount"] = pr["duration"]

        if pr["duration"] < merged_summary["shortest"]["amount"]:
            merged_summary["shortest"]["amount"] = pr["duration"]

        durations.append(pr["duration"])

    merged_summary["75_percentile"]["amount"] = "{:.2f}".format(numpy.percentile(durations, 75))
    merged_summary["95_percentile"]["amount"] = "{:.2f}".format(numpy.percentile(durations, 95))

    merged_summary["median"]["amount"] = statistics.median(durations)

    return(merged_summary)


def summarise(resolution_type, repo, prs):
    """Display the summarised stats for the given PR type."""

    if len(prs) < 1:
        return ""

    output = []
    output.append("") # open with a blank line for readability

    summary = generate_statistics(prs)

    output.append(f"{resolution_type} summary for {repo}")
    output.append("==========")

    for metric in summary:
        amount = summary[metric]["amount"]
        description = summary[metric]["display"]

        output.append(f"{description} == {amount}")

    return "\n".join(output)


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

    if args.verbose:
        print(f" == Working set of {len(pull_requests)} PRs")

    # ignore any PRs resolved in under X days
    interesting_prs = {
        key: value
        for (key, value) in pull_requests.items()
        if pull_requests[key]["duration"] > args.minimum_days
    }

    if args.verbose:
        print(f" == {len(interesting_prs)} PRs resolved after {args.minimum_days} days")

    merged_prs = {
        key: value
        for (key, value) in interesting_prs.items()
        if pull_requests[key]["ending"] == "merged"
    }

    closed_prs = {
        key: value
        for (key, value) in interesting_prs.items()
        if pull_requests[key]["ending"] == "closed"
    }

    closed = summarise("Closed", args.repo_name, closed_prs)
    merged = summarise("Merged", args.repo_name, merged_prs)

    if closed:
        print(closed)

    if merged:
        print(merged)

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
