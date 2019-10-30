CYAN='\[\e[0;36m\]'
NC='\033[0m' # No Color

function title() {
  echo $1
  echo "----------"

}

function rap() {
  # run an pause
  read ANY
  (
    set -x
    $1
  )
  read ANY
}

function demo1() {
  clear
  echo "Demo 1"
  echo "======"
  title "Pytest feedback when failing..."
  rap "pytest tests/1_assert_info_fail_test.py"

  clear
  title "Let's see with success..."
  rap "pytest tests/1_assert_info_fail_test.py"
}

function demo2() {
  clear
  echo "Demo 2"
  echo "======"
  title "Unittest example"
  rap "python -m unittest tests/2_pytest_vs_unittest_test.py"

  clear
  title "Pytest example"
  rap "python -m pytest -s tests/2_pytest_vs_unittest_test.py"

  clear
  title "Selecting specific tests"
  rap "python -m pytest -s -k isupper tests/"

  clear
  title "Marked tests only"
  rap "python -m pytest -s -m awesome tests/"
}

demo1
demo2
