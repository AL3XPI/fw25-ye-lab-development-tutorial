# tests/test_functions.py
import json
import importlib.util
from pathlib import Path
import pytest

# ---- Optional import: pandas used in Task 2 tests ----
try:
    import pandas as pd  # noqa: F401
    _HAS_PANDAS = True
except Exception:
    _HAS_PANDAS = False

REPO = Path(__file__).resolve().parents[1]
SUBMISSIONS = REPO / "submissions"
COLLAB_JSON = REPO / "collaborators.json"
DATA_PATH = REPO / "data" / "animals.csv"  # Task 2 dataset


def _discover_targets():
    """
    Return a list of (label, folder_path) pairs to test.
    Includes placeholder entries for collaborators with missing folders.
    """
    targets = []
    missing = []

    if COLLAB_JSON.exists():
        try:
            mapping = json.loads(COLLAB_JSON.read_text(encoding="utf-8"))
        except Exception as e:
            raise SystemExit(f"❌ Failed to parse collaborators.json: {e}")

        for alias, folder_name in mapping.items():
            folder = SUBMISSIONS / folder_name
            if folder.is_dir():
                targets.append((alias, folder))
            else:
                missing.append(alias)
    else:
        # fallback: discover from filesystem
        if SUBMISSIONS.exists():
            for p in sorted(SUBMISSIONS.iterdir(), key=lambda x: x.name.lower()):
                if p.is_dir() and p.name != "_TEMPLATE_":
                    targets.append((p.name, p))

    if not targets and not missing:
        raise SystemExit(
            "❌ No submissions found.\n"
            "Create: submissions/<github-username>/task1.py\n"
            "Or add collaborators.json mapping aliases → folder names."
        )

    return targets, missing


TARGETS, MISSING = _discover_targets()


def _import_module_from_file(module_name: str, path: Path):
    """Generic import-by-path helper."""
    spec = importlib.util.spec_from_file_location(module_name, path)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


# =========================
# Task 1: loader + fixture
# =========================

def _load_task1_module(label: str, folder: Path):
    """Import that student's task1.py module and print a banner."""
    target = folder / "task1.py"
    if not target.exists():
        pytest.skip(f"[{label}] No task1.py file found in {folder}")

    print(f"\n{'=' * 72}")
    print(f"🔍 Testing {label.upper()}  ({folder.relative_to(REPO)}/task1.py)")
    print(f"{'=' * 72}")

    return _import_module_from_file("student_task1", target)


@pytest.fixture(params=TARGETS, ids=lambda t: t[0])
def student(request):
    label, folder = request.param
    return _load_task1_module(label, folder)


# ---------------------- TASK 1 TESTS ----------------------

def test_mean_basic(student):
    """Check correct mean on a small list."""
    result = student.mean([1, 2, 3, 4])
    assert result == 2.5, f"Expected mean=2.5 but got {result!r}"

def test_mean_raises_on_empty(student):
    """Empty list should raise an error."""
    with pytest.raises(Exception):
        student.mean([])

def test_moving_average(student):
    """Check 2-point moving average."""
    result = student.moving_average([1, 2, 3, 4], 2)
    assert result == [1.5, 2.5, 3.5], f"Incorrect moving average: {result}"

def test_moving_average_window_errors(student):
    """Invalid window sizes should raise."""
    with pytest.raises(Exception):
        student.moving_average([1, 2], 0)
    with pytest.raises(Exception):
        student.moving_average([1, 2], 3)

def test_top_k_basic(student):
    """Top-k should return the k largest values, descending."""
    result = student.top_k([5, 1, 3, 2, 4], 3)
    assert result == [5, 4, 3], f"Expected [5,4,3], got {result}"

def test_top_k_zero(student):
    """k=0 should return an empty list."""
    result = student.top_k([1, 2, 3], 0)
    assert result == [], f"Expected [], got {result}"

def test_top_k_ties(student):
    """Stable tie behavior."""
    result = student.top_k([3, 3, 2, 2, 1], 2)
    assert result == [3, 3], f"Expected [3,3], got {result}"


# =========================
# Task 2: loader + fixture
# =========================

def _load_task2_module(label: str, folder: Path):
    """Import that student's task2.py if present; otherwise skip for that student."""
    target = folder / "task2.py"
    if not target.exists():
        pytest.skip(f"[{label}] No task2.py yet in {folder} (skipping Task 2 for this collaborator)")

    print(f"\n{'-' * 72}")
    print(f"📊 Task 2 for {label.upper()}  ({folder.relative_to(REPO)}/task2.py)")
    print(f"{'-' * 72}")

    return _import_module_from_file("student_task2", target)


@pytest.fixture(params=TARGETS, ids=lambda t: t[0])
def student_task2(request):
    if not _HAS_PANDAS:
        pytest.skip("pandas not installed in this environment; skipping Task 2.")
    if not DATA_PATH.exists():
        pytest.skip(f"Dataset missing: {DATA_PATH} — add data/animals.csv to run Task 2 tests.")

    label, folder = request.param
    return _load_task2_module(label, folder)


# ---------------------- TASK 2 TESTS ----------------------

def test_task2_load_data_shape_and_types(student_task2):
    """load_data should read 40 rows and ensure 'healthy' is boolean dtype."""
    import pandas as pd  # local import to satisfy type checkers
    df = student_task2.load_data(str(DATA_PATH))
    assert isinstance(df, pd.DataFrame), "load_data must return a pandas DataFrame"
    assert len(df) == 40, f"Expected 40 rows, got {len(df)}"
    assert "healthy" in df.columns, "Column 'healthy' missing"
    # accept numpy bool_, pandas boolean, or Python bool
    is_bool = str(df["healthy"].dtype).lower() in {"bool", "boolean"}
    assert is_bool, f"'healthy' column should be boolean dtype; got {df['healthy'].dtype!r}"

def test_task2_count_by_species(student_task2):
    """Species counts should match the provided 40-row dataset."""
    df = student_task2.load_data(str(DATA_PATH))
    counts = student_task2.count_by_species(df)

    expected = {
        "mouse": 3,
        "rat": 4,
        "guinea_pig": 3,
        "hamster": 3,
        "gerbil": 3,
        "rabbit": 4,
        "dog": 4,
        "cat": 4,
        "pigeon": 3,
        "parrot": 3,
        "ferret": 3,
        "squirrel": 3,
    }
    # ensure all expected species present and counts match
    for sp, n in expected.items():
        assert counts.get(sp, 0) == n, f"Expected {n} {sp}, got {counts.get(sp)}"
    # ensure total adds to 40
    assert int(counts.sum()) == 40, f"Total count should be 40, got {int(counts.sum())}"

def test_task2_average_weight_sorted(student_task2):
    """average_weight_by_species should be sorted descending by mean weight."""
    df = student_task2.load_data(str(DATA_PATH))
    avgs = student_task2.average_weight_by_species(df)
    # check sorted descending
    vals = avgs.values.tolist()
    assert vals == sorted(vals, reverse=True), "Averages must be sorted descending by mean weight"
    # sanity: heaviest species should be 'dog' in this dataset (> 20kg)
    assert avgs.index[0] == "dog", f"Expected heaviest species 'dog', got {avgs.index[0]!r}"

def test_task2_heaviest_n_top2(student_task2):
    """heaviest_n should return top-N by weight desc; ties broken by id asc; index reset."""
    df = student_task2.load_data(str(DATA_PATH))
    top2 = student_task2.heaviest_n(df, 2)
    # Deterministic expectation for provided CSV: dog 28.0 (id=24), then 27.0 (id=22)
    assert list(top2["id"]) == [24, 22], f"Expected ids [24, 22] for top2, got {list(top2['id'])}"
    assert top2.index.tolist() == [0, 1], "Result index should be reset to 0..n-1"
    # n < 0 should raise
    with pytest.raises(ValueError):
        student_task2.heaviest_n(df, -1)


# ---------------------- REPORT MISSING ----------------------

def test_report_missing_collaborators():
    """Emit warnings for collaborators with no submissions (folder missing entirely)."""
    if not MISSING:
        pytest.skip("All collaborators submitted code ✅")

    print("\n⚠️  Missing submissions:")
    for alias in MISSING:
        print(f"   - {alias}")
    assert not MISSING, f"Missing submissions for: {', '.join(MISSING)}"
