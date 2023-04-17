# python3

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    # outputs
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # funkcija atrod sakarības tekstā izmantojot Rabin-Karp algoritmu un atdod sarakstu ar pozīcijām kur modelis sākās tekstā
    
    p = 1000000007  # pirmskaitlis (prime number)
    x = 263         # inteģers
    result = []
    p_hash = compute_hash(pattern, p, x)
    hashes = precompute_hashes(text, len(pattern), p, x)
    
    for i in range(len(text) - len(pattern) + 1):
        if p_hash != hashes[i]:
            continue
        if text[i:i+len(pattern)] == pattern:
            result.append(i)
            
    return result

def compute_hash(s, p, x):
    # aprēķina string hash vērtību izmantojot pirmskaitli un inteģeri
    h = 0
    for c in reversed(s):
        h = (h * x + ord(c)) % p
    return h

def precompute_hashes(text, pattern_length, p, x):
    # aprēķina visas hash vērtības
    t = len(text) - pattern_length
    hashes = [0] * (t + 1)
    last_substring = text[-pattern_length:]
    hashes[t] = compute_hash(last_substring, p, x)
    y = 1
    for i in range(pattern_length):
        y = (y * x) % p
    for i in range(t-1, -1, -1):
        current_substring = text[i:i+pattern_length]
        hashes[i] = (x * hashes[i+1] + ord(current_substring[0]) - y * ord(last_substring[-1])) % p
        last_substring = current_substring
    return hashes

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
