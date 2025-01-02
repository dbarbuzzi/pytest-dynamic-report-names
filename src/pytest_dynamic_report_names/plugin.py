from datetime import datetime, timezone
import os
from pathlib import Path

import pytest


def pytest_load_initial_conftests(
    early_config: pytest.Config, args: list[str], parser: pytest.Parser
):
    with open("txt-args", "w") as f:
        f.write(str(args))

    if junitxml_base_dir := os.getenv("PDRN_JUNIT_BASE"):
        junitxml_file = (
            Path(junitxml_base_dir) / f"{datetime.now(timezone.utc).timestamp()}.xml"
        )
        if prefix := os.getenv("PDRN_JUNIT_PREFIX"):
            junitxml_file = junitxml_file.with_name(f"{prefix}{junitxml_file.name}")
        args[:] = [*args, f"--junit-xml={junitxml_file.as_posix()}"]

    with open("txt-args-2", "w") as f:
        f.write(str(args))
