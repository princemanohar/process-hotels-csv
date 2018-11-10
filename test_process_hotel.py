import process_hotel_csv

def test_validate_hotel_name():

    valid_name1 = "Hotel Park Inn"
    print("Testing validate_hotel_name() with : "+valid_name1)
    result = process_hotel_csv.validate_hotel_name(valid_name1)
    assert result == True

    invalid_name1 = "Döring Comfort Inn"
    print("Testing validate_hotel_name() with : " + invalid_name1)
    result = process_hotel_csv.validate_hotel_name(invalid_name1)
    assert result == False

def test_validate_hotel_url():

    valid_url = "http://mynormalhotel.com/parkview"
    print("Testing validate_hotel_url() with : " + valid_url)
    result = process_hotel_csv.validate_hotel_url(valid_url)
    assert result == True

    valid_url = "https://mynormalhotel.com/parkview"
    print("Testing validate_hotel_url() with : " + valid_url)
    result = process_hotel_csv.validate_hotel_url(valid_url)
    assert result == True

    invalid_url = "ftp://mynormalhotel.com/parkview"
    print("Testing validate_hotel_url() with : " + invalid_url)
    result = process_hotel_csv.validate_hotel_url(invalid_url)
    assert result == False

    in_valid_url = "mynormalhotel/parkview"
    print("Testing validate_hotel_url() with : " + invalid_url)
    result = process_hotel_csv.validate_hotel_url(in_valid_url)
    assert result == False

def test_validate_stars():

    valid_stars = 5
    print("Testing validate_stars() with : " , valid_stars)
    result = process_hotel_csv.validate_stars(valid_stars)
    assert result == True

    valid_stars = 0
    print("Testing validate_stars() with : " , valid_stars)
    result = process_hotel_csv.validate_stars(valid_stars)
    assert result == True

    valid_stars = 3
    print("Testing validate_stars() with : " , valid_stars)
    result = process_hotel_csv.validate_stars(valid_stars)
    assert result == True

    valid_stars = "3"
    print("Testing validate_stars() with : " , valid_stars)
    result = process_hotel_csv.validate_stars(valid_stars)
    assert result == True

    valid_stars = 7
    print("Testing validate_stars() with : " , valid_stars)
    result = process_hotel_csv.validate_stars(valid_stars)
    assert result == False

    valid_stars = -1
    print("Testing validate_stars() with : " ,valid_stars)
    result = process_hotel_csv.validate_stars(valid_stars)
    assert result == False

    valid_stars = "a"
    print("Testing validate_stars() with : " , valid_stars)
    result = process_hotel_csv.validate_stars(valid_stars)
    assert result == False

def test_transform_phone_no():
    phone_no = "+91 7797045315"
    print("Testing transform_phone_no() with : " , phone_no)
    result = process_hotel_csv.transform_phone_no(phone_no)
    assert result == "7797045315"

    phone_no = "+412 7797045315"
    print("Testing transform_phone_no() with : ", phone_no)
    result = process_hotel_csv.transform_phone_no(phone_no)
    assert result == "7797045315"

    phone_no = "(412) 7797 045315"
    print("Testing transform_phone_no() with : ", phone_no)
    result = process_hotel_csv.transform_phone_no(phone_no)
    assert result == "7797 045315"

    phone_no = "412.7797.045315"
    print("Testing transform_phone_no() with : ", phone_no)
    result = process_hotel_csv.transform_phone_no(phone_no)
    assert result == "7797.045315"

    phone_no = "478 - 855 - 0765"
    print("Testing transform_phone_no() with : ", phone_no)
    result = process_hotel_csv.transform_phone_no(phone_no)
    assert result == "855 - 0765"


def test_transform_names():
    name = "Mr.Prince"
    print("Testing transform_names() with : ", name)
    result = process_hotel_csv.transform_names(name)
    assert result == "Prince"

    name = "Mr. Raman"
    print("Testing transform_names() with : ", name)
    result = process_hotel_csv.transform_names(name)
    assert result == "Raman"

    name = "Dr. Sobhit Dey"
    print("Testing transform_names() with : ", name)
    result = process_hotel_csv.transform_names(name)
    assert result == "Sobhit Dey"

    name = "Mrs. Rumani singh"
    print("Testing transform_names() with : ", name)
    result = process_hotel_csv.transform_names(name)
    assert result == "Rumani singh"

    name = "Mrs. Lorelai Pagac"
    print("Testing transform_names() with : ", name)
    result = process_hotel_csv.transform_names(name)
    assert result == "Lorelai Pagac"

    name = "Miss Maribeth Stanton DDS"
    print("Testing transform_names() with : ", name)
    result = process_hotel_csv.transform_names(name)
    assert result == "Maribeth Stanton DDS"

if __name__ == "__main__":
    test_validate_hotel_name()
    test_validate_hotel_url()
    test_validate_stars()
    test_transform_phone_no()
    test_transform_names()
    print("All tests run successfully.")