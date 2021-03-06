
import sys
import os
import argparse

import github  # PyGithub

# Set the argument parser
parser = argparse.ArgumentParser('Release Download')

# Add arguments
parser.add_argument(
    "--repo",
    type     = str,
    required = True,
    help     = "Github Repo"
)

parser.add_argument(
    "--tag",
    type     = str,
    required = True,
    help     = "Tag to release"
)

parser.add_argument(
    "--file",
    type     = str,
    required = True,
    help     = "File to upload"
)

# Get the arguments
args = parser.parse_args()

print("\nLogging into github....\n")

token = os.environ.get('GH_REPO_TOKEN')

if token is None:
    sys.exit("Failed to get github token from GH_REPO_TOKEN environment variable")

gh = github.Github(token)
remRepo = gh.get_repo(args.repo)

try:

    release = remRepo.get_release(args.tag)
    release.upload_asset(args.file)

except Exception as e:
    sys.exit(f"Failed to find and upload tag {args.tag}: {e}")

