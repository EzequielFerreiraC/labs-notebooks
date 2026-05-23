"""Simple CLI entrypoint."""
import argparse


def main() -> None:
    parser = argparse.ArgumentParser(prog="labs")
    parser.add_argument("command", choices=["hello", "version"])
    args = parser.parse_args()
    if args.command == "hello":
        print("hello from labs-notebooks")
    else:
        print("0.1.0")


if __name__ == "__main__":
    main()
