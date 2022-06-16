from src.connection.connection import Connection
import logging

class importData(Connection):
    
    """Imports the data from the passed csv file from results/csv into the target database
    """
    
    def __init__(self, filename):
        self.csv_file = f"results/csv/{filename}"
    
    def verify(self):
        with open(self.csv_file, 'r') as f:
            for row in f:
                print(row)
    
    def upload(self, loadIntoTableName = None):
        with open(f'{self.csv_file}', 'r') as f:
            self.cur.copy_from(f, loadIntoTableName, sep = ',')
            self.conn.commit()
            self.conn.close()
        logging.getLogger("importData.upload() call").addHandler(self.handler)
        f.close()