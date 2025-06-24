from collections.abc import Callable
from pathlib import Path

import pytest


@pytest.fixture
def fixture_loader() -> Callable[[str], str]:
    def _load(name: str) -> str:
        path = Path(__file__).parent / "__fixtures__" / name
        return path.read_text()

    return _load


@pytest.fixture
def json_content(fixture_loader: Callable[[str], str]) -> str:
    return fixture_loader("test.json")
