# Modul 0: Jembatan Logika & Pemrograman (Prerequisite Bridge)

Selamat datang di modul pembuka! Modul ini dirancang khusus sebagai **jembatan tanpa rasa takut** untuk membekali Anda dengan konsep logika dasar dan mekanisme memori komputer sebelum melangkah ke analisis algoritma yang lebih dalam.

---

## 🎯 Tujuan Pembelajaran
Setelah menyelesaikan modul ini, Anda akan:
1. Memahami operasi logika boolean fundamental (`AND`, `OR`, `NOT`, `XOR`, dan `IMPLICATION`).
2. Memahami konsep himpunan (*Set Theory*) untuk mengenali keunikan data dan operasi relasional.
3. Memahami bagaimana Python mengelola memori (konsep *Reference/Pointer* objek).
4. Mampu merancang dan menghubungkan struktur `Node` pertama Anda menggunakan `class`.

---

## 📖 Materi Teori

### 1. Logika Boolean untuk Programmer
Komputer mengambil keputusan melalui aljabar Boolean (hanya bernilai `True` atau `False`).

| Operasi | Simbol Logika | Di Python | Cara Kerja |
| :--- | :---: | :---: | :--- |
| **AND** (Konjungsi) | $P \land Q$ | `p and q` | Bernilai `True` **hanya jika kedua kondisi** bernilai `True`. |
| **OR** (Disjungsi) | $P \lor Q$ | `p or q` | Bernilai `True` jika **salah satu atau kedua kondisi** bernilai `True`. |
| **NOT** (Negasi) | $\neg P$ | `not p` | Membalikkan nilai kebenaran (`True` jadi `False`, dan sebaliknya). |
| **XOR** (Exclusive OR) | $P \oplus Q$ | `p ^ q` | Bernilai `True` jika kedua kondisi **berbeda nilai**. |
| **IMPLICATION** | $P \implies Q$ | `(not p) or q` | "Jika P maka Q". Hanya bernilai `False` jika $P$ benar tetapi $Q$ salah. |

---

### 2. Teori Himpunan (*Set Theory*)
Himpunan adalah kumpulan objek-objek unik (tidak ada duplikasi).
- **Irisan (*Intersection*)**: Elemen yang ada di himpunan $A$ **DAN** di himpunan $B$.
- **Gabungan (*Union*)**: Semua elemen yang ada di $A$ **ATAU** di $B$.
- **Selisih (*Difference*)**: Elemen yang ada di $A$ tetapi **TIDAK ADA** di $B$.
- **Symmetric Difference**: Elemen yang hanya ada di salah satu himpunan (bukan irisan keduanya).

Visualisasi Diagram Venn:
```text
      Himpunan A            Himpunan B
    ┌───────────────┐     ┌───────────────┐
    │               │     │               │
    │   Hanya A     │Iris-│    Hanya B    │
    │  (Difference) │ an  │ (Difference)  │
    │               │     │               │
    └───────────────┴─────┴───────────────┘
```

---

### 3. Memori di Python: Variabel adalah Label, Bukan Kotak!
Banyak pemula membayangkan variabel seperti kotak fisik yang menyimpan nilai. Di Python, **semua data adalah objek di RAM**, dan variabel hanyalah **label/penunjuk (pointer/reference)** ke objek tersebut.

Perhatikan contoh penting ini:
```python
a = [1, 2, 3]
b = a          # b BUKAN salinan baru! b menunjuk ke list yang sama dengan a di memori.
b.append(4)

print(a)       # Output: [1, 2, 3, 4] -> a ikut berubah!
print(id(a) == id(b))  # Output: True (alamat memori persis sama)
```
> 💡 **Penting untuk Struktur Data**:
> Konsep "menunjuk alamat memori" inilah yang akan kita gunakan untuk membangun **Linked List, Tree, dan Graph**!

---

### 4. Mengenal Struktur `Node` (Pondasi Segala Struktur Data)
Hampir seluruh struktur data dinamis (Linked List, Binary Tree, Graph) dibangun dari bata fondasi yang disebut **Node (Simpul)**.

Sebuah Node sederhana memiliki dua hal:
1. `val`: Nilai/data yang disimpan (misal: angka, teks).
2. `next`: Referensi (tali penghubung) yang menunjuk ke Node berikutnya di memori.

```text
┌──────────────┐       ┌──────────────┐       ┌──────────────┐
│ val: 10      │       │ val: 20      │       │ val: 30      │
│ next: ───────┼─────> │ next: ───────┼─────> │ next: None   │
└──────────────┘       └──────────────┘       └──────────────┘
   (Head Node)                                   (Tail Node)
```

Implementasi dasar di Python:
```python
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

# Menghubungkan 3 node secara manual:
node3 = Node(30)
node2 = Node(20, next=node3)
node1 = Node(10, next=node2)  # node1 -> node2 -> node3
```

---

## 📝 Tugas Praktik (Assignment)

Buka file **`starter/assignment.py`** dan selesaikan 4 fungsi yang memiliki tanda `# TODO:`:

1. **`evaluate_boolean_logic(p: bool, q: bool, operation: str) -> bool`**
   - Menghitung hasil operasi logika berdasarkan string operasi: `"AND"`, `"OR"`, `"NOT_P"`, `"XOR"`, dan `"IMPLIES"`.
2. **`set_operations_summary(list_a: list, list_b: list) -> dict`**
   - Mengambil dua list (yang mungkin berisi duplikasi), lalu menghasilkan dictionary yang berisi:
     - `"union"`: list elemen gabungan unik terurut.
     - `"intersection"`: list elemen irisan unik terurut.
     - `"difference_a_b"`: list elemen yang ada di A tapi tidak ada di B (terurut).
     - `"symmetric_diff"`: list elemen yang hanya ada di salah satu (terurut).
3. **`create_node_chain(values: list) -> Optional[Node]`**
   - Menerima list nilai (misal: `[10, 20, 30]`) dan membangun rantai `Node` berurutan, lalu mengembalikan node kepala (*head*). Jika list kosong, kembalikan `None`.
4. **`traverse_and_count_nodes(head: Optional[Node]) -> tuple[int, list]`**
   - Menelusuri rantai node dari `head` sampai ujung (`next is None`), lalu mengembalikan pasangan: `(total_node, list_nilai)`.

---

## 🧪 Cara Menjalankan Automated Test

Setelah Anda mengisi fungsi di `starter/assignment.py`, jalankan perintah ini di terminal:

```powershell
python -m unittest discover -s 00-prasyarat-logika/tests
```

Jika semua jawaban Anda benar, Anda akan melihat pesan:
```text
Ran 4 tests in 0.002s
OK
```
