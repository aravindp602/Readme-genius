import questionary
from rich.console import Console

console = Console()

def ask_for_custom_badges():
    """Asks the user to add any number of custom Markdown badges."""
    badges = []
    if not questionary.confirm("Do you want to add custom badges (e.g., for technologies, platforms)?", default=True).ask():
        return ""
        
    console.print("\n[bold]Paste each full Markdown badge on its own line.[/bold]")
    console.print("Example: [![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python)](https://www.python.org/)")
    console.print("Press [Enter] on an empty line when you're done.")
    
    while True:
        badge_text = questionary.text(f"  Badge #{len(badges) + 1}:").ask()
        if not badge_text:
            break
        badges.append(badge_text)
        
    return "\n".join(badges)

def ask_for_enhanced_features():
    """Asks for features with a title and a description."""
    features = []
    if not questionary.confirm("Do you want to add a 'Key Features' section?", default=True).ask():
        return features
        
    console.print("\n[bold]List your project's key features.[/bold]")
    console.print("Enter a title (e.g., 'User Authentication') and a short description for each feature.")
    
    while True:
        title = questionary.text(f"  Feature Title #{len(features) + 1} (or press Enter to finish):").ask()
        if not title:
            break
        
        description = questionary.text(f"    Description for '{title}':").ask()
        features.append({'title': title, 'description': description})
        
    return features

def ask_for_tech_stack():
    """Asks for technologies used, grouped by category."""
    tech_stack = {}
    if not questionary.confirm("Do you want to add a 'Technology Stack' section?", default=True).ask():
        return None
        
    console.print("\n[bold]List your project's technology stack.[/bold]")
    console.print("Group your technologies by category (e.g., Framework, Database, etc.).")
    
    while True:
        category = questionary.text("  Category (or press Enter to finish):").ask()
        if not category:
            break
        
        techs = questionary.text(f"    Technologies for '{category}' (comma-separated):").ask()
        if techs:
            tech_stack[category.strip()] = techs.strip()
            
    return tech_stack

def ask_for_custom_sections():
    """Asks the user to add any number of custom, free-form sections."""
    sections = []
    if not questionary.confirm("Do you want to add other custom sections (e.g., 'Installation', 'How it Works')?", default=True).ask():
        return sections
    
    console.print("\n[bold]Add your custom README sections.[/bold]")
    console.print("Provide a title and the full Markdown content for each section.")
    
    while True:
        title = questionary.text(f"  Section Title #{len(sections) + 1} (or press Enter to finish):").ask()
        if not title:
            break
        
        console.print(f"    Enter the Markdown content for '{title}'. Press [ESC] then [Enter] when done.")
        content = questionary.text("    Content:", multiline=True).ask()
        if content:
            sections.append({'title': title, 'content': content})
    
    return sections

def get_project_info():
    """Asks the user a series of questions to gather project information."""

    console.print("\n[bold green]Welcome to Readme-Genius! ✨[/bold green]")
    console.print("Let's create a professional README for your project.")

    custom_style = questionary.Style([('question', 'bold'), ('answer', 'fg:cyan bold'), ('pointer', 'fg:yellow bold')])

    answers = {}

    # --- Start with basic info ---
    answers['project_name'] = questionary.text('What is your project\'s name?', validate=lambda text: len(text) > 0).ask()
    answers['description'] = questionary.text('Enter a short, catchy description of your project:').ask()

    # --- New structured questions ---
    answers['badges'] = ask_for_custom_badges()
    answers['features_list'] = ask_for_enhanced_features()
    answers['tech_stack'] = ask_for_tech_stack()
    answers['custom_sections'] = ask_for_custom_sections()

    # --- Ask for standard sections at the end ---
    answers['include_contributing'] = questionary.confirm('Do you want to include a standard "Contributing" section?', default=True).ask()
    if answers['include_contributing']:
        answers['github_username'] = questionary.text('What is your GitHub username?', validate=lambda text: len(text) > 0).ask()

    answers['license'] = questionary.select('Choose a license for your project:', choices=['MIT', 'Apache 2.0', 'None']).ask()
    if answers['license'] != 'None':
        answers['author_fullname'] = questionary.text('Enter your full name (for the LICENSE file):', validate=lambda text: len(text) > 0).ask()

    if not answers:
        raise KeyboardInterrupt("Readme generation cancelled.")

    # Add template name manually as it's a fixed choice for this advanced generator
    answers['template'] = 'advanced_template.md'

    return answers