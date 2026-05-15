def dao_nguoc_list(lst):
    return lst[::-1]
# Nhập danh sách từ người dùng và xử lý chuỗi
input_list = input("Nhập danh sách các số nguyên (phân tách bởi dấu phẩy): ")
numbers = list(map(int, input_list.split(',')))
# Sử dụng ham và in kết quả
list_dao_nguoc = dao_nguoc_list(numbers)
print("Danh sách sau khi đảo ngược là: ", list_dao_nguoc)