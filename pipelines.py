# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import mysql.connector

class ScrapeamanzonPipeline:
    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = mysql.connector.connect(
           host ='localhost',
            user ='root',
            passwd = 'root',
            database = 'amazon_data'
        )
        self.curr=self.conn.cursor()

    def create_table(self):
        self.curr.execute("""drop table if exists amazon_db""")
        self.curr.execute("""create table amazon_db(product_name varchar(500),product_author varchar(200),product_price varchar(100),product_imagelink varchar(1000))""")

    def process_item(self, item, spider):
        self.curr.execute("""insert into amazon_db values(%s,%s,%s,%s)""",(item['product_name'][0],item['product_author'][0],item['product_price'][0],item['product_imagelink'][0]))
        self.conn.commit()
        
        return item
