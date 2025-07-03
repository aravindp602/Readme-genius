import questionary
from rich.console import Console

console = Console()

def ask_for_features():
    """Asks the user to list project features one by one."""
    features = []
    console.print("\n[bold]List your project's features.[/bold]")
    console.print("Enter one feature per line. Press [bold]Enter[/bold] on an empty line when you're done.")
    
    while True:
        feature_text = questionary.text(f"  Feature #{len(features) + 1}:").ask()
        
        if not feature_text:
            break
        features.append(feature_text)
        
    return features

def get_project_info():
    """Asks the user a series of questions to gather project information."""

    console.print("\n[bold green]Welcome to Readme-Genius! ✨[/bold green]")
    console.print("Let's create a professional README for your project.")

    custom_style = questionary.Style([
        ('question', 'bold'),
        ('answer', 'fg:cyan bold'),
        ('pointer', 'fg:yellow bold'),
        ('highlighted', 'fg:yellow bold'),
        ('selected', 'fg:cyan bg:black'),
    ])

    questions = [
        {
            'type': 'input',
            'name': 'project_name',
            'message': 'What is your project\'s name?',
            'validate': lambda text: len(text) > 0 or "Please enter a project name."
        },
        {
            'type': 'select',
            'name': 'template',
            'message': 'Choose a README template:',
            'choices': [
                {'name': 'Default (Recommended)', 'value': 'default_template.md'},
                {'name': 'Minimalist', 'value': 'minimalist_template.md'}
            ],
        },
        {
            'type': 'input',
            'name': 'description',
            'message': 'Enter a short, catchy description of your project:',
        },
        {
            'type': 'input',
            'name': 'github_username',
            'message': 'What is your GitHub username?',
            'validate': lambda text: len(text) > 0 or "Please enter your GitHub username."
        },
        {
            'type': 'select',
            'name': 'license',
            'message': 'Choose a license for your project (this will also generate a LICENSE file):',
            'choices': ['MIT', 'Apache 2.0', 'None'],
        },
        {
            'type': 'input',
            'name': 'author_fullname',
            'message': 'Enter your full name (for the LICENSE file):',
            'when': lambda answers: answers['license'] != 'None',
            'validate': lambda text: len(text) > 0 or "Please enter your full name."
        },
        # --- REMOVED: The question about adding badges ---
        {
            'type': 'confirm',
            'name': 'include_contributing',
            'message': 'Do you want to include a "Contributing" section?',
            'default': True
        }
    ]

    answers = questionary.prompt(questions, style=custom_style)

    if not answers:
        raise KeyboardInterrupt("Readme generation cancelled.")
    
    answers['features_list'] = ask_for_features()

    return answers