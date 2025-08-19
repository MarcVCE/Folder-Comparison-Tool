import os
from pathlib import Path

# ====== SET YOUR FOLDERS HERE ======
DIR_A = Path(r"G:\folder\folder")   # Folder A (reference)
DIR_B = Path(r"C:\Users")   # Folder B (to compare)
# ===================================

def collect_names(root: Path):
    files = set()
    for dirpath, _, filenames in os.walk(root):
        for fn in filenames:
            files.add(fn)  # only name + extension
    return files

def main():
    if not DIR_A.is_dir() or not DIR_B.is_dir():
        print("⚠️ Check the paths: one of them is not a valid directory.")
        return

    set_a = collect_names(DIR_A)
    set_b = collect_names(DIR_B)

    missing_in_b = sorted(set_a - set_b)
    missing_in_a = sorted(set_b - set_a)

    print(f"📂 Comparing:\nA = {DIR_A}\nB = {DIR_B}\n")

    print(f"❌ Files present in A but missing in B ({len(missing_in_b)}):")
    for f in missing_in_b:
        print("   -", f)
    print()

    print(f"❌ Files present in B but missing in A ({len(missing_in_a)}):")
    for f in missing_in_a:
        print("   -", f)

if __name__ == "__main__":
    main()

