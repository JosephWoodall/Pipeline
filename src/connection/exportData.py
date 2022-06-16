import logging
import datetime
from src.connection.connection import Connection

class exportData(Connection):
    
    """Exports data out of the source database using the Connection class
    
    Returns: 
        showReults: shows the result of the passed query in the console
        saveFile: saves the result of the passed query into a csv file that is stored in results/csv
    """
    def __init__(self, sql_query):
        logging.getLogger('Export Class Initialization').addHandler(self.handler)
        self.sql_query = sql_query
        
    def query(self, showReults = bool, saveFile = bool):
        query_execution_date = datetime.now()
        query_execute = self.cur.execute(self.sql_query)
        if showReults == True: 
            for row in query_execute.fetchall():
                print(row)
        if saveFile == True:
            if query_execute:
                output_query = 'copy ({0}) to stdout with csv header'.format(self.sql_query)
                with open(f'results/csv/{query_execution_date}_query_output.csv', 'w') as f:
                    query_execute.copy_expert(output_query, f)
                self.conn.close()
            else:
                print("Resulting query is blank. Please check query in Export().__init__ and try again")
                self.conn.close()
        logging.getLogger("exportData.query() call").addHandler(self.handler)
        self.conn.close()