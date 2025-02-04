"""Includes a function to get presentation string"""
def presentation():
    """Get Presentation String."""
    with open('presentation.txt', 'r', encoding='utf-8') as file:
        return file.read()
