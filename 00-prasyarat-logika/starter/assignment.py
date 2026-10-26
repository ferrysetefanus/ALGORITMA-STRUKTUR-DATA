"""
Assignment 00: Jembatan Logika & Pemrograman
Instruksi:
Selesaikan setiap fungsi yang memiliki tanda '# TODO:' di bawah ini.
Setelah selesai, jalankan unit test dengan perintah:
python -m unittest discover -s 00-prasyarat-logika/tests
"""

from typing import Any, Dict, List, Optional, Tuple


class Node:
    """
    Kelas dasar representasi Node (simpul data).
    Setiap node menyimpan sebuah nilai (val) dan referensi ke node berikutnya (next).
    """
    def __init__(self, val: Any, next: Optional["Node"] = None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f"Node({self.val})"


# ---------------------------------------------------------------------------
# Task 1: Evaluator Logika Boolean
# ---------------------------------------------------------------------------
def evaluate_boolean_logic(p: bool, q: bool, operation: str) -> bool:
    """
    Mengevaluasi operasi logika antara p dan q.
    
    Argumen:
        p: Nilai boolean pertama.
        q: Nilai boolean kedua.
        operation: Jenis operasi, salah satu dari:
                   - "AND"     : p AND q
                   - "OR"      : p OR q
                   - "NOT_P"   : Negasi dari p (mengabaikan q)
                   - "XOR"     : Exclusive OR (True jika nilai p dan q berbeda)
                   - "IMPLIES" : Implikasi logis p -> q (False hanya jika p=True dan q=False)
                   
    Returns:
        Hasil evaluasi boolean.
        
    Raises:
        ValueError: Jika jenis operasi tidak dikenali.
    """
    # TODO: Implementasikan logika evaluasi sesuai nilai 'operation'
    raise NotImplementedError("TODO: Kerjakan fungsi evaluate_boolean_logic")


# ---------------------------------------------------------------------------
# Task 2: Ringkasan Operasi Himpunan (Set Operations)
# ---------------------------------------------------------------------------
def set_operations_summary(list_a: List[Any], list_b: List[Any]) -> Dict[str, List[Any]]:
    """
    Menghasilkan ringkasan operasi himpunan dari dua buah list.
    Semua list output harus berisi elemen unik dan terurut (menggunakan sorted()).
    
    Argumen:
        list_a: List elemen pertama (bisa memuat duplikasi).
        list_b: List elemen kedua (bisa memuat duplikasi).
        
    Returns:
        Dictionary dengan 4 kunci:
        - "union"           : Gabungan semua elemen unik dari A dan B.
        - "intersection"    : Elemen yang ada di A DAN ada di B.
        - "difference_a_b"  : Elemen yang ada di A tetapi TIDAK ada di B.
        - "symmetric_diff"  : Elemen yang hanya ada di salah satu (A atau B, bukan keduanya).
    """
    # TODO: Gunakan tipe data set Python untuk melakukan operasi himpunan,
    # lalu kembalikan dalam bentuk list yang terurut menggunakan sorted().
    raise NotImplementedError("TODO: Kerjakan fungsi set_operations_summary")


# ---------------------------------------------------------------------------
# Task 3: Pembangun Rantai Node (Node Chain Builder)
# ---------------------------------------------------------------------------
def create_node_chain(values: List[Any]) -> Optional[Node]:
    """
    Membangun rantai Node berurutan dari sebuah list nilai.
    
    Contoh:
        Input: [10, 20, 30]
        Output: Node(10) -> Node(20) -> Node(30) -> None
        Fungsi harus mengembalikan node kepala (head), yaitu Node(10).
        
        Input: []
        Output: None
        
    Argumen:
        values: List nilai yang akan dimasukkan ke dalam node.
        
    Returns:
        Node pertama (head) dari rantai node yang terbentuk, atau None jika list kosong.
    """
    # TODO: Buat simpul-simpul Node dan hubungkan atribut .next dari simpul pertama hingga terakhir.
    raise NotImplementedError("TODO: Kerjakan fungsi create_node_chain")


# ---------------------------------------------------------------------------
# Task 4: Penelusuran & Penghitungan Rantai Node
# ---------------------------------------------------------------------------
def traverse_and_count_nodes(head: Optional[Node]) -> Tuple[int, List[Any]]:
    """
    Menelusuri rantai Node dari head sampai ujung (node dengan next == None).
    
    Contoh:
        Jika rantai adalah Node(1) -> Node(2) -> Node(3) -> None
        Output: (3, [1, 2, 3])
        
        Jika head adalah None
        Output: (0, [])
        
    Argumen:
        head: Node kepala dari rantai node.
        
    Returns:
        Tuple berupa: (jumlah_total_node, list_nilai_node_secara_berurutan)
    """
    # TODO: Gunakan perulangan while untuk menelusuri rantai pointer node.
    raise NotImplementedError("TODO: Kerjakan fungsi traverse_and_count_nodes")
