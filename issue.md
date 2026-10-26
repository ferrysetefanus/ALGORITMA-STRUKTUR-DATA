# ISSUE & ROADMAP MASTER: Algoritma & Struktur Data (Level S1)

> **Catatan untuk AI Agent / Developer Masa Depan**:
> File ini adalah *Single Source of Truth* (SSOT) yang memuat seluruh rancangan kurikulum, filosofi pembelajaran, arsitektur modul, standar penugasan, dan status progres pengerjaan repo ini.
> Jika Anda adalah AI Agent yang diminta melanjutkan proyek ini, **baca file ini terlebih dahulu** untuk memahami konteks, modul mana yang sudah selesai, modul yang sedang berjalan, dan aturan pembuatan modul berikutnya.

---

## 1. Identitas & Tujuan Proyek

- **Nama Proyek**: Pembelajaran Mandiri Algoritma & Struktur Data (Kurikulum Standar S1 Teknik Informatika / Ilmu Komputer).
- **Bahasa Utama**: **Python 3** (mengutamakan *clean code*, *type hinting* `typing`, dan tanpa ketergantungan library eksternal yang membungkus struktur data).
- **Test Runner**: Python bawaan `unittest` atau `pytest`.
- **Target Pembelajar**: Mahasiswa / Software Engineer yang ingin menguasai logika algoritma dari tingkat paling dasar (*scratch*) hingga mahir (*advanced*) tanpa harus mengambil perkuliahan formal Matematika Diskrit 1 semester penuh terlebih dahulu.

---

## 2. Filosofi & Metode Pembelajaran

1. **Implementasi From Scratch**: Dilarang langsung mengandalkan library instan bawaan (seperti `queue.Queue` atau `collections.deque` untuk materi antrean; semuanya harus dibuat dari nol menggunakan `class` dan manipulasi pointer/referensi objek).
2. **Just-in-Time Mathematics**: Konsep matematika (seperti teori graf, himpunan, induksi matematika, dan asimptotik) diajarkan tepat pada modul yang membutuhkannya secara visual dan aplikatif, bukan teoretis abstrak murni.
3. **Hands-on Task Driven**: Setiap topik wajib menuntut *output* nyata dari pembelajar berupa tugas yang diuji dengan **Automated Unit Testing**.
4. **Clean Git Portfolio**: Setiap modul dan tugas yang diselesaikan di-commit dengan rapi dan terdokumentasi agar siap dipush ke GitHub pribadi sebagai portofolio teknis.

---

## 3. Format Standar Struktur Setiap Modul

Setiap direktori modul wajib mengikuti template arsitektur berikut:

```text
[nomor-modul]-[nama-topik]/
│
├── README.md                   # Materi teori lengkap, visualisasi langkah komputasi,
│                               # analisis kompleksitas (waktu & memori), dan deskripsi tugas.
├── starter/                    # Folder template pengerjaan untuk pembelajar
│   ├── __init__.py
│   └── assignment.py           # Kode dengan komentar TODO, docstrings, & type hints
├── tests/                      # Folder automated testing
│   ├── __init__.py
│   └── test_assignment.py      # Kasus uji (normal, edge cases, boundary values)
└── solutions/                  # Kunci jawaban & analisis mendalam
    └── solution.py             # Solusi referensi jika pembelajar memerlukan evaluasi/buntu
```

---

## 4. Master Roadmap & Status Tracker

Gunakan checklist ini untuk melacak perkembangan:
- `[ ]` Belum Dibuat
- `[-]` Modul Aktif / Sedang Dikerjakan Pembelajar
- `[x]` Selesai & Lulus Unit Test

- [-] **Modul 0: Jembatan Logika & Pemrograman (Prerequisite Bridge)**
  - [x] Teori: Pola pikir komputasi, Aljabar Boolean, Logika Himpunan visual, Konsep Referensi Objek di RAM Python.
  - [-] Tugas: Evaluator ekspresi logika, manipulasi struktur `Node` berantai pertama (menunggu pengerjaan user).
  - [x] Unit Test: Validasi kebenaran logika & integritas node pointer (5 automated tests siap diuji).
- [ ] **Modul 1: Fondasi Analisis & Paradigma Dasar**
  - [ ] Teori: Notasi Asimptotik (Big-O, Big-$\Omega$, Big-$\Theta$), Call Stack Frame, Rekursi vs Iterasi.
  - [ ] Tugas: Perhitungan manual operasi loop bertingkat, `CustomDynamicArray` sederhana, Fast Exponentiation $O(\log n)$.
  - [ ] Unit Test: Validasi array dinamis dan solver rekursif.
- [ ] **Modul 2: Struktur Data Linear Fundamental**
  - [ ] 01: Singly & Doubly Linked List (Insert, Delete, Reverse In-Place).
  - [ ] 02: Stack (LIFO) & Kasus Validasi Kurung / Evaluasi Postfix.
  - [ ] 03: Queue (FIFO) & Circular Queue Ring Buffer.
- [ ] **Modul 3: Algoritma Pencarian & Pengurutan (Searching & Sorting)**
  - [ ] 01: Linear Search & Binary Search (Iteratif & Rekursif, Rotated Array Search).
  - [ ] 02: Sorting Dasar $O(n^2)$: Bubble, Selection, Insertion Sort.
  - [ ] 03: Sorting Lanjut $O(n \log n)$: Merge Sort & Quick Sort (Partisi Lomuto/Hoare).
  - [ ] 04: Benchmark Performa waktu nyata terhadap variasi ukuran $N$.
- [ ] **Modul 4: Struktur Data Hirarkis (Tree & Heap)**
  - [ ] 01: Binary Tree & 4 Metode Traversal (In/Pre/Post/Level-Order).
  - [ ] 02: Binary Search Tree (BST) lengkap dengan penghapusan node 2-anak.
  - [ ] 03: AVL Tree & Tree Rotations (Self-Balancing).
  - [ ] 04: Binary Heap (Min/Max Heap) & Priority Queue dari scratch.
  - [ ] 05: Trie (Prefix Tree) untuk kamus kata & Autocomplete.
- [ ] **Modul 5: Hashing & Hash Table**
  - [ ] 01: Konsep Hash Function, Modulo, Collision Handling (Separate Chaining).
  - [ ] 02: Load Factor, Re-hashing, & Dynamic Resizing $O(1)$ amortized.
  - [ ] 03: Implementasi custom `HashMap` dari nol dan problem Group Anagrams.
- [ ] **Modul 6: Graph (Jaringan & Relasi)**
  - [ ] 01: Representasi Graf (Adjacency Matrix & List).
  - [ ] 02: Traversal Graf: BFS & DFS.
  - [ ] 03: Topological Sort (Kahn's Algorithm & DFS) & Cycle Detection.
  - [ ] 04: Shortest Path: Dijkstra Algorithm & Bellman-Ford.
  - [ ] 05: Minimum Spanning Tree (MST): Kruskal (Disjoint Set Union / DSU) & Prim.
- [ ] **Modul 7: Paradigma Desain Algoritma Lanjut**
  - [ ] 01: Greedy Algorithms (Interval Scheduling, Fractional Knapsack).
  - [ ] 02: Divide and Conquer (Inversion Count, Kadane's Algorithm).
  - [ ] 03: Dynamic Programming (DP) 1D: Memoization vs Tabulation (Coin Change, Climbing Stairs).
  - [ ] 04: Dynamic Programming (DP) 2D: 0/1 Knapsack, Longest Common Subsequence.
  - [ ] 05: Backtracking: N-Queens Problem & Sudoku Solver.
- [ ] **Modul 8: Struktur Data Tingkat Lanjut & Capstone Project**
  - [ ] 01: Disjoint Set Union (DSU / Union-Find) dengan Path Compression & Rank.
  - [ ] 02: Segment Tree / Fenwick Tree (Range Sum Query).
  - [ ] 03: Capstone Mini Engine (Pilihan: In-Memory LRU Cache Engine / GPS Routing Engine / Mini Search Engine).

---

## 5. Panduan Instruksi bagi AI Agent yang Melanjutkan Repo Ini

Saat user meminta Anda untuk melanjutkan pengerjaan:
1. **Cek Checklist di Atas**: Periksa modul mana yang sedang bertanda `[-]` atau modul pertama yang masih `[ ]`.
2. **Jika Membantu User Belajar/Mengerjakan Tugas**:
   - Jangan langsung memberikan kode jawaban utuh kecuali user secara eksplisit meminta kunci jawaban.
   - Bimbing user dengan petunjuk logika (*hints*), visualisasi alur data, atau menjelaskan letak bug dari hasil uji `unittest`.
3. **Jika Membuka Modul Baru**:
   - Buat folder modul sesuai penomoran standar.
   - Tulis `README.md` modul dengan bahasa Indonesia yang jelas, edukatif, bersahabat, dan kaya contoh visual (ASCII/diagram).
   - Buat `starter/assignment.py` dengan fungsi ber-`TODO`, `docstrings` jelas, dan `typing`.
   - Buat `tests/test_assignment.py` dengan skenario uji komprehensif.
   - Buat `solutions/solution.py` sebagai referensi.
   - Perbarui checklist di file `issue.md` ini dan `README.md` utama.
   - Jalankan `python -m unittest discover` untuk memastikan seluruh struktur test berjalan tanpa galat sintaks.
4. **Git Commit Standard**:
   - Gunakan format konvensional, contoh:
     - `feat: setup initial repository structure and curriculum roadmap`
     - `feat(module-00): add prerequisite logic module with starter and tests`
     - `docs: update issue.md progress tracker`
