from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]

DATA_DIR = ROOT_DIR / "data"

RAW_DIR = DATA_DIR / "raw"
INTERIM_DIR = DATA_DIR / "interim"
PROCESSED_DIR = DATA_DIR / "processed"

AUH_DIR = RAW_DIR / "AUH"
CBTA_DIR = RAW_DIR / "CBT-CBA"
ENGHO_DIR = RAW_DIR / "ENGHO"
EPH_DIR = RAW_DIR / "EPH"
IPC_DIR = RAW_DIR / "IPC"