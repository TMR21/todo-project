#!/bin/bash
set -euo pipefail

TASK_FILE="$1"
TEST_FILE="$2"
HTML_FILE="/github/workspace/index.html"

update_pre() {
  local id="$1"
  local content="$2"
  perl -0777 -pe "s|(<pre id=\"$id\">).*?(</pre>)|\$1\n$content\n\$2|s" -i "$HTML_FILE"
}

TODO_CONTENT="$(awk '/^ToDo Tasks:/{flag=1;next}/^Done Tasks:/{flag=0}flag' $TASK_FILE)"
DONE_CONTENT="$(awk '/^Done Tasks:/{flag=1;next}flag' $TASK_FILE)"
TESTS_CONTENT="$(cat $TEST_FILE)"

update_pre "todo-block" "$TODO_CONTENT"
update_pre "done-block" "$DONE_CONTENT"
update_pre "tests-block" "$TESTS_CONTENT"

echo "index.html updated successfully"

