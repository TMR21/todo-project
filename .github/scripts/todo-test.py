# todo-test.py
import unittest
from io import StringIO
import sys
from todo import Task, TaskPool

class TestTaskPool(unittest.TestCase):
    def setUp(self):
        self.pool = TaskPool()
        self.pool.populate()

    def test_open_tasks(self):
        open_tasks = self.pool.get_open_tasks()
        self.assertTrue(all(t.status == "ToDo" for t in open_tasks))

    def test_done_tasks(self):
        done_tasks = self.pool.get_done_tasks()
        self.assertTrue(all(t.status == "Done" for t in done_tasks))

if __name__ == "__main__":
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestTaskPool)
    stream = StringIO()
    runner = unittest.TextTestRunner(stream=stream, verbosity=2)
    result = runner.run(suite)
    print(stream.getvalue())
    if not result.wasSuccessful():
        sys.exit(1)

