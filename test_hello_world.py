# test_hello_world.py

from hello_world import main
from io import StringIO
import sys

def test_main_prints_hello_world():
    # Capture stdout
    captured = StringIO()
    sys.stdout = captured

    main()

    # Restore stdout
    sys.stdout = sys.__stdout__

    output = captured.getvalue().lower()
    assert "hellow" in output and "world" in output