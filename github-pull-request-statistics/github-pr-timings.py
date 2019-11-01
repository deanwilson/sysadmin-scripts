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
        key: value
        for (key, value) in pull_requests.items()
        if pull_requests[key]["ending"] == "merged"
    }
    merged_prs = {
        key: value
        for (key, value) in pull_requests.items()
        if pull_requests[key]["duration"] > args.minimum_days
    }

    if len(merged_prs) > 0:
        print("Merged Pull requests")

    merged_summary = {
        "pull_requests": 0,
        "longest": 0,
        "shortest": 100000,
        "durations": [],
    }

    for pull_request in merged_prs:
        pr = merged_prs[pull_request]
        # print(f"""PR#{pr["number"]} Days={pr["duration"]} Title={pr["title"]}""")

        merged_summary["pull_requests"] += 1

        if pr["duration"] > merged_summary["longest"]:
            merged_summary["longest"] = pr["duration"]

        if pr["duration"] < merged_summary["shortest"]:
            merged_summary["shortest"] = pr["duration"]

        merged_summary["durations"].append(pr["duration"])

    if len(merged_prs) > 0:
        print(f"Summary for {args.repo_name}\n==========")
        for metric in ["pull_requests", "longest", "shortest"]:
            print(f"{metric} == {merged_summary[metric]}")

        print(
            f"""Median duration == {statistics.median(merged_summary["durations"])}"""
        )
        print(
            f"""75 percentile == {numpy.percentile(merged_summary["durations"], 75)}"""
        )
        print(
            f"""95 percentile == {numpy.percentile(merged_summary["durations"], 95)}"""
        )


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
        "repo_name", nargs=argparse.REMAINDER, help="GitHub repo name to query"
    )

    args = parser.parse_args()

    # print(start_date)
    # print(args.repo_name)
    # sys.exit(1)

    main(args)
