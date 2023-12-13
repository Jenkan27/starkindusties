from datetime import date

def convert_american_to_date(american_date: str) -> date:
    month = american_date.split('/')[0]
    day = american_date.split('/')[1]
    year = american_date.split('/')[2]
    
    iso_date = year
    if len(month) < 2:
        month = '0' + month
    iso_date += month
    if len(day) < 2:
        day ='0' + day
    iso_date += day
    
    converted_date  = date.fromisoformat(iso_date)
    return converted_date

if __name__ == '__main__':
    print(convert_american_to_date("2/8/1993"))
    print(convert_american_to_date("3/12/2002"))
    print(convert_american_to_date("12/13/2023"))
