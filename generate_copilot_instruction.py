import argparse
from pathlib import Path

"""
Usage:
python generate_copilot_instruction.py --tools-path tools/ --venv-path venv/ [--output global-copilot-instruction.md]

Parameters:
--tools-path Path to tools directory (e.g., tools/)
--venv-path  Path to virtual environment (e.g., venv/)
--output     Output filename (optional, defaults to global-copilot-instruction.md)

This script generates a global-copilot-instruction.md file suitable for Copilot Agent, 
with all tool command paths automatically replaced based on your parameters.
"""

TEMPLATE = '''# global-copilot-instruction.md

## Lessons

- Website image paths should use correct relative paths (e.g., 'images/filename.png') and ensure images directory exists
- Search results should handle different character encodings (e.g., UTF-8) correctly, especially for international queries
- Debug information should be output to stderr while keeping main output stdout clean for pipeline integration
- When using matplotlib's seaborn style, use 'seaborn-v0_8' instead of 'seaborn' to match newer seaborn versions
- With Jest, test suite can fail due to setup or lifecycle hooks even if all unit tests pass
- For Python development, activate venv and prefer `uv pip install` for dependencies, fallback to `pip`
- When using git/gh with multiline commit messages, write to file first then use `git commit -F <filename>`, add '[Cursor] ' to PR/commit message

## Tools Guide

> ⚙️ All tool paths (venv) and local relative root paths should be set via parameters, not hardcoded. Recommended to pass through script parameters.

### Screenshot Verification

- Screenshot Capture: `{venv_path}/bin/python3 {tools_path}screenshot_utils.py URL [--output OUTPUT] [--width WIDTH] [--height HEIGHT]`
- LLM Image Verification: `{venv_path}/bin/python3 {tools_path}llm_api.py --prompt "Your verification question" --provider {{openai|anthropic}} --image path/to/screenshot.png`
- Recommended to use APIs in `llm_api.py` for LLM calls

### Web Scraper

- Web Page Scraping: `{venv_path}/bin/python3 {tools_path}web_scraper.py --max-concurrent 3 URL1 URL2 URL3`

### Search Engine

- Search: `{venv_path}/bin/python3 {tools_path}search_engine.py "your search keywords"`

## Scratchpad (Task Planning Area)

This file can be used as a Scratchpad. For each new task, clear old tasks, explain the task, and plan steps.
Recommendations:
- Mark task progress with `[X]`/`[ ]`
- Update progress after completing subtasks
- Reflect and plan next steps after milestones
- Always refer to Scratchpad to maintain overall perspective and progress

---

Let me know if you need further refinements or additions!
'''

def main():
    parser = argparse.ArgumentParser(description='Generate global-copilot-instruction.md')
    parser.add_argument('--tools-path', type=str, required=True, help='Tools directory path, e.g., tools/')
    parser.add_argument('--venv-path', type=str, required=True, help='Virtual environment path, e.g., venv/')
    parser.add_argument('--output', type=str, default='global-copilot-instruction.md', help='Output filename')
    args = parser.parse_args()

    # Ensure paths end with /
    tools_path = args.tools_path
    if not tools_path.endswith('/'):
        tools_path += '/'
    venv_path = args.venv_path.rstrip('/')

    content = TEMPLATE.format(tools_path=tools_path, venv_path=venv_path)
    Path(args.output).write_text(content, encoding='utf-8')
    print(f'Generated {args.output}')

if __name__ == '__main__':
    main()
