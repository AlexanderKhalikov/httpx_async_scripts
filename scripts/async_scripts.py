import httpx
import asyncio
import yaml
import os


with open(os.path.realpath('../credentials/configTest.yaml')) as conf_file:
    config = yaml.load(conf_file, Loader=yaml.FullLoader)

URL = config['jar_url']
FOLDER_PATH = config['folder_path']
FILE_NAME = config['file_name']


def create_dir(path_to_folder: str = FOLDER_PATH):
    try:
        os.mkdir(path_to_folder)
        # print(f"Directory {path_to_folder} created")
    except FileExistsError:
        print(f'{path_to_folder} exists')


async def get_archive(url: str, write_to: str = FOLDER_PATH) -> None:
    # Downloading archive file in byte chunks
    with open(write_to + FILE_NAME, 'wb') as f:
        async with httpx.AsyncClient() as client:
            async with client.stream('GET', url) as r:
                async for chunk in r.aiter_bytes():
                    f.write(chunk)


async def post_archive(url: str, path_to_archive: str) -> None:
    # Upload archive to server
    headers = {'Content-Type': 'application/octet-stream'}
    async with httpx.AsyncClient() as client:
        await client.post(url, content=b'Hello, world', headers=headers)


async def main():
    # Create directory to download
    create_dir()    # pragma: no cover
    await get_archive(URL)  # pragma: no cover


if __name__ == '__main__':
    asyncio.run(main())     # pragma: no cover
