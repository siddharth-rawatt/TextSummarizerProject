from dataclasses import dataclass
from pathlib import Path


# Consider this as a entity for our configuration file
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path
