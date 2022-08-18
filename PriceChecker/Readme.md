It's a project which do next things Once per day:
1. Take links to the dns-shop site items from local txt file
2. Fetch prices from dns-shop site.
3. Save them to the spreadsheet (instead of SQL database, because it's small application)
4. Check that is a price of items is lower then in the previous day
5. If so - send formatted message to Telegram bot about item which price is lowered Today


Plans:
- Automate that not only dns-shop links to be fetched
- Check price not only lowered but risen too
