# tests/test_generator.py
import pytest
from readme_genius.core import generator

# A dictionary of mock data to use for testing
@pytest.fixture
def mock_project_data():
    return {
        'project_name': 'Test Project',
        'description': 'A cool test project.',
        'github_username': 'testuser',
        'license': 'MIT',
        'add_badges': True,
        'features_list': ['Feature 1', 'Feature 2'],
        'include_contributing': True,
        'author_fullname': 'Test User',
        'template': 'default_template.md', # Use a real template for rendering
    }

def test_generate_badges(mock_project_data):
    """Tests if badge generation works correctly."""
    badges = generator.generate_badges(mock_project_data)
    assert "img.shields.io/github/stars/testuser/test-project" in badges
    assert "img.shields.io/github/forks/testuser/test-project" in badges
    assert "img.shields.io/github/license/testuser/test-project" in badges

def test_generate_readme_content(mock_project_data):
    """Tests if the README is rendered with the correct project name."""
    readme_content = generator.generate_readme(mock_project_data)
    assert "# Test Project" in readme_content
    assert "> A cool test project." in readme_content
    assert "- Feature 1" in readme_content
    assert "licensed under the MIT License" in readme_content