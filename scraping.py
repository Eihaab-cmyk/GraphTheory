import requests
from bs4 import BeautifulSoup
import re

def scrape_web_pages(urls):
    all_text_data = []
    for url in urls:
        # Send a GET request to the URL
        response = requests.get(url)
        if response.status_code == 200:
            # Parse the HTML content of the page using BeautifulSoup
            soup = BeautifulSoup(response.content, 'html.parser')
            # Extract text data from HTML
            text_data = soup.get_text()
            # Clean the text 
            text_data = re.sub(r'\s+', ' ', text_data)
            # Append the cleaned text data to the list
            all_text_data.append(text_data)
        else:
            print(f"Failed to fetch data from {url}")

    return all_text_data

#URLs to scrape data
urls = [
    # finance train data
         #"https://www.toptal.com/finance/business-consultants/optimizing-profit",
         #"https://www.toptal.com/finance/management-consultants/corporate-strategy",
         #"https://www.toptal.com/finance/growth-strategy/ai-marketing",
         #"https://www.toptal.com/finance/business-process-optimization/business-controls",
         #"https://www.toptal.com/finance/business-development/global-expansion",
         #"https://www.toptal.com/finance/interim-cfos/c-corp-vs-s-corp",
         #"https://www.toptal.com/finance/startup-consultants/startup-financial-model",
         #"https://www.toptal.com/finance/startup-funding-consultants/business-startup-costs",
         #"https://www.toptal.com/finance/excel-experts/google-sheets-advantages",
         #"https://www.toptal.com/finance/interim-cfos/modern-cfo",
         #"https://www.toptal.com/finance/fundraising/financial-modeling-cap-table-modeling",
         #"https://www.toptal.com/finance/business-plan-consultants/sales-and-operations-planning-implementation",
    # finance test data
         #"https://www.toptal.com/finance/data-analysis-consultants/data-analytics-in-banking",
         #"https://www.toptal.com/finance/compliance-consultants/work-from-anywhere-policy",
         #"https://www.toptal.com/finance/venture-capital-consultants/evolution-of-venture-capital",
    # Lifestyle & Hobbies train data
         #"https://medium.com/@rohan.gorlewar/lifestyle-and-hobbies-the-importance-of-finding-balance-5583caf33afa",
         #"https://medium.com/illumination/15-amazing-benefits-of-video-games-b5e8b4b07f8f",
         #"https://medium.com/@aranyasarkarps/the-benefits-of-having-a-good-sleep-and-its-impact-on-work-bde1c062af06",
         #"https://medium.com/@aranyasarkarps/mindfulness-and-motivation-combating-laziness-with-awareness-cbc8622da0f8",
         #"https://medium.com/illumination/ten-habits-that-will-get-you-ahead-of-99-of-people-cd14232a781c",
         #"https://medium.com/@wizdombookinsights/9-minimalist-habits-that-will-save-you-hours-ff3010db542f",
         #"https://medium.com/@wizdombookinsights/6-rules-that-you-should-adopt-in-life-3a3989a78a38",
         #"https://medium.com/@wizdombookinsights/5-things-youre-doing-wrong-in-the-morning-1f8df73eda4f",
         #"https://medium.com/soulsync/how-i-tricked-my-brain-to-like-doing-hard-things-dopamine-detox-d21d5e0e3edc",
         #"https://medium.com/gitconnected/how-to-use-chatgpt-in-daily-life-4688f7afb930",
         #"https://medium.com/@kevinnokiawriting/reading-books-is-useless-heres-a-better-way-to-read-b3a49e157948",
         #"https://medium.com/@kevinnokiawriting/take-a-break-from-worrying-about-what-you-cant-control-d24a2b46381f",
    # Lifestyle & Hobbies test data
          #"https://medium.com/@mandalsaurav3/these-27-sentences-will-make-you-stronger-than-93-of-the-people-197bc1f32acb",
          #"https://medium.com/new-writers-welcome/7-secret-habits-that-will-make-you-an-unstoppable-writer-7fc3256dcdbf",
          #"https://medium.com/@riikkaiivanainen/the-secret-life-of-people-with-high-self-control-its-easier-than-you-think-7dd26fb5282c",
    # Marketing & sales train data
           #"https://medium.com/vizzuell/5-truths-about-marketing-i-wish-every-business-owner-knew-fad646272c70",
           #"https://medium.com/design-bootcamp/if-you-are-a-pm-you-need-to-know-these-frameworks-techniques-for-prioritization-ed3d62fbb5a7",
           #"https://medium.com/@dplayer/top-10-strategies-that-will-transform-marketing-in-2024-0b699ba3e166",
           #"https://medium.com/@rochan-n/understanding-marketing-mix-modeling-with-metas-robyn-7f1792ec9273",
           #"https://medium.com/@ayushtanwal77/15-blogging-mistakes-i-made-before-hitting-50k-daily-visitors-613043209ba9",
           #"https://medium.com/@ugursavci/step-by-step-customer-segmentation-using-k-means-and-pca-in-python-5733822295b6",
           #"https://medium.com/@f20200812/deciphering-marketing-roi-exploring-multi-touch-attribution-models-with-python-and-probabilistic-004164cd0e9f",
           #"https://medium.com/@f20200812/deciphering-marketing-roi-exploring-multi-touch-attribution-models-with-python-and-probabilistic-66c0710ae1c1",
           #"https://medium.com/@kobzevvv/marketing-attribution-data-model-for-b2b-company-0b0ed26e4f77",
           #"https://medium.com/@owox/the-art-of-marketing-analytics-a-deep-dive-a05a49b455d7",
           #"https://hbr.org/1978/07/how-to-pay-your-sales-force",
           #"https://hbr.org/2021/06/what-happens-when-companies-pay-customers-to-write-reviews",
    # Marketing & sales test data
            #"https://medium.com/@dplayer/a-marketers-guide-to-gen-z-generation-z-in-2024-b646cc7af69c",
            #"https://medium.com/@heinrichkoegel/causal-machine-learning-in-marketing-12dcd91ec24e",
            #"https://medium.com/@pedrohportoalegre/the-power-of-distinctive-brand-assets-fda1bc55112b",
           ]

# Scrape text data from web pages
scraped_data = scrape_web_pages(urls)

# Save scraped data to a file
with open("Marketing_test_3_data.txt", "w", encoding="utf-8") as file:
    for data in scraped_data:
        file.write(data + "\n")
