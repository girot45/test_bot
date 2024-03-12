def proccess_info_from_db(data):
    res_str = ""
    for item in data:
        res_str += f"{item[0].user_id} - {item[0].timestamp} - {item[0].product_code}\n"
    return res_str
