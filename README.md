# Copilot Instruction Generator

A Python utility for generating GitHub Copilot instruction files that help customize Copilot's behavior for your project.

## Introduction

This tool generates a structured instruction file for GitHub Copilot, which includes:
- Lessons learned and best practices
- Tool configurations and paths
- Task planning and scratchpad area
- Screenshot verification workflows
- Web scraping and search capabilities

## Setup

### Create Python Virtual Environment

1. Create a new virtual environment:
```bash
python -m venv venv
```

2. Activate the virtual environment:
- On macOS/Linux:
```bash
source venv/bin/activate
```
- On Windows:
```bash
venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Generate Instruction File

Use the following command to generate the Copilot instruction file:

```bash
python generate_copilot_instruction.py --tools-path tools/ --venv-path venv/ --output .github/copilot-instructions.md
```

Parameters:
- `--tools-path`: Path to tools directory (default: tools/)
- `--venv-path`: Path to virtual environment (default: venv/)
- `--output`: Output filename (default: global-copilot-instruction.md)

### Configure in Your IDE

#### Visual Studio Code
1. Install GitHub Copilot and GitHub Copilot Chat extensions
2. Open VS Code `settings.json` (Ctrl/Cmd + Shift + P, then type "Open Settings (JSON)")
3. Add the following configuration:
```json
{
    "github.copilot.chat.codeGeneration.instructions": "path/to/your/instruction/file"
}
```

#### JetBrains IDEs
1. Install GitHub Copilot plugin
2. Go to Settings/Preferences
3. Navigate to Languages & Frameworks > GitHub Copilot
4. Look for "Custom Instructions" section
5. Set the path to your generated instruction file

For more detailed configuration instructions, refer to:
- [GitHub Copilot Documentation](https://docs.github.com/en/copilot)
- [VS Code Copilot Extension](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot)
- [JetBrains Copilot Plugin](https://plugins.jetbrains.com/plugin/17718-github-copilot)

## Example Prompts

Here are some example prompts to test your Copilot configuration:

1. Task Planning:
```
Please help me plan the implementation of a new feature that involves web scraping and screenshot verification.
```

2. Code Generation:
```
Write a function that uses the screenshot verification tool to capture and verify a webpage's appearance.
```

3. Debug Assistance:
```
I'm getting an encoding error when searching for Japanese text. How can I fix this?
```

4. Best Practices:
```
What's the recommended way to handle multiline git commit messages in this project?
```

These prompts should trigger responses that incorporate the custom instructions and tools defined in your generated instruction file.
