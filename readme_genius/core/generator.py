from jinja2 import Environment, FileSystemLoader
from pathlib import Path
import datetime

def generate_badges(data):
    """Generates Markdown for badges based on user answers."""
    if not data.get('add_badges'):
        return ""

    username = data['github_username']
    project = data['project_name'].lower().replace(' ', '-')
    license_type = data.get('license', 'None')
    
    badges = []
    badges.append(f"[![GitHub Stars](https://img.shields.io/github/stars/{username}/{project}?style=for-the-badge)](https://github.com/{username}/{project}/stargazers)")
    badges.append(f"[![GitHub Forks](https://img.shields.io/github/forks/{username}/{project}?style=for-the-badge)](https://github.com/{username}/{project}/network/members)")
    
    if license_type != 'None':
        badges.append(f"[![GitHub License](https://img.shields.io/github/license/{username}/{project}?style=for-the-badge)](./LICENSE)")
        
    return "\n".join(badges)

def generate_readme(data):
    """Renders the README template with the provided data."""
    data['badges'] = generate_badges(data)
    template_name = data.get('template', 'default_template.md')
    template_dir = Path(__file__).parent.parent / 'templates'
    env = Environment(loader=FileSystemLoader(template_dir), trim_blocks=True, lstrip_blocks=True)
    template = env.get_template(template_name)
    output = template.render(data)
    return output

def create_license_file(data):
    """Creates a LICENSE file based on the chosen license."""
    license_type = data.get('license')
    if not license_type or license_type == 'None':
        return None, None

    fullname = data.get('author_fullname', 'The Project Contributors')
    year = datetime.date.today().year
    
    license_template_dir = Path(__file__).parent.parent / 'templates' / 'licenses'
    env = Environment(loader=FileSystemLoader(license_template_dir))

    try:
        template = env.get_template(f"{license_type}.txt")
        content = template.render(year=year, fullname=fullname)
        
        with open("LICENSE", "w", encoding="utf-8") as f:
            f.write(content)
        
        return "LICENSE", "LICENSE file successfully created."
    except Exception as e:
        return None, f"Error creating LICENSE file: {e}"

def save_readme(content, path="README.md"):
    """Saves the generated content to a file."""
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    return path