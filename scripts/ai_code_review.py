#!/usr/bin/env python3
"""
AI Code Review Script

Uses OpenAI GPT-4 to review code changes in Pull Requests.

Usage:
    # Review specific files
    python3 scripts/ai_code_review.py file1.py file2.js

    # Review all changed files in current PR
    python3 scripts/ai_code_review.py

Environment variables:
    OPENAI_API_KEY: OpenAI API key (required)
    GITHUB_TOKEN: GitHub token for PR comments (optional)
"""

import os
import sys
import subprocess
from typing import List, Dict
import json


def get_openai_client():
    """Get OpenAI client with API key validation."""
    try:
        import openai
    except ImportError:
        print("❌ Error: openai package not installed")
        print("Install with: pip install openai")
        sys.exit(1)

    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        print("❌ Error: OPENAI_API_KEY environment variable not set")
        sys.exit(1)

    return openai.OpenAI(api_key=api_key)


def get_git_diff(file_path: str = None) -> str:
    """
    Get git diff for file or all changes.

    Args:
        file_path: Specific file to diff (None for all changes)

    Returns:
        Git diff output
    """
    try:
        if file_path:
            cmd = ['git', 'diff', 'HEAD', '--', file_path]
        else:
            cmd = ['git', 'diff', 'HEAD']

        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout

    except subprocess.CalledProcessError as e:
        print(f"❌ Error getting git diff: {e}")
        return ""


def get_changed_files() -> List[str]:
    """
    Get list of changed files from git.

    Returns:
        List of changed file paths
    """
    try:
        result = subprocess.run(
            ['git', 'diff', '--name-only', 'HEAD'],
            capture_output=True,
            text=True,
            check=True
        )

        files = [
            f.strip()
            for f in result.stdout.split('\n')
            if f.strip() and is_code_file(f)
        ]

        return files

    except subprocess.CalledProcessError:
        return []


def is_code_file(file_path: str) -> bool:
    """Check if file is a code file worth reviewing."""
    code_extensions = {
        '.py', '.js', '.ts', '.jsx', '.tsx',
        '.java', '.go', '.rs', '.cpp', '.c', '.h',
        '.rb', '.php', '.swift', '.kt', '.cs',
        '.sh', '.bash', '.sql', '.vue', '.svelte'
    }

    return any(file_path.endswith(ext) for ext in code_extensions)


def review_code_with_ai(file_path: str, diff: str, client) -> Dict:
    """
    Review code using AI.

    Args:
        file_path: Path to file being reviewed
        diff: Git diff content
        client: OpenAI client

    Returns:
        Dict with review results
    """
    if not diff:
        return {
            'file': file_path,
            'issues': [],
            'summary': 'No changes to review'
        }

    prompt = f"""
Role: You are a senior code reviewer expert in software engineering best practices.

Action: Review this code change and identify potential issues.

Context:
- File: {file_path}
- This is a git diff showing the changes made

Diff:
```diff
{diff}
```

Expectations:
1. Identify potential bugs
2. Security vulnerabilities
3. Performance issues
4. Code quality improvements
5. Best practices violations

Format your response as JSON:
{{
    "issues": [
        {{
            "severity": "critical|high|medium|low",
            "type": "bug|security|performance|quality",
            "line": "line number if applicable",
            "description": "clear description",
            "suggestion": "how to fix it"
        }}
    ],
    "summary": "brief overall assessment"
}}

Keep it concise - max 5 most important issues.
"""

    try:
        response = client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2,
            response_format={"type": "json_object"}
        )

        content = response.choices[0].message.content

        # Parse JSON response
        result = json.loads(content)
        result['file'] = file_path

        return result

    except Exception as e:
        print(f"⚠️  Error reviewing {file_path}: {e}")
        return {
            'file': file_path,
            'issues': [],
            'summary': f'Error during review: {str(e)}'
        }


def format_review_markdown(reviews: List[Dict]) -> str:
    """
    Format review results as markdown.

    Args:
        reviews: List of review results

    Returns:
        Formatted markdown
    """
    lines = ["# 🤖 AI Code Review", ""]

    # Count issues by severity
    issue_counts = {'critical': 0, 'high': 0, 'medium': 0, 'low': 0}

    for review in reviews:
        for issue in review.get('issues', []):
            severity = issue.get('severity', 'low')
            issue_counts[severity] += 1

    # Summary
    lines.append("## 📊 Summary")
    lines.append("")
    lines.append(f"- 🔴 Critical: {issue_counts['critical']}")
    lines.append(f"- 🟠 High: {issue_counts['high']}")
    lines.append(f"- 🟡 Medium: {issue_counts['medium']}")
    lines.append(f"- 🔵 Low: {issue_counts['low']}")
    lines.append("")

    # Detailed reviews
    for review in reviews:
        file_path = review.get('file', 'Unknown')
        issues = review.get('issues', [])
        summary = review.get('summary', '')

        lines.append(f"## 📁 {file_path}")
        lines.append("")

        if summary:
            lines.append(f"**Overall**: {summary}")
            lines.append("")

        if issues:
            for i, issue in enumerate(issues, 1):
                severity = issue.get('severity', 'low')
                issue_type = issue.get('type', 'general')
                description = issue.get('description', '')
                suggestion = issue.get('suggestion', '')
                line = issue.get('line', '')

                # Severity emoji
                severity_emoji = {
                    'critical': '🔴',
                    'high': '🟠',
                    'medium': '🟡',
                    'low': '🔵'
                }.get(severity, '⚪')

                lines.append(f"### {severity_emoji} Issue #{i}: {severity.upper()}")
                lines.append("")
                lines.append(f"**Type**: {issue_type}")
                if line:
                    lines.append(f"**Line**: {line}")
                lines.append("")
                lines.append(f"**Description**: {description}")
                lines.append("")

                if suggestion:
                    lines.append(f"**Suggestion**: {suggestion}")
                    lines.append("")

        else:
            lines.append("✅ No issues found")
            lines.append("")

        lines.append("---")
        lines.append("")

    # Footer
    lines.append("*Generated by GPT-4 AI Code Review*")

    return "\n".join(lines)


def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(
        description='AI-powered code review using GPT-4'
    )
    parser.add_argument(
        'files',
        nargs='*',
        help='Files to review (default: all changed files)'
    )
    parser.add_argument(
        '--output',
        type=str,
        default='ai-review.md',
        help='Output file for review (default: ai-review.md)'
    )

    args = parser.parse_args()

    print("🤖 AI Code Review starting...\n")

    # Get OpenAI client
    client = get_openai_client()

    # Get files to review
    if args.files:
        files = args.files
    else:
        files = get_changed_files()

    if not files:
        print("⚠️  No files to review")
        sys.exit(0)

    print(f"Reviewing {len(files)} file(s):\n")
    for f in files:
        print(f"  - {f}")
    print("")

    # Review each file
    reviews = []

    for file_path in files:
        print(f"📝 Reviewing: {file_path}...")

        # Get diff
        diff = get_git_diff(file_path)

        if not diff:
            print(f"  ⚠️  No changes in {file_path}")
            continue

        # Review with AI
        review = review_code_with_ai(file_path, diff, client)
        reviews.append(review)

        # Print quick summary
        issue_count = len(review.get('issues', []))
        if issue_count > 0:
            print(f"  ⚠️  Found {issue_count} issue(s)")
        else:
            print(f"  ✅ No issues found")

    print("")

    # Generate markdown report
    markdown = format_review_markdown(reviews)

    # Write to file
    with open(args.output, 'w') as f:
        f.write(markdown)

    print(f"✅ Review complete! Report saved to: {args.output}")

    # Count total issues
    total_issues = sum(
        len(r.get('issues', []))
        for r in reviews
    )

    if total_issues > 0:
        print(f"\n⚠️  Found {total_issues} total issue(s)")
        sys.exit(1)  # Non-zero exit for CI/CD
    else:
        print("\n✅ No issues found!")
        sys.exit(0)


if __name__ == '__main__':
    main()
