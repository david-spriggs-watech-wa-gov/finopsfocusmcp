import trafilatura
from trafilatura.spider import focused_crawler
from trafilatura.sitemaps import sitemap_search
from pathlib import Path
import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

logger = logging.getLogger(__name__)

urls = ["https://focus.finops.org/docs/specification/v1-0","https://focus.finops.org/docs/use-cases/v1-0"]
# urls = sitemap_search("https://finops.org/")

# print("\n".join(links))
# urls = ["https://focus.finops.org/docs/use-cases/v1-0"]
crawl_settings = {
    "maxdepth": 2,
    "maxpages": 20,
    "delay": 5,
    "verbose": True
}

for url in urls:
    doc_id = 1
    to_visit, known_urls = focused_crawler(url, max_seen_urls=100, max_known_urls=100000)
    for url in to_visit:
        type = url.split("/")[4]
        full_file_path = f"finops_focus/focus_doc_{type}_{doc_id}.md"
        path = Path(full_file_path)
     
        downloaded = trafilatura.fetch_url(url)
        markdown = trafilatura.extract(downloaded, output_format='markdown', with_metadata=True)
        if markdown:
            path.write_text(markdown, encoding="utf-8")
            logger.info(f"Downloaded document from {url} to {full_file_path}.")
            doc_id = doc_id+1
   

