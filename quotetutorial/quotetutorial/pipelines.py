# everytime the for loop in quotes_spider.py runs, items go to the pipelines.py 
from itemadapter import ItemAdapter
import sqlite3

class QuotetutorialPipeline:

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = sqlite3.connect("myquotes.db")
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS quotes_tb""") # drop table if the table already exists
        self.curr.execute("""create table quotes_tb(
                            quote text, 
                            author text,
                            tag text        
                        )""")

    def process_item(self, item, spider):
        self.store_db(item)
        return item
    
    def store_db(self, item):
        self.curr.execute("""insert into quotes_tb values (?,?,?)""", (
            item['quote'][0],
            item['author'][0],
            item['tags'][0]
        ))

        self.conn.commit()
