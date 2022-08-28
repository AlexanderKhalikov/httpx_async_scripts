from httpx import AsyncClient
import pytest_asyncio
import pytest
from six import PY2


@pytest_asyncio.fixture(scope="function")
async def async_client():
    async with AsyncClient() as client:
        yield client


@pytest.fixture
def mocker_open_for_write(mocker):
    # Read a mocked /etc/release file
    mocked_etc_release_data = mocker.mock_open(read_data="some data")
    builtin_open = "__builtin__.open" if PY2 else "builtins.open"
    mocker.patch(builtin_open, mocked_etc_release_data)


