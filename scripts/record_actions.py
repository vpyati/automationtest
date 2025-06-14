import subprocess
import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: python scripts/record_actions.py <url>")
        sys.exit(1)
    url = sys.argv[1]
    # Launch Playwright codegen for the provided URL
    subprocess.run(["playwright", "codegen", url], check=True)


if __name__ == "__main__":
    main()
