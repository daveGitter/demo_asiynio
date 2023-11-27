import asyncio
import datetime
import time

from colorama import init
from colorama import Fore, Back, Style


async def async_job(color: str = Fore.WHITE):
    print(color + 'Pretending to wait async...')
    await asyncio.sleep(3)


def sync_job():
    print(Back.CYAN + Fore.WHITE + 'Pretending to wait...')
    time.sleep(3)


async def main():
    # sync job
    print(Back.GREEN + Fore.WHITE + 'Starting sync job.', flush=True)

    t0 = datetime.datetime.now()

    sync_job()
    sync_job()

    t1 = datetime.datetime.now()

    print(
        Back.GREEN + Fore.WHITE
        + f'Ending sync job. Total time: {(t1 - t0).total_seconds():.2f} sec.',
        flush=True
    )

    # async job
    print(Back.MAGENTA + Fore.WHITE + 'Starting awaiting async job.', flush=True)

    t0 = datetime.datetime.now()

    await async_job(Back.LIGHTYELLOW_EX + Fore.WHITE)
    await async_job(Back.LIGHTRED_EX + Fore.WHITE)

    t1 = datetime.datetime.now()

    print(
        Back.MAGENTA + Fore.WHITE
        + f'Ending awaiting async job. Total time: {(t1 - t0).total_seconds():.2f} sec.',
        flush=True
    )

    # async job
    print(Back.LIGHTBLUE_EX + Fore.WHITE + 'Starting async job.', flush=True)

    t0 = datetime.datetime.now()

    tasks = [
        async_job(Back.LIGHTYELLOW_EX + Fore.WHITE),
        async_job(Back.LIGHTRED_EX + Fore.WHITE)
    ]
    await asyncio.gather(*tasks)

    t1 = datetime.datetime.now()

    print(
        Back.LIGHTBLUE_EX + Fore.WHITE
        + f'Ending async job. Total time: {(t1 - t0).total_seconds():.2f} sec.',
        flush=True
    )

    print(Style.RESET_ALL)


if __name__ == '__main__':
    init()
    asyncio.run(main())
