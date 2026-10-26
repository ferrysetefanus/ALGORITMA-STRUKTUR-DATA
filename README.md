# 🎓 Kurikulum Algoritma & Struktur Data (Level S1)

Selamat datang di repositori media pembelajaran mandiri **Algoritma dan Struktur Data (ASD)** standar kurikulum Sarjana (S1) Teknik Informatika / Ilmu Komputer.

Repositori ini dirancang khusus dengan pendekatan **Hands-on & Test-Driven**: setiap materi teori langsung diikuti tantangan penulisan kode mandiri (*from scratch*) yang diuji secara otomatis menggunakan **Automated Unit Testing**.

---

## 📌 Peta Jalan Belajar (Roadmap & Progress Tracker)

Beri tanda centang `[x]` setiap kali Anda menyelesaikan tugas pada masing-masing modul:

- [ ] **[Modul 0: Jembatan Logika & Pemrograman (Prerequisite Bridge)](./00-prasyarat-logika/README.md)**
  - Pola Pikir Komputasi, Aljabar Boolean, Logika Himpunan visual, Referensi Objek RAM Python, dan Struktur Node Pertama.
- [ ] **Modul 1: Fondasi Analisis & Paradigma Dasar**
  - Notasi Asimptotik (Big-O, Big-$\Omega$, Big-$\Theta$), Model Memori Python, Analisis Rekursi vs Iterasi, dan Dynamic Array.
- [ ] **Modul 2: Struktur Data Linear Fundamental**
  - Singly & Doubly Linked List, Stack (LIFO), Queue (FIFO), dan Circular Ring Buffer.
- [ ] **Modul 3: Algoritma Pencarian & Pengurutan (Searching & Sorting)**
  - Binary Search, Sorting Dasar ($O(n^2)$), Sorting Tingkat Lanjut ($O(n \log n)$: Merge & Quick Sort), dan Analisis Kasus Terbaik/Terburuk.
- [ ] **Modul 4: Struktur Data Hirarkis (Tree & Heap)**
  - Binary Tree Traversal, Binary Search Tree (BST), Self-Balancing Tree Concept, Binary Heap & Priority Queue, serta Trie.
- [ ] **Modul 5: Hashing & Hash Table**
  - Hash Function, Collision Handling (Separate Chaining), Load Factor, Dynamic Resizing, dan Penerapan Pola Hashing.
- [ ] **Modul 6: Graph (Jaringan & Relasi)**
  - Representasi Graf, Traversal (BFS & DFS), Topological Sort, Shortest Path (Dijkstra), dan Minimum Spanning Tree (MST Kruskal / DSU).
- [ ] **Modul 7: Paradigma Desain Algoritma Lanjut**
  - Greedy Algorithms, Divide and Conquer, Dynamic Programming (1D & 2D Memoization/Tabulation), dan Backtracking.
- [ ] **Modul 8: Struktur Data Tingkat Lanjut & Capstone Project**
  - Disjoint Set Union (DSU), Segment Tree / Fenwick Tree, serta Proyek Akhir Terpadu Portofolio S1 (LRU Cache / Routing Engine).

---

## 🛠️ Cara Menggunakan Repositori Ini

### 1. Struktur Folder Setiap Modul
Di setiap modul, Anda akan menemukan struktur folder yang seragam:
```text
nama-modul/
├── README.md               # Baca ini terlebih dahulu! Teori, visualisasi, & petunjuk tugas
├── starter/assignment.py   # Tempat Anda menulis kode solusi Anda (isi TODO)
├── tests/test_assignment.py# Skrip otomatis untuk menguji apakah kode Anda sudah benar
└── solutions/solution.py   # Kunci solusi & penjelasan (gunakan hanya jika buntu)
```

### 2. Alur Belajar yang Disarankan
1. **Pelajari Materi**: Buka dan pelajari file `README.md` pada modul yang aktif.
2. **Kerjakan Tugas**: Buka file `starter/assignment.py` lalu isi bagian fungsi yang memiliki komentar `# TODO:`.
3. **Uji Kode Anda (Automated Test)**:
   Jalankan perintah test dari terminal untuk melihat apakah kode Anda lulus semua pengujian:
   ```powershell
   python -m unittest discover -s 00-prasyarat-logika/tests
   ```
   Atau untuk menjalankan seluruh test yang ada di repositori:
   ```powershell
   python -m unittest discover
   ```
4. **Catat & Commit ke Git**:
   Jika semua test sudah lulus (`OK`), simpan progres Anda ke Git:
   ```powershell
   git add .
   git commit -m "feat(module-00): solve assignment and pass all unit tests"
   ```

---

## 🚀 Repositori GitHub

Repositori ini telah terhubung ke GitHub:
**[https://github.com/ferrysetefanus/ALGORITMA-STRUKTUR-DATA](https://github.com/ferrysetefanus/ALGORITMA-STRUKTUR-DATA)**

Setiap kali Anda menyelesaikan modul baru atau tugas baru, cukup jalankan perintah berikut untuk menyinkronkan progres Anda:
```powershell
git add .
git commit -m "feat(modul-xx): selesai mengerjakan tugas"
git push
```

---

## 📖 Konteks Proyek untuk Kolaborator / AI Agent
Dokumen rancangan induk, arsitektur kurikulum menyeluruh, dan panduan untuk AI Agent masa depan dapat dibaca di **[issue.md](./issue.md)**.
