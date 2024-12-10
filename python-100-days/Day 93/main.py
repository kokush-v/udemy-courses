import asyncio
from pyppeteer import launch
import pandas as pd
from re import sub
import os


def to_snake(s: str):
    return '_'.join(
        sub('([A-Z][a-z]+)', r' \1',
            sub('([A-Z]+)', r' \1',
                s.replace('-', ' '))).split()).lower()


async def main():

    async def create_data_frame_from_data(table) -> pd.DataFrame:
        if table:
            heroes = await table[0].xpath('./*')
            df = pd.DataFrame(columns=["HERO", "WINRATE"])
            if heroes:
                for i, hero in enumerate(heroes):
                    hero_name = await page.evaluate('(hero) => hero.querySelector("span").textContent', hero)
                    hero_winrate = await page.evaluate('(hero) => hero.querySelector(".ch2").textContent.trim()', hero)
                    df.loc[i] = {"HERO": hero_name, "WINRATE": hero_winrate}

                    print(f"{i+1}. {hero_name} has {hero_winrate} right now")

        return df.sort_values(by='WINRATE', ascending=False)

    browser = await launch(
        headless=False,
        executablePath="/usr/bin/chromium"
    )
    page = await browser.newPage()
    await page.setViewport({'width': 1920, 'height': 1080})
    await page.goto("https://dota2protracker.com/")

    table_tabs = await page.xpath('//*[@id="top-heroes"]/div/div[2]/*')
    os.mkdir('winrate_stats')
    for tab in table_tabs:
        tab.click()

        hero_table = await page.xpath('//*[@id="top-heroes"]/div/div[5]')
        tab_title = await page.evaluate('(tab) => tab.textContent.trim()', tab)

        hero_df = await create_data_frame_from_data(hero_table)

        hero_df.to_csv(
            f'winrate_stats/{to_snake(tab_title)}.csv', index=False)

    print("Browser will remain open. Press Ctrl+C to stop the script.")
    while True:
        await asyncio.sleep(1)  # Keep the event loop alive


asyncio.get_event_loop().run_until_complete(main())
