# Звіт: Порівняння алгоримів пошуку підрядка

## Опис завдання

Програмно реалізовано три алгоритми пошуку підрядка:

* Алгоритм Кнута-Морріса-Пратта (KMP)
* Алгоритм Боєра-Мура (BM)
* Алгоритм Рабіна-Карпа (RK)

Для двох статей (текстових файлів `article1.txt` та `article2.txt`) здійснено пошук двох видів підрядків:

* існуючого (слово "алгоритм")
* вигаданого (слово "немаєтакогослова")

Застосовано модуль `timeit` для вимірювання часу виконання кожного алгоритму під час 10-ти ітерацій.



## Результати тестування
# Substring Search Algorithms Benchmark

This project compares the performance of three substring search algorithms:

- **Knuth-Morris-Pratt (KMP)**
- **Boyer-Moore (BM)**
- **Rabin-Karp (RK)**

Testing was conducted using two different text files (`article1.txt` and `article2.txt`) with two types of search targets:

- A substring that exists in the text: `"алгоритм"`
- A substring that does not exist in the text: `"немаєтакогослова"`

## Benchmark Results

| Algorithm | Article  | Search Type | Time (sec) |
|-----------|----------|-------------|------------|
| KMP       | Article1 | Exists      | 0.0136     |
| KMP       | Article1 | Missing     | 0.0125     |
| BM        | Article1 | Exists      | 0.0035     |
| BM        | Article1 | Missing     | 0.0017     |
| RK        | Article1 | Exists      | 0.0213     |
| RK        | Article1 | Missing     | 0.0213     |
| KMP       | Article2 | Exists      | 0.0273     |
| KMP       | Article2 | Missing     | 0.0275     |
| BM        | Article2 | Exists      | 0.0224     |
| BM        | Article2 | Missing     | 0.0050     |
| RK        | Article2 | Exists      | 0.0523     |
| RK        | Article2 | Missing     | 0.0522     |

## Conclusion

- **Boyer-Moore** showed the fastest performance overall across both articles.
- **KMP** demonstrated consistent average performance.
- **Rabin-Karp** was the slowest in all scenarios.

---

> Benchmarking was done using Python's `timeit` module with 10 iterations per test case.
## Висновки


* **Boyer-Moore** стабільно найкращий для великих текстів, оскільки має найкращі часові характеристики як для успішного, так і неуспішного пошуку.
* KMP доволі ефективний, але простий перегляд забирає більше ресурсів.
* RK не очікувано тупий для коротких підрядків у великих текстах.
