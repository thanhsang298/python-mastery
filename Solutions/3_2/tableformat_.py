
def print_table(records, fields):
    header_line = "".join('%15s' %field for field in fields)
    print(header_line)
    print(('-'*15 + ' ')*len(fields))
    for record in records:
        print("".join('%15s' % getattr(record, field) for field in fields))