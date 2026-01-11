# nuitka-project: --mode=onefile
# nuitka-project: --output-dir=build

import sys

from src import app


if __name__ == "__main__":
    app.cli()
