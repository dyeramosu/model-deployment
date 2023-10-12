"""
Module that contains the command line app.

Typical usage example from command line:
        python cli.py --upload
"""

import os
import argparse

GCP_PROJECT = os.environ["GCP_PROJECT"]
GCS_MODELS_BUCKET_NAME = os.environ["GCS_MODELS_BUCKET_NAME"]


def main(args=None):
    if args.upload:
        print("Upload model to GCS")


if __name__ == "__main__":
    # Generate the inputs arguments parser
    # if you type into the terminal 'python cli.py --help', it will provide the description
    parser = argparse.ArgumentParser(description="Data Collector CLI")

    parser.add_argument(
        "-u",
        "--upload",
        action="store_true",
        help="Upload saved model to GCS Bucket",
    )

    args = parser.parse_args()

    main(args)
