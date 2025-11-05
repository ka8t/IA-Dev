#!/usr/bin/env python3
"""
Script pour convertir les diagrammes Mermaid en images PNG
et générer un DOCX avec les images intégrées.
"""

import re
import subprocess
import os
from pathlib import Path

def extract_mermaid_blocks(md_file):
    """Extrait tous les blocs mermaid du fichier markdown."""
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Regex pour capturer les blocs ```mermaid ... ```
    pattern = r'```mermaid\n(.*?)```'
    blocks = re.findall(pattern, content, re.DOTALL)

    return content, blocks

def convert_mermaid_to_png(mermaid_code, output_path):
    """Convertit un bloc mermaid en PNG."""
    # Créer un fichier temporaire .mmd
    temp_mmd = output_path.replace('.png', '.mmd')

    with open(temp_mmd, 'w', encoding='utf-8') as f:
        f.write(mermaid_code)

    # Convertir avec mmdc
    cmd = [
        'mmdc',
        '-i', temp_mmd,
        '-o', output_path,
        '-b', 'transparent',
        '-t', 'default'
    ]

    try:
        subprocess.run(cmd, check=True, capture_output=True)
        print(f"✅ Converti: {output_path}")
        os.remove(temp_mmd)  # Nettoyer le fichier temporaire
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Erreur conversion {output_path}: {e.stderr.decode()}")
        if os.path.exists(temp_mmd):
            os.remove(temp_mmd)
        return False

def replace_mermaid_with_images(content, blocks, images_dir):
    """Remplace les blocs mermaid par des références d'images."""
    modified_content = content

    for i, block in enumerate(blocks):
        # Le bloc original avec les backticks
        original_block = f"```mermaid\n{block}```"

        # Le chemin de l'image
        image_path = f"{images_dir}/diagram_{i+1}.png"

        # Remplacer par une image markdown
        image_ref = f"![Diagramme {i+1}]({image_path})"

        modified_content = modified_content.replace(original_block, image_ref, 1)

    return modified_content

def main():
    # Chemins
    base_dir = Path("/Users/k/Documents/Documents - MacBook Pro de k/Code/IA-Dev")
    md_file = base_dir / "AI Driven Dev.md"
    images_dir = base_dir / "mermaid_diagrams"
    output_md = base_dir / "AI Driven Dev_with_images.md"
    output_docx = base_dir / "AI Driven Dev.docx"

    # Créer le dossier pour les images
    images_dir.mkdir(exist_ok=True)

    print("📖 Lecture du fichier Markdown...")
    content, blocks = extract_mermaid_blocks(md_file)

    print(f"✨ {len(blocks)} diagrammes Mermaid trouvés")

    # Convertir chaque bloc en PNG
    print("\n🔄 Conversion en PNG...")
    for i, block in enumerate(blocks):
        output_path = images_dir / f"diagram_{i+1}.png"
        convert_mermaid_to_png(block, str(output_path))

    # Créer un nouveau markdown avec les images
    print("\n📝 Génération du Markdown avec images...")
    modified_content = replace_mermaid_with_images(content, blocks, "mermaid_diagrams")

    with open(output_md, 'w', encoding='utf-8') as f:
        f.write(modified_content)

    print(f"✅ Markdown modifié: {output_md}")

    # Générer le DOCX avec pandoc
    print("\n📄 Génération du DOCX...")
    cmd = [
        'pandoc',
        str(output_md),
        '-o', str(output_docx),
        '--standalone',
        '--toc',
        '--toc-depth=3',
        '--resource-path', str(base_dir)
    ]

    subprocess.run(cmd, check=True)
    print(f"✅ DOCX généré: {output_docx}")

    print("\n🎉 Terminé ! Ouvrez 'AI Driven Dev.docx'")

if __name__ == "__main__":
    main()
