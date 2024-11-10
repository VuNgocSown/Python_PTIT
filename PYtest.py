def nhap():
    a, b = map(int, input("Nhập số đỉnh và số cạnh (a b): ").split())
    adj = [set() for _ in range(a + 1)]  # Tạo danh sách các tập hợp, mỗi đỉnh có một tập chứa các đỉnh kề
    bac = [0] * (a + 1)  # Tạo danh sách lưu bậc của các đỉnh, ban đầu tất cả bậc đều bằng 0
    
    print("Nhập các cạnh (x y):")
    for _ in range(b):
        x, y = map(int, input().split())  # Nhập từng cạnh (x, y)
        adj[x].add(y)  # Thêm y vào danh sách đỉnh kề của x
        adj[y].add(x)  # Thêm x vào danh sách đỉnh kề của y (vì đồ thị vô hướng)
        bac[x] += 1  # Tăng bậc của đỉnh x
        bac[y] += 1  # Tăng bậc của đỉnh y
    
    return a, adj, bac  # Trả về số đỉnh, danh sách đỉnh kề và danh sách bậc của đỉnh
def euler(v, adj):
    nx = [v]  # Khởi tạo ngăn xếp với đỉnh bắt đầu v
    rs = []  # Danh sách chứa kết quả, đường đi Euler
    
    while nx:
        x = nx[-1]  # Lấy đỉnh trên cùng của ngăn xếp (đỉnh hiện tại)
        if adj[x]:  # Nếu đỉnh hiện tại còn đỉnh kề (còn cạnh chưa đi qua)
            y = adj[x].pop()  # Lấy đỉnh kề bất kỳ (và xóa cạnh giữa x và y)
            adj[y].remove(x)  # Xóa cạnh giữa y và x (vì đồ thị vô hướng)
            nx.append(y)  # Thêm y vào ngăn xếp để tiếp tục duyệt từ y
        else:
            rs.append(x)  # Nếu không còn cạnh nào từ x, thêm x vào kết quả
            nx.pop()  # Xóa x khỏi ngăn xếp
    
    return rs  # Trả về kết quả là đường đi Euler (danh sách các đỉnh)def main():
    a, adj, bac = nhap()  # Gọi hàm nhập để nhận dữ liệu đồ thị
    
    start = 1  # Điểm bắt đầu mặc định là đỉnh 1
    odd_vertices = [i for i in range(1, a + 1) if bac[i] % 2 != 0]  # Tìm các đỉnh có bậc lẻ
    
    # Kiểm tra số đỉnh bậc lẻ
    if len(odd_vertices) == 0:
        # Nếu không có đỉnh bậc lẻ, bắt đầu từ đỉnh 1
        start = 1
    elif len(odd_vertices) == 2:
        # Nếu có hai đỉnh bậc lẻ, bắt đầu từ một trong hai đỉnh đó
        start = odd_vertices[0]
    else:
        print("Đồ thị không có đường đi Euler.")
        return
    
    result = euler(start, adj)  # Gọi hàm euler để tìm đường đi Euler
    print("Đường đi Euler:", " ".join(map(str, result[::-1])))  # In kết quả theo thứ tự ngược