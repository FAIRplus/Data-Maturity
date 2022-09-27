import pandas as pd


def create_md():
    """Method to automatically create glossary file for website."""
    glossary_file = pd.read_csv(
        'docs/glossary.tsv', sep='\t', usecols=['TERM', 'DESCRIPTION']
    )

    """Process to create template markdown"""
    template = """---
layout: default
title: Glossary
nav_order: 4
---

# Glossary terms
"""

    for row in glossary_file.values:
        (
            term_name,
            definition
        ) = row

        template += '\n'
        template += f'### {term_name} \n'
        if pd.notna(definition):
            template += definition + '\n'
        else:
            template += ' \n'

    with open('docs/Glossary.md', 'w') as f:
        print(template, file=f)


if __name__ == '__main__':
    create_md()
