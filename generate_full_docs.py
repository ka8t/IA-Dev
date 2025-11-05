#!/usr/bin/env python3
import os
import shutil
import sys
from datetime import date

def create_file(path, content, overwrite=False):
    if os.path.exists(path) and not overwrite:
        print(f"⏭️  Fichier existant conservé : {path}")
        return
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✅ Créé : {path}")

def main(target_dir):
    print(f"🚀 Génération de la documentation dans : {target_dir}\n")
    os.makedirs(target_dir, exist_ok=True)

    # 1. Création de la structure
    folders = [
        '.github/ISSUE_TEMPLATE', 'guides', 'resources', 'examples',
        'scripts', 'assets/pdf', 'assets/visuals', 'archives'
    ]
    for d in folders:
        os.makedirs(os.path.join(target_dir, d), exist_ok=True)

    # 2. Copie des templates
    base = os.path.dirname(__file__)
    tpl = os.path.join(base, 'templates')

    create_file(os.path.join(target_dir, 'LICENSE'), open(os.path.join(tpl, 'LICENSE.txt')).read())
    create_file(os.path.join(target_dir, 'CONTRIBUTING.md'), open(os.path.join(tpl, 'CONTRIBUTING.md')).read())
    create_file(os.path.join(target_dir, 'CODE_OF_CONDUCT.md'), open(os.path.join(tpl, 'CODE_OF_CONDUCT.md')).read())
    create_file(os.path.join(target_dir, '.gitignore'), open(os.path.join(tpl, '.gitignore')).read())

    # 3. READMEs par dossier
    sub_tpl = os.path.join(tpl, 'folder_README_templates')
    for name in os.listdir(sub_tpl):
        folder_name = name.replace('.md', '')
        target_path = os.path.join(target_dir, folder_name, 'README.md')
        create_file(target_path, open(os.path.join(sub_tpl, name)).read())

    # 4. README racine
    root_readme = open(os.path.join(tpl, 'README_root.md')).read()
    create_file(os.path.join(target_dir, 'README.md'), root_readme, overwrite=True)

    print("\n🎉 Documentation générée avec succès.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("❌ Usage: python3 generate_full_docs.py /chemin/vers/projet")
        sys.exit(1)
    main(sys.argv[1])
