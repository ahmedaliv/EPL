from datetime import datetime

def check_date(date_1,date_2):
    format_string = "%d/%m/%Y"
    try:
        date1 = datetime.strptime(date_1,format_string)
        date2 = datetime.strptime(date_1,format_string)
        return True
    except ValueError:
        return False
    
def convert_date(date_string):
    format_string = "%d/%m/%Y"
    datetime_obj = datetime.strptime(date_string,format_string).date()
    return datetime_obj

