from lec02.job1.dal import local_disk, sales_api

def save_sales_to_local_disk(date: str, raw_dir: str) -> None:
    # TODO: implement me
    # 1. get data from the API
    # 2. save data to disk
    print("\tI'm in get_sales(...) function!")

    sales = sales_api.get_sales(date)
    local_disk.save_to_disk(sales, f'{raw_dir}/sales_{date}.json')


