# Practice for tableformat

def print_table(records, fields, formatter):
    formatter.headings(fields)
    for r in records:
        rowdata = [getattr(r, fieldname) for fieldname in fields]
        formatter.row(rowdata)

class TableFormatter:
    def headings(self, headers):
        raise NotImplementedError()

    def row(self, rowdata):
        raise NotImplementedError()
    
class TextTableFormatter(TableFormatter):
    def headings(self, headers):
        print(' '.join('%10s' % h for h in headers))
        print(('-'*10 + ' ')*len(headers))
    
    def row(self, rowdata):
        print(' '.join('%10s' % d for d in rowdata))

class CSVTableFormatter(TableFormatter):
    def headings(self, headers): 
        print(",".join(headers)) 

    def row(self, rowdata):
        print(','.join('%s' % d for d in rowdata)) 

class HTMLTableFormatter(TableFormatter):
    def headings(self, headers): 
        print("<tr>", end=" ")
        for header in headers: 
            print("<th>%s</th>" %header, end=" ")
        print("/tr")

    def row(self, rowdata):
        print('<tr>', end=' ')
        for d in rowdata:
            print('<td>%s</td>' % d, end=' ')
        print('</tr>')

def create_formatter(format): 
    if format == "text": 
        formatter = TextTableFormatter
    elif format == "csv": 
        formatter = CSVTableFormatter
    elif format == "html": 
        formatter = HTMLTableFormatter
    else: 
        raise RuntimeError("Unknown format %s" % format)
    return formatter()