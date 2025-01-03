# pytest-dynamic-report-names

A plugin for `pytest` to generate dynamic (timestamped) JUnit report file names. As the names are typically controlled by CLI flags; this is for scenarios where the test commands cannot be modified.

## Installation

```shell
# install the v0.1.0-beta tag from GitHub
pip install https://github.com/dbarbuzzi/pytest-dynamic-report-names/archive/v0.1.0-beta.tar.gz
```

## Usage

To activate the plugin, you must set the `PDRN_JUNIT_BASE` environment variable to the root path where the test result files would be stored.

```shell
# set the env var either before the command or as part of it
# supports the same relative or absolute names that `--junit-xml` would
PDRN_JUNIT_BASE="test-results" pytest
# file would be written to `$(pwd)/test-results/[TIMESTAMP].xml
```

Optionally, you can also set the `` environment variable if you’d like to add a prefix to the filename

```shell
export PDRN_JUNIT_BASE="test-results"
export PDRN_JUNIT_PREFIX="kwyjibo-"
pytest
# file would be written to `$(pwd)/test-results/kwyjibo-[TIMESTAMP].xml
```

> [!NOTE]
> If this plugin is activated, it will replace any existing `--junit-xml` flags
