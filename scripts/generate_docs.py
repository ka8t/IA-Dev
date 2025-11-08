#!/usr/bin/env python3
"""
Auto-generate table of contents for markdown files.

This script scans markdown files and automatically generates/updates
table of contents based on headers.

Usage:
    python3 scripts/generate_docs.py
    python3 scripts/generate_docs.py --file guides/Quick_Start_Dev.md
"""

import re
import os
import sys
from pathlib import Path
from typing import List, Tuple


def extract_headers(content: str) -> List[Tuple[int, str, str]]:
    """
    Extract headers from markdown content.

    Args:
        content: Markdown file content

    Returns:
        List of tuples (level, title, anchor)
    """
    headers = []
    lines = content.split('\n')

    for line in lines:
        # Match markdown headers (# Header)
        match = re.match(r'^(#{1,6})\s+(.+)$', line)
        if match:
            level = len(match.group(1))
            title = match.group(2).strip()

            # Remove emoji and special chars for anchor
            anchor = title.lower()
            anchor = re.sub(r'[^\w\s-]', '', anchor)
            anchor = re.sub(r'[-\s]+', '-', anchor)

            headers.append((level, title, anchor))

    return headers


def generate_toc(headers: List[Tuple[int, str, str]], max_level: int = 3) -> str:
    """
    Generate table of contents from headers.

    Args:
        headers: List of (level, title, anchor) tuples
        max_level: Maximum header level to include (default: 3)

    Returns:
        Generated TOC markdown
    """
    toc_lines = ["## 📋 Table des matières", ""]

    for level, title, anchor in headers:
        # Skip title and TOC itself
        if title.lower().startswith('table des matières'):
            continue

        # Only include headers up to max_level
        if level > max_level:
            continue

        # Indent based on level
        indent = "  " * (level - 1)

        # Create list item with link
        toc_line = f"{indent}- [{title}](#{anchor})"
        toc_lines.append(toc_line)

    return "\n".join(toc_lines)


def update_markdown_toc(file_path: str, dry_run: bool = False) -> bool:
    """
    Update table of contents in a markdown file.

    Args:
        file_path: Path to markdown file
        dry_run: If True, only print changes without writing

    Returns:
        True if file was updated, False otherwise
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Extract headers
        headers = extract_headers(content)

        if not headers:
            print(f"⚠️  No headers found in {file_path}")
            return False

        # Generate new TOC
        new_toc = generate_toc(headers)

        # Check if TOC already exists
        toc_pattern = r'##\s+📋\s+Table des matières\s*\n(.*?)(?=\n##|\n---|\Z)'
        toc_match = re.search(toc_pattern, content, re.DOTALL)

        if toc_match:
            # Replace existing TOC
            old_toc = toc_match.group(0)
            updated_content = content.replace(old_toc, new_toc)

            if old_toc.strip() == new_toc.strip():
                print(f"✅ {file_path} - TOC already up to date")
                return False
        else:
            # Insert TOC after first header
            first_header_match = re.search(r'^#\s+.+$', content, re.MULTILINE)
            if first_header_match:
                insert_pos = first_header_match.end()
                updated_content = (
                    content[:insert_pos] +
                    "\n\n" + new_toc + "\n" +
                    content[insert_pos:]
                )
            else:
                print(f"⚠️  Could not find insertion point in {file_path}")
                return False

        # Write updated content
        if dry_run:
            print(f"🔍 {file_path} - Would update (dry run)")
            print("\nNew TOC:")
            print(new_toc)
        else:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            print(f"✅ {file_path} - TOC updated")

        return True

    except Exception as e:
        print(f"❌ Error processing {file_path}: {e}")
        return False


def find_markdown_files(root_dir: str = '.') -> List[str]:
    """
    Find all markdown files in directory recursively.

    Args:
        root_dir: Root directory to search

    Returns:
        List of markdown file paths
    """
    markdown_files = []
    exclude_dirs = {'.git', 'node_modules', 'venv', '__pycache__', '.github'}

    for root, dirs, files in os.walk(root_dir):
        # Remove excluded directories
        dirs[:] = [d for d in dirs if d not in exclude_dirs]

        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                markdown_files.append(file_path)

    return markdown_files


def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(
        description='Generate table of contents for markdown files'
    )
    parser.add_argument(
        '--file',
        type=str,
        help='Specific markdown file to process'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Show changes without writing files'
    )
    parser.add_argument(
        '--max-level',
        type=int,
        default=3,
        help='Maximum header level to include in TOC (default: 3)'
    )

    args = parser.parse_args()

    print("📝 Generating table of contents...\n")

    if args.file:
        # Process single file
        files = [args.file]
    else:
        # Process all markdown files
        files = find_markdown_files()

    # Filter out certain files
    excluded_files = {'README.md', 'CHANGELOG.md', 'LICENSE.md'}
    files = [
        f for f in files
        if os.path.basename(f) not in excluded_files
    ]

    if not files:
        print("⚠️  No markdown files found")
        return

    print(f"Found {len(files)} markdown files\n")

    updated_count = 0
    for file in sorted(files):
        if update_markdown_toc(file, dry_run=args.dry_run):
            updated_count += 1

    print(f"\n{'🔍' if args.dry_run else '✅'} Complete!")
    print(f"Updated {updated_count}/{len(files)} files")


if __name__ == '__main__':
    main()
