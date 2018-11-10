import re
import csv
import json

def validate_hotel_name(hotel_name):
    all_ascii = all( ord(c) < 128 for c in hotel_name )
    return all_ascii

def validate_hotel_url(url):
    matchObj = re.match(r'^(http:\/\/|https:\/\/)\S+', url, re.M )
    if matchObj:
        return True
    else:
       return False

def validate_stars(stars):
    try:
        stars = int(stars)
    except:
        return False
    if stars > 5 or stars < 0:
        return False
    else:
        return True

def transform_phone_no(ph_no):
    reg4country_code = r'(^\+\d{0,3})|(^\(\d{0,3}\s?\)|(^\d{0,3}\s?-)|(^\d{0,3}\s?\.))'
    ph_no = re.sub(reg4country_code, "", ph_no)
    ph_no = ph_no.strip()
    return ph_no

def transform_names(name):
    reg4salutation = r'(^Dr\.?\s*)|(^Mrs?\.?\s*)|(^Miss\.*\s*)|(^Ms\.*\s*)'
    name = re.sub(reg4salutation, "", name)
    return name

def get_sql_insert_query(json_object):
    query = "INSERT INTO table_details (`name`, address, stars, contact, phone, uri) VALUES ( '{name}', '{address}', {stars}, '{contact}', '{phone}', '{uri}' ) "
    query=query.format(**json_object)
    return query

CREATE_TABLE_CMD = '''
CREATE TABLE table_details(
  id PRIMARY_KEY AUTO_INCREMENT,
  name VARCHAR(100),
  address VARCHAR(1024), 
  stars INTEGER, 
  contact VARCHAR(100), 
  phone VARCHAR(30), 
  uri VARCHAR(512)
)
'''

def read_csv_file( source_csv_file, dest_json_file, dest_sql_file ):
    list_of_hotel_details = []
    sql_f = open(dest_sql_file, "w")
    sql_f.write(CREATE_TABLE_CMD)
    sql_f.write("\n")

    with open(source_csv_file) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            name = row['name']
            address = row['address']
            stars = row['stars']
            contact_person = row['contact']
            phone   = row['phone']
            uri     = row['uri']

            if validate_hotel_name(name) and validate_hotel_url(uri) and validate_stars(stars):
                phone_no = transform_phone_no(phone)
                contact_person = transform_names(contact_person)
                hotel_detail = {
                    "name"              : name,
                    "address"           : address,
                    "stars"             : stars,
                    "contact"           : contact_person,
                    "phone"             : phone_no,
                    "uri"               : uri
                }
                list_of_hotel_details.append(hotel_detail)
                sql_query = get_sql_insert_query(hotel_detail)
                sql_f.write(sql_query)
                sql_f.write("\n")
            else:
                print("Skipping "+row['name']+" because of invalid values.")
                continue
    result_str = json.dumps(list_of_hotel_details, indent=2)
    f = open(dest_json_file, "w")
    f.write(result_str)
    f.close()
    sql_f.close()
    print("Success!! Source CSV File : "+source_csv_file+" processed and data written to files: "+dest_json_file+" and "+dest_sql_file)

if __name__ == "__main__":
    read_csv_file(r"input_dir\hotels.csv", "output_dir/hotels.json", "output_dir/hotels.sql")