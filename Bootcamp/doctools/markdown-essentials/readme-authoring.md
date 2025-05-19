Here is the complete content for `markdown-essentials/readme-authoring.md`:

---

# Writing a Quality README.md

A good `README.md` helps others understand, use, and contribute to your project. Below is a guide to writing a clear and effective README.

## Purpose

Begin with a short summary of what your project does and why it exists.

```markdown
# Project Name

This project is a simple weather application that shows current weather data using the OpenWeatherMap API. It is designed to demonstrate basic API integration and responsive web design.
```

## Installation

Explain how users can install or set up the project locally. Use code blocks for commands.

````markdown
## Installation

1. Clone the repository:

```bash
git clone https://github.com/username/project-name.git
````

2. Navigate to the project directory:

```bash
cd project-name
```

3. Install dependencies:

```bash
npm install
```

````

## Usage

Provide instructions and examples of how to run or use the project.

```markdown
## Usage

To start the development server:

```bash
npm start
````

Visit `http://localhost:3000` in your browser.
Search for a city name to view the current weather data.

````

## Troubleshooting

Mention common issues and how to solve them.

```markdown
## Troubleshooting

- **API Key Not Working:** Make sure you've added your API key in the `.env` file as `REACT_APP_API_KEY=your_key_here`.
- **Port Already in Use:** Change the port in the `.env` file or stop the service using the port.
````

## Badges (Optional)

You can add badges to show build status, license, or other metadata.

```markdown
## Badges

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Build](https://img.shields.io/github/workflow/status/username/project-name/CI)
```

---

Let me know if you'd like a template version that you can reuse for different projects.
