import timeit

# KMP


def compute_lps(pattern):
    lps = [0] * len(pattern)
    length = 0
    i = 1
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps


def kmp_search(main_string, pattern):
    M = len(pattern)
    N = len(main_string)
    lps = compute_lps(pattern)
    i = j = 0
    while i < N:
        if pattern[j] == main_string[i]:
            i += 1
            j += 1
        elif j != 0:
            j = lps[j - 1]
        else:
            i += 1
        if j == M:
            return i - j
    return -1

# Boyer-Moore


def build_shift_table(pattern):
    table = {}
    length = len(pattern)
    for index, char in enumerate(pattern[:-1]):
        table[char] = length - index - 1
    table.setdefault(pattern[-1], length)
    return table


def boyer_moore_search(text, pattern):
    shift_table = build_shift_table(pattern)
    i = 0
    while i <= len(text) - len(pattern):
        j = len(pattern) - 1
        while j >= 0 and text[i + j] == pattern[j]:
            j -= 1
        if j < 0:
            return i
        i += shift_table.get(text[i + len(pattern) - 1], len(pattern))
    return -1

# Rabin-Karp


def polynomial_hash(s, base=256, modulus=101):
    n = len(s)
    hash_value = 0
    for i, char in enumerate(s):
        power_of_base = pow(base, n - i - 1) % modulus
        hash_value = (hash_value + ord(char) * power_of_base) % modulus
    return hash_value


def rabin_karp_search(main_string, substring):
    substring_length = len(substring)
    main_string_length = len(main_string)
    base = 256
    modulus = 101
    substring_hash = polynomial_hash(substring, base, modulus)
    current_slice_hash = polynomial_hash(
        main_string[:substring_length], base, modulus)
    h_multiplier = pow(base, substring_length - 1) % modulus

    for i in range(main_string_length - substring_length + 1):
        if substring_hash == current_slice_hash:
            if main_string[i:i+substring_length] == substring:
                return i
        if i < main_string_length - substring_length:
            current_slice_hash = (current_slice_hash -
                                  ord(main_string[i]) * h_multiplier) % modulus
            current_slice_hash = (
                current_slice_hash * base + ord(main_string[i + substring_length])) % modulus
            if current_slice_hash < 0:
                current_slice_hash += modulus
    return -1

# --- Завантаження текстів ---


def load_text(path):
    with open(path, "r", encoding="latin-1") as f:
        return f.read()


article1 = load_text("article1.txt")
article2 = load_text("article2.txt")

# --- Налаштування тестів ---
existing_pattern = "алгоритм"
missing_pattern = "немаєтакогослова"

tests = {
    "KMP_Article1_Exists": lambda: kmp_search(article1, existing_pattern),
    "KMP_Article1_Missing": lambda: kmp_search(article1, missing_pattern),
    "BM_Article1_Exists": lambda: boyer_moore_search(article1, existing_pattern),
    "BM_Article1_Missing": lambda: boyer_moore_search(article1, missing_pattern),
    "RK_Article1_Exists": lambda: rabin_karp_search(article1, existing_pattern),
    "RK_Article1_Missing": lambda: rabin_karp_search(article1, missing_pattern),
    "KMP_Article2_Exists": lambda: kmp_search(article2, existing_pattern),
    "KMP_Article2_Missing": lambda: kmp_search(article2, missing_pattern),
    "BM_Article2_Exists": lambda: boyer_moore_search(article2, existing_pattern),
    "BM_Article2_Missing": lambda: boyer_moore_search(article2, missing_pattern),
    "RK_Article2_Exists": lambda: rabin_karp_search(article2, existing_pattern),
    "RK_Article2_Missing": lambda: rabin_karp_search(article2, missing_pattern),
}

# --- Вимір часу виконання ---
print(f"{'Алгоритм':<8} {'Стаття':<9} {'Тип':<8} {'Час (сек)':<10}")
print("-" * 40)
for name, func in tests.items():
    time = timeit.timeit(func, number=10)
    algo, article, status = name.split("_")
    print(f"{algo:<8} {article:<9} {status:<8} {time:.6f}")
