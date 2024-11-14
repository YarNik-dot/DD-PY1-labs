# TODO Найдите количество книг, которое можно разместить на дискете
disk_size_mb = 1.44
count_of_pages = 100
lines_per_page = 50
count_of_symbol = 25
bytes_per_symbol = 4
disk_size_bytes = disk_size_mb * 1024 * 1024
count_of_bytes_per_book = bytes_per_symbol * count_of_symbol * lines_per_page * count_of_pages
count_of_book = int(disk_size_bytes // count_of_bytes_per_book)
print("Количество книг, помещающихся на дискету:", count_of_book)
