def prime_factors_count(n):
    factors = []
    i = 2
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 1
    if n > 1:
        factors.append(n)
    return factors

def main():
    with open("INPUT.TXT", "r") as file:
        m = int(file.readline().strip())
        samples = list(map(int, file.readline().strip().split()))
    
    results = []
    for sample in samples:
        factors = prime_factors_count(sample)
        factors.sort(reverse=False)
        results.append(f"{len(factors)}\n{' '.join(map(str, factors))}")
    with open("OUTPUT.TXT", "w") as file:
        file.write("\n".join(results))

if __name__ == "__main__":
    main()

# Bài 3: 
def read_input(file_name):
    with open(file_name, 'r') as file:
        n = int(file.readline().strip())
        s = file.readline().strip()
        t = file.readline().strip()
    return n, s, t

def write_output(file_name, result):
    with open(file_name, 'w') as file:
        file.write(result)

def can_transform(s, t, n):
    for k in range(n):
        rotated_s = s[k:] + s[:k]
        d = (ord(t[0]) - ord(rotated_s[0])) % 26
        transformed = ''.join(chr((ord(rotated_s[i]) - ord('a') + d) % 26 + ord('a')) for i in range(n))
        if transformed == t:
            return k, d
    return None

def main():
    n, s, t = read_input('INPUT.TXT')
    result = can_transform(s, t, n)
    if result:
        k, d = result
        write_output('OUTPUT.TXT', f"Succes\n{k} {d}")
    else:
        write_output('OUTPUT.TXT', "Impossible")

if __name__ == "__main__":
    main()
    