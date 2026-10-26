"""
KUNCI SOLUSI & PEMBAHASAN: Modul 0 (Jembatan Logika & Pemrograman)
Gunakan file ini sebagai referensi evaluasi mandiri atau jika Anda mengalami kebuntuan.
"""

from typing import Any, Dict, List, Optional, Tuple


class Node:
    def __init__(self, val: Any, next: Optional["Node"] = None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f"Node({self.val})"


# ---------------------------------------------------------------------------
# Solusi Task 1: Evaluator Logika Boolean
# ---------------------------------------------------------------------------
def evaluate_boolean_logic(p: bool, q: bool, operation: str) -> bool:
    """
    Pembahasan:
    - AND: bernilai True jika kedua operand True.
    - OR: bernilai True jika salah satu atau keduanya True.
    - NOT_P: pembalik nilai p (not p).
    - XOR: bernilai True jika p != q (eksklusif, tidak boleh sama).
    - IMPLIES: p -> q secara logika ekuivalen dengan (not p) or q.
      Artinya premis yang salah (p=False) selalu menghasilkan implikasi yang benar secara logika formal.
    """
    op = operation.upper()
    if op == "AND":
        return p and q
    elif op == "OR":
        return p or q
    elif op == "NOT_P":
        return not p
    elif op == "XOR":
        return p != q
    elif op == "IMPLIES":
        return (not p) or q
    else:
        raise ValueError(f"Operasi logika tidak dikenali: {operation}")


# ---------------------------------------------------------------------------
# Solusi Task 2: Ringkasan Operasi Himpunan (Set Operations)
# ---------------------------------------------------------------------------
def set_operations_summary(list_a: List[Any], list_b: List[Any]) -> Dict[str, List[Any]]:
    """
    Pembahasan:
    - Set di Python secara otomatis membuang duplikasi data.
    - Union: a_set | b_set
    - Intersection: a_set & b_set
    - Difference: a_set - b_set
    - Symmetric Difference: a_set ^ b_set
    - Penggunaan sorted() mengembalikan list yang terurut rapi.
    """
    set_a = set(list_a)
    set_b = set(list_b)

    return {
        "union": sorted(list(set_a | set_b)),
        "intersection": sorted(list(set_a & set_b)),
        "difference_a_b": sorted(list(set_a - set_b)),
        "symmetric_diff": sorted(list(set_a ^ set_b)),
    }


# ---------------------------------------------------------------------------
# Solusi Task 3: Pembangun Rantai Node (Node Chain Builder)
# ---------------------------------------------------------------------------
def create_node_chain(values: List[Any]) -> Optional[Node]:
    """
    Pembahasan:
    - Jika list kosong, tidak ada node yang bisa dibuat, kembalikan None.
    - Buat node pertama sebagai head.
    - Gunakan variabel penunjuk (current) untuk menyambungkan setiap node baru ke current.next,
      kemudian gerakkan current maju ke node baru tersebut.
    """
    if not values:
        return None

    head = Node(values[0])
    current = head

    for val in values[1:]:
        current.next = Node(val)
        current = current.next

    return head


# ---------------------------------------------------------------------------
# Solusi Task 4: Penelusuran & Penghitungan Rantai Node
# ---------------------------------------------------------------------------
def traverse_and_count_nodes(head: Optional[Node]) -> Tuple[int, List[Any]]:
    """
    Pembahasan:
    - Mulai penelusuran dari head.
    - Selama current bukan None, catat nilainya dan tambahkan penghitung (count).
    - Pindahkan pointer ke node berikutnya dengan `current = current.next`.
    - Ketika current mencapai None, artinya kita sudah sampai di ujung rantai.
    """
    count = 0
    values = []

    current = head
    while current is not None:
        count += 1
        values.append(current.val)
        current = current.next

    return count, values
