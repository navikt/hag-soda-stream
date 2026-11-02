import logging
from pathlib import Path
import warnings

from soda_core.contracts import verify_contract_locally

logging.basicConfig(level=logging.INFO)

warnings.filterwarnings("ignore", message='Your application has authenticated using end user credentials', category=Warning)

for file in sorted(Path("soda-checks").iterdir()):
    if file.is_file() and file.suffix in {".yaml", ".yml"}:
        verify_contract_locally(
            contract_file_path=str(file),
            data_source_file_path="soda-config/config.yaml",
        )
