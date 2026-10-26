import sys
from pathlib import Path
import unittest

# Pastikan starter dapat diimpor secara portabel
current_dir = Path(__file__).resolve().parent
starter_dir = current_dir.parent / "starter"
if str(starter_dir) not in sys.path:
    sys.path.insert(0, str(starter_dir))

from assignment import (
    Node,
    create_node_chain,
    evaluate_boolean_logic,
    set_operations_summary,
    traverse_and_count_nodes,
)


class TestModule00Assignment(unittest.TestCase):
    
    # -----------------------------------------------------------------------
    # Test Task 1: evaluate_boolean_logic
    # -----------------------------------------------------------------------
    def test_evaluate_boolean_logic(self):
        # AND
        self.assertTrue(evaluate_boolean_logic(True, True, "AND"))
        self.assertFalse(evaluate_boolean_logic(True, False, "AND"))
        self.assertFalse(evaluate_boolean_logic(False, False, "AND"))

        # OR
        self.assertTrue(evaluate_boolean_logic(True, False, "OR"))
        self.assertTrue(evaluate_boolean_logic(False, True, "OR"))
        self.assertFalse(evaluate_boolean_logic(False, False, "OR"))

        # NOT_P
        self.assertFalse(evaluate_boolean_logic(True, False, "NOT_P"))
        self.assertTrue(evaluate_boolean_logic(False, True, "NOT_P"))

        # XOR
        self.assertTrue(evaluate_boolean_logic(True, False, "XOR"))
        self.assertTrue(evaluate_boolean_logic(False, True, "XOR"))
        self.assertFalse(evaluate_boolean_logic(True, True, "XOR"))
        self.assertFalse(evaluate_boolean_logic(False, False, "XOR"))

        # IMPLIES (p -> q)
        # True -> True is True
        self.assertTrue(evaluate_boolean_logic(True, True, "IMPLIES"))
        # True -> False is False
        self.assertFalse(evaluate_boolean_logic(True, False, "IMPLIES"))
        # False -> True is True
        self.assertTrue(evaluate_boolean_logic(False, True, "IMPLIES"))
        # False -> False is True
        self.assertTrue(evaluate_boolean_logic(False, False, "IMPLIES"))

        # Invalid operation
        with self.assertRaises(ValueError):
            evaluate_boolean_logic(True, True, "UNKNOWN_OP")

    # -----------------------------------------------------------------------
    # Test Task 2: set_operations_summary
    # -----------------------------------------------------------------------
    def test_set_operations_summary(self):
        a = [1, 2, 2, 3, 4]
        b = [3, 4, 4, 5, 6]

        result = set_operations_summary(a, b)

        self.assertEqual(result["union"], [1, 2, 3, 4, 5, 6])
        self.assertEqual(result["intersection"], [3, 4])
        self.assertEqual(result["difference_a_b"], [1, 2])
        self.assertEqual(result["symmetric_diff"], [1, 2, 5, 6])

    def test_set_operations_summary_empty(self):
        a = []
        b = [10, 20]

        result = set_operations_summary(a, b)
        self.assertEqual(result["union"], [10, 20])
        self.assertEqual(result["intersection"], [])
        self.assertEqual(result["difference_a_b"], [])
        self.assertEqual(result["symmetric_diff"], [10, 20])

    # -----------------------------------------------------------------------
    # Test Task 3: create_node_chain
    # -----------------------------------------------------------------------
    def test_create_node_chain(self):
        # Test empty
        self.assertIsNone(create_node_chain([]))

        # Test single element
        head_single = create_node_chain([99])
        self.assertIsNotNone(head_single)
        self.assertEqual(head_single.val, 99)
        self.assertIsNone(head_single.next)

        # Test multiple elements
        head = create_node_chain([10, 20, 30])
        self.assertIsNotNone(head)
        self.assertEqual(head.val, 10)
        self.assertIsNotNone(head.next)
        self.assertEqual(head.next.val, 20)
        self.assertIsNotNone(head.next.next)
        self.assertEqual(head.next.next.val, 30)
        self.assertIsNone(head.next.next.next)

    # -----------------------------------------------------------------------
    # Test Task 4: traverse_and_count_nodes
    # -----------------------------------------------------------------------
    def test_traverse_and_count_nodes(self):
        # Empty chain
        count, values = traverse_and_count_nodes(None)
        self.assertEqual(count, 0)
        self.assertEqual(values, [])

        # Chain with 3 nodes
        n3 = Node("C")
        n2 = Node("B", next=n3)
        n1 = Node("A", next=n2)

        count, values = traverse_and_count_nodes(n1)
        self.assertEqual(count, 3)
        self.assertEqual(values, ["A", "B", "C"])


if __name__ == "__main__":
    unittest.main()
