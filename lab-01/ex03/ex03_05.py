def dem_so_lan_xuat_hien(lst):
    count_dict = {}
    for item in lst:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    return count_dict
# Nhập danh sách từ người dùng và xử lý chuỗi
input_string = input("Nhập danh sách các số nguyên (phân tách bởi dấu phẩy): ")
word_list = input_string.split(',')
# Sử dụng hàm và in kết quả
so_lan_xuat_hien = dem_so_lan_xuat_hien(word_list)
print("Số lần xuất hiện của mỗi phần tử trong danh sách: ", so_lan_xuat_hien)