import pathlib
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github" / "workflows" / "build-kodi-repo.yml"
README = ROOT / "README.md"


class ManualWorkflowTests(unittest.TestCase):
    def test_build_workflow_is_manual_only(self):
        workflow = WORKFLOW.read_text(encoding="utf-8")

        self.assertIn("workflow_dispatch:", workflow)
        self.assertNotIn("\n  push:", workflow)
        self.assertNotIn("branches: [main]", workflow)

    def test_readme_tells_users_to_run_workflow_manually(self):
        readme = README.read_text(encoding="utf-8")

        self.assertIn("Run workflow", readme)
        self.assertIn("The workflow does not run automatically when you upload files", readme)
        self.assertNotIn("git push origin main", readme)


if __name__ == "__main__":
    unittest.main()
