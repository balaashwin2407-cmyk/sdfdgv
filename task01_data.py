"""Task 1: data definition - inputs, named constants, types and validation rules."""
from decimal import Decimal

# Named constants (Decimal so money and percentages are exact)
BASE_RATE = Decimal("30.00")        # Rs per litre at 3.5% fat and 8.5% SNF
STD_FAT = Decimal("3.5")
STD_SNF = Decimal("8.5")
FAT_STEP_VALUE = Decimal("0.40")    # Rs per litre per 0.1% fat
SNF_STEP_VALUE = Decimal("0.30")    # Rs per litre per 0.1% SNF
STEP = Decimal("0.1")
MIN_FAT, MAX_FAT = Decimal("2.0"), Decimal("7.0")
MIN_SNF, MAX_SNF = Decimal("6.0"), Decimal("10.0")   # assumption
VALID_SHIFTS = ("M", "E")

# One sample entry showing the chosen data types
entry = {
    "farmer_id": "F0123",        # str  (identifier, not used in arithmetic)
    "litres": Decimal("8.5"),    # Decimal
    "fat": Decimal("4.2"),       # Decimal
    "snf": Decimal("8.7"),       # Decimal
    "shift": "M",                # str
}

def is_valid(e):
    """Return True when the entry satisfies every validation rule."""
    return (bool(e["farmer_id"])
            and e["litres"] >= 0
            and MIN_FAT <= e["fat"] <= MAX_FAT
            and MIN_SNF <= e["snf"] <= MAX_SNF
            and e["shift"] in VALID_SHIFTS)

if __name__ == "__main__":
    for key, value in entry.items():
        print(f"{key:10} {value!r:12} {type(value).__name__}")
    print("valid entry          :", is_valid(entry))
    print("negative litres      :", is_valid({**entry, "litres": Decimal("-1")}))
    print("fat 7.5 (too high)   :", is_valid({**entry, "fat": Decimal("7.5")}))
    print("shift 'X'            :", is_valid({**entry, "shift": "X"}))
