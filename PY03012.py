
if __name__ == '__main__':
    n = int(input())
    arr = []
    for i in range(n):
        name = input()
        correct, submit = map(int, input().split())
        student = {
            'name':name,
            'correct':correct,
            'submit':submit
        }
        arr.append(student)
    arr.sort(key = lambda x: (-x['correct'], x['submit'], x['name']))
    for ele in arr:
        print(f"{ele['name']} {ele['correct']} {ele['submit']}")