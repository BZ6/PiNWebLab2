from bs4 import BeautifulSoup

from connection_async import SessionLocal_async
from models import WebPage


async def parse_and_save_async(url, session):
    try:
        async with session.get(url) as response:
            text = await response.text()
            soup = BeautifulSoup(text, 'html.parser')
            title = soup.title.string if soup.title else 'No title'

            async with SessionLocal_async() as db_session:
                page = WebPage(url=url, title=title)
                db_session.add(page)
                await db_session.commit()
        print(f"Parsed: {url}: {title}")
    except Exception as e:
        print(f"Error parsing {url}: {e}")
