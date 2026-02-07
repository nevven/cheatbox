import yaml
from pathlib import Path

class Data:
    data_dir = Path(__file__).parent.parent / "data"

    def __init__(self, domain: str):
        self.domain = domain
        self.content = self._read_domain()

    @classmethod
    def list_domains(cls) -> list[str]:
        """List available cheatsheets"""
        return sorted([file.stem for file in cls.data_dir.glob("*.yaml")])

    def _read_domain(self) -> dict:
        """Read the content of the domain"""
        file_path = self.data_dir / f"{self.domain}.yaml"
        if not file_path.exists():
            print(f"Cheatsheet '{self.domain}' not found.")
            print(f"Available: {', '.join(self.list_domains())}")
            return {}
        try:
            with open(file_path, 'r') as f:
                return yaml.safe_load(f)
        except Exception as e:
            print(f"Error loading {self.domain}.yaml: {e}")
            return {}
