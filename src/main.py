from pprint import pprint
from scrappers.punch_scrapper import punch_scrapper_loop
from scrappers.sun_scrapper import sun_scrapper
from database.connect import create_server_connection
from database.db_utils import execute_query, create_database
from DAO.db_queries import CREATE_TABLE_QUERY, CREATE_DATABASE_QUERY, SAVE_DATA_QUERY, ALTER_TABLE_QUERY
 
 
connection = create_server_connection("localhost", "root", "Mitochondria1998")
 
cursor = connection.cursor()
 
# execute_query(connection, ALTER_TABLE_QUERY)
 
 
def run_scapers():
    This function runs all the scrapers, and saves the data to the database.
    punch_data = punch_scrapper_loop()
    print("running the punch scraper... saving the data to the db")
    for item in punch_data:
        data = (
            item["news_title"],
            item["media_house"],
            item["article_link"],
            item["abstract"],
            item["thumbnail"],
            item["large_image"],
            item["publisher"],
            item["publish_date"],
        )
 
        cursor.execute(SAVE_DATA_QUERY(), data)
        connection.commit()
 
    sun_data = sun_scrapper()
    print("running the sun scraper... saving the data to the db")
    for item in sun_data:
        data = (
            item["news_title"],
            item["media_house"],
            item["article_link"],
            item["abstract"],
            item["thumbnail"],
            item["large_image"],
            item["publisher"],
            item["publish_date"],
        )
 
        cursor.execute(SAVE_DATA_QUERY(), data)
        connection.commit()
 
    print(f"scraper done. No of data points added:  {len(sun_data)}  ")
 
 
run_scapers()
