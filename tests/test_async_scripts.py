from pathlib import Path
import pytest
from pytest_httpx import HTTPXMock
from scripts.async_scripts import *


@pytest.mark.asyncio
async def test_status_code(async_client):
    response = await async_client.get(URL)
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_download_archive(tmp_path):
    await get_archive(url=URL, write_to=str(tmp_path))

    for i in tmp_path.iterdir():
        assert FILE_NAME in str(i)


@pytest.mark.asyncio
async def test_get_archive_open_for_write(mocker_open_for_write):
    assert await get_archive(url=URL, write_to='fakefile') is None


def test_create_dir(tmp_path):
    create_dir(tmp_path)


@pytest.mark.asyncio
async def test_post_archive(httpx_mock: HTTPXMock, tmp_path):
    httpx_mock.add_response(method="POST")
    CONTENT = b'Hello, world'

    tmp_dir = tmp_path / "sub"
    tmp_dir.mkdir()
    tmp_file = tmp_dir / Path('my_binary_file')
    tmp_file.write_bytes(CONTENT)

    await post_archive(url="https://test_url", path_to_archive=str(tmp_file))
