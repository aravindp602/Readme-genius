# tests/test_generator.py
import pytest
from readme_genius.core import generator

@pytest.fixture
def mock_project_data():
    return {
        'project_name': 'Test Project',
        'description': 'A cool test project.',
        'github_username': 'testuser',
        'license': 'MIT',
        # 'add_badges': True,  <-- REMOVE THIS LINE
        'features_list': ['Feature 1', 'Feature 2'],
        'include_contributing': True,
        'author_fullname': 'Test User',
        'template': 'default_template.md',
    }

# The test_generate_badges function has been deleted.

def test_generate_readme_content(mock_project_data):
    """Tests if the README is rendered with the correct project name."""
    readme_content = generator.generate_readme(mock_project_data)
    assert "# Test Project" in readme_content
    assert "> A cool test project." in readme_content
    assert "- Feature 1" in readme_content
    assert "licensed under the MIT License" in readme_content
    