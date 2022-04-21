"""Module containing a very basic CLI example."""
import os
import logging
import argparse
from importlib import resources

from demo_project import package_data


def parse_arguments():
    """Parses command line arguments."""
    parser = argparse.ArgumentParser("CLI example")
    subparsers = parser.add_subparsers(
        dest="command", help="Provide a command: initialize or check."
    )

    # Add command subparsers
    init_parser = subparsers.add_parser("initialize", help="Initialize a new project.")
    init_parser.add_argument(
        "-d",
        "--dir",
        type=str,
        default=".",
        help="Directory to create the project in (default: current directory).",
    )
    init_parser.add_argument(
        "-l",
        "--loglevel",
        type=str,
        choices=["critical", "error", "warning", "info", "debug"],
        default="info",
        help="Logging level fpr the command line interface.",
    )

    check_parser = subparsers.add_parser("check", help="Run DQ checks.")
    check_parser.add_argument(
        "-d",
        "--dir",
        type=str,
        default=".",
        help="Project directory to run checks on (default: current directory).",
    )
    check_parser.add_argument(
        "-l",
        "--loglevel",
        type=str,
        choices=["critical", "error", "warning", "info", "debug"],
        default="info",
        help="Logging level fpr the command line interface.",
    )

    return parser.parse_args()


def run_checks(data_folder: str, checks_path: str, schema_path: str) -> None:
    """Run DQ checks on a set of data files."""
    logger = logging.getLogger(__name__)
    logger.info("Running DQ checks...")
    logger.debug(f"- Data folder: {data_folder!r}")
    logger.debug(f"- Checks file: {checks_path!r}")
    logger.debug(f"- Schema file: {schema_path!r}")

    # TODO: Check paths / files exist
    # TODO: Implement checks logic


def main():
    """Command line routine"""
    args = parse_arguments()


    if args.command == "initialize":
        # Set up root logger
        logging.basicConfig(level=args.loglevel.upper())
        logger = logging.getLogger(__name__)

        # Create the project structure
        logger.info("Creating project folder structure...")
        for subdir in "data", "input", "config":
            logger.debug(f"- Creating subfolder: {subdir}")
            os.makedirs(os.path.join(args.dir, subdir))

        # Copy in checks JSON schema
        schema = resources.read_text(package_data, "checks_schema.json")
        schema_path = os.path.join(args.dir, "config", "checks_schema.json")
        with open(schema_path, "w", encoding="utf=8") as schema_file:
            schema_file.write(schema)

        # Copy in checks skeleton
        checks = resources.read_text(package_data, "variables_to_check.json")
        checks_path = os.path.join(args.dir, "input", "variables_to_check.json")
        with open(checks_path, "w", encoding="utf=8") as checks_file:
            checks_file.write(checks)

    elif args.command == "check":
        # Set up root logger
        logging.basicConfig(level=args.loglevel.upper())

        # Run checks
        data_folder = os.path.join(args.dir, "data")
        checks_path = os.path.join(args.dir, "input", "variables_to_check.json")
        schema_path = os.path.join(args.dir, "config", "checks_schema.json")

        run_checks(data_folder, checks_path, schema_path)

    else:
        print(
            f"Unknown command '{args.command}'; choose from 'check' or 'initialize'."
        )


if __name__ == "__main__":
    main()
