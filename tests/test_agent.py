import tempfile
import unittest
from pathlib import Path

from software_version_checker.agent import build_prompt, load_catalog


class CatalogTests(unittest.TestCase):
    def test_loads_catalog_file(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            catalog_path = Path(directory) / "languages.csv"
            catalog_path.write_text(
                "name,version,url\nPython,3.12,https://www.python.org/\n",
                encoding="utf-8",
            )

            self.assertEqual(
                load_catalog(catalog_path),
                [{"name": "Python", "url": "https://www.python.org/"}],
            )

    def test_rejects_catalog_missing_required_columns(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            catalog_path = Path(directory) / "languages.csv"
            catalog_path.write_text("language,version\nPython,3.12\n", encoding="utf-8")

            with self.assertRaisesRegex(ValueError, "name.*url"):
                load_catalog(catalog_path)

    def test_prompt_uses_current_lookup_and_official_source_hint(self) -> None:
        prompt = build_prompt(
            ["Python"],
            [{"name": "Python", "url": "https://www.python.org/"}],
        )

        self.assertIn("latest stable", prompt)
        self.assertIn("WebSearch and WebFetch", prompt)
        self.assertIn("https://www.python.org/", prompt)
        self.assertIn('"name": "Python"', prompt)


if __name__ == "__main__":
    unittest.main()
