import sys 
from pathlib import Path 

class redirect_stdout:
    def __init__(self, out_file):
        self.out_file = out_file 

    # print statement will save in the sys.stdout
    # store sys.stdout to a new temp variable self.stdout 
    # change the place to store from sys.stdout to out_file
    # when exit, redirect sys.stdout back to the variable self.stdout
    def __enter__(self):
        self.stdout = sys.stdout 
        sys.stdout = self.out_file 
        return self.out_file 
    
    def __exit__(self, ty, val, tb):
        sys.stdout = self.stdout

if __name__ == "__main__":
    from tableformat import create_formatter
    import tableformat
    import stock, reader
    portfolio = reader.read_csv_as_instances('Data/portfolio.csv', stock.Stock)
    formatter = create_formatter('text')

    with redirect_stdout(open(Path.cwd() / 'out.txt', 'w')) as file:
        tableformat.print_table(portfolio, ['name','shares','price'], formatter)
        file.close()