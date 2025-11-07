
#!/bin/bash
set -euo pipefail

TASK_OUT="/tmp/tasks.out"
TEST_OUT="/tmp/tests.out"

python3 /github/workspace/.github/scripts/todo.py | tee "$TASK_OUT"
python3 /github/workspace/.github/scripts/todo-test.py | tee "$TEST_OUT" || true

bash /github/workspace/.github/scripts/update_index.sh "$TASK_OUT" "$TEST_OUT"

echo "Entrypoint completed successfully!"
