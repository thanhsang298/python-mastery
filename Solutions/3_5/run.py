import stock
import reader  
from tableformat_ import create_formatter, print_table
from pathlib import Path 

porfolio = reader.read_csv_as_instances(Path("Data/portfolio.csv").resolve(), stock.Stock)
# formatter = tableformat_.TextTableFormatter()
# formatter = tableformat_.CSVTableFormatter()
# formatter = tableformat_.HTMLTableFormatter()
formatter = create_formatter('html')
print_table(porfolio, ['name', 'shares', 'price'], formatter)