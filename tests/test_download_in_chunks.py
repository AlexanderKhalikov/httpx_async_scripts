import pytest
from scripts.async_scripts import *


@pytest.mark.asyncio
async def test_create_user(async_client):
    response = await async_client.get(URL)
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_something_else(tmp_path):
    await get_archive(url=URL, write_to=str(tmp_path))

    for i in tmp_path.iterdir():
        assert FILE_NAME in str(i)


@pytest.mark.asyncio
async def test_get_archive_open_for_write(mocker_open_for_write):
    assert await get_archive(url=URL, write_to='fakefile') is None


def test_create_dir(tmp_path):
    create_dir(tmp_path)
