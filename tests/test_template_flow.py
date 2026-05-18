import importlib.util
import pathlib
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github" / "workflows" / "build-kodi-repo.yml"
GENERATOR = ROOT / "tools" / "generate_repo.py"


def load_generator():
    spec = importlib.util.spec_from_file_location("generate_repo", GENERATOR)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class TemplateFlowTests(unittest.TestCase):
    def test_generator_uses_pages_url_from_environment(self):
        generator = load_generator()

        url = generator.resolve_repo_url(
            "repository.myrepo",
            {"KODI_REPO_URL": "https://example.github.io/kodi-repo"},
        )

        self.assertEqual(url, "https://example.github.io/kodi-repo/")

    def test_generator_keeps_legacy_url_fallback(self):
        generator = load_generator()

        url = generator.resolve_repo_url("repository.myrepo", {})

        self.assertEqual(url, "https://myrepo.github.io/myrepo/")

    def test_workflow_is_template_repo_friendly(self):
        workflow = WORKFLOW.read_text(encoding="utf-8")

        self.assertIn("workflow_dispatch:", workflow)
        self.assertIn("push:", workflow)
        self.assertIn("branches: [main]", workflow)
        self.assertIn("contents: read", workflow)
        self.assertNotIn("contents: write", workflow)
        self.assertNotIn("Commit generated repository output", workflow)
        self.assertNotIn("git push origin", workflow)
        self.assertIn("KODI_REPO_URL: https://${{ github.repository_owner }}.github.io/${{ github.event.repository.name }}/", workflow)


if __name__ == "__main__":
    unittest.main()
