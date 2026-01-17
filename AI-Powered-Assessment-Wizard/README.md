<div align="left" style="position: relative;">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" align="right" width="30%" style="margin: -20px 0 0 20px;">
<h1>AI-POWERED-ASSESSMENT-WIZARD</h1>
<p align="left">
	<em><code></code></em>
</p>
<p align="left">
	<img src="https://img.shields.io/github/license/ronak-create/AI-Powered-Assessment-Wizard.git?style=default&logo=opensourceinitiative&logoColor=white&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/ronak-create/AI-Powered-Assessment-Wizard.git?style=default&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/ronak-create/AI-Powered-Assessment-Wizard.git?style=default&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/ronak-create/AI-Powered-Assessment-Wizard.git?style=default&color=0080ff" alt="repo-language-count">
</p>
<p align="left"><!-- default option, no dependency badges. -->
</p>
<p align="left">
	<!-- default option, no dependency badges. -->
</p>
</div>
<br clear="right">

## 🔗 Table of Contents

- [📍 Overview](#-overview)
- [👾 Features](#-features)
- [📁 Project Structure](#-project-structure)
  - [📂 Project Index](#-project-index)
- [🚀 Getting Started](#-getting-started)
  - [☑️ Prerequisites](#-prerequisites)
  - [⚙️ Installation](#-installation)
  - [🤖 Usage](#🤖-usage)
  - [🧪 Testing](#🧪-testing)
- [📌 Project Roadmap](#-project-roadmap)
- [🔰 Contributing](#-contributing)
- [🎗 License](#-license)
- [🙌 Acknowledgments](#-acknowledgments)

---

## 📍 Overview

The **Online Assessment MCQ Answering System** is a web-based application designed to assist users in answering multiple-choice questions (MCQs) from images. The application leverages Google's Generative AI (GenAI) API to analyze uploaded images containing MCQs and generate the correct answers. 

### Key Components:
1. **Backend**:
   - Built using **Flask**, a lightweight Python web framework.
   - Handles image uploads, processes them using Google's Generative AI, and returns the answers in a structured JSON format.
   - Ensures proper sanitization and cleaning of the AI-generated responses.

2. **Frontend**:
   - Designed with **Tailwind CSS** for a clean, responsive, and user-friendly interface.
   - Allows users to upload images, submit them for processing, and view the results in a table format.

3. **AI Integration**:
   - Uses Google's **Gemini 1.5 Pro** model to analyze the images and extract correct answers.
   - The AI is prompted to return answers in a JSON format, making it easy to parse and display.

4. **Workflow**:
   - Users upload images of MCQs.
   - The backend processes the images using the AI model.
   - The AI generates answers, which are then displayed in a table on the frontend.

### Use Cases:
- **Students**: Quickly get answers to MCQs from textbooks, worksheets, or online assessments.
- **Educators**: Verify answers or generate answer keys for assessments.
- **Professionals**: Solve MCQ-based quizzes or tests efficiently.

### Technologies Used:
- **Python**: For backend logic and AI integration.
- **Flask**: For building the web application.
- **Google Generative AI**: For analyzing images and generating answers.
- **Tailwind CSS**: For styling the frontend.
- **JavaScript**: For handling form submissions and dynamically updating the UI.

### Why This Project?
- **Automation**: Saves time by automating the process of answering MCQs.
- **Accuracy**: Leverages state-of-the-art AI to provide accurate answers.
- **User-Friendly**: Simple and intuitive interface for seamless user experience.

---

## 👾 Features

The **Online Assessment MCQ Answering System** comes with the following features:

### 1. **Image Upload**
   - Users can upload one or multiple images containing multiple-choice questions (MCQs).
   - Supports common image formats (e.g., JPEG, PNG).

### 2. **AI-Powered Answering**
   - Utilizes **Google's Generative AI** (Gemini 1.5 Pro) to analyze the uploaded images.
   - Accurately identifies and extracts correct answers from the MCQs.

### 3. **Structured JSON Response**
   - The AI generates answers in a structured JSON format, making it easy to parse and display.
   - Example output format:
     ```json
     {
       "1": "A",
       "2": "C",
       "3": "B"
     }
     ```

### 4. **Dynamic Frontend Display**
   - Answers are displayed in a clean and responsive table on the frontend.
   - Built using **Tailwind CSS** for a modern and user-friendly interface.

### 5. **Error Handling**
   - Proper error handling for invalid image uploads or AI processing failures.
   - Displays meaningful error messages to the user.

### 6. **Sanitized Output**
   - The backend cleans and sanitizes the AI-generated text to ensure safe and readable output.
   - Removes unnecessary characters, null bytes, and HTML entities.

### 7. **Responsive Design**
   - The frontend is fully responsive and works seamlessly on desktops, tablets, and mobile devices.

### 8. **Easy to Use**
   - Simple and intuitive user interface for uploading images and viewing results.
   - No complex setup or configuration required for end-users.

### 9. **Extensible Architecture**
   - The project is designed to be easily extended with additional features, such as:
     - Support for PDF uploads.
     - Integration with other AI models.
     - User authentication and history tracking.

### 10. **Open Source**
   - The project is open-source, allowing developers to contribute, customize, and improve the application.
---

## 📁 Project Structure

```sh
└── AI-Powered-Assessment-Wizard.git/
    ├── __pycache__
    │   └── app.cpython-312.pyc
    ├── app.py
    └── templates
        └── index.html
```


### 📂 Project Index
<details open>
	<summary><b><code>AI-POWERED-ASSESSMENT-WIZARD.GIT/</code></b></summary>
	<details> <!-- __root__ Submodule -->
		<summary><b>__root__</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/ronak-create/AI-Powered-Assessment-Wizard.git/blob/master/app.py'>app.py</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- templates Submodule -->
		<summary><b>templates</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/ronak-create/AI-Powered-Assessment-Wizard.git/blob/master/templates/index.html'>index.html</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			</table>
		</blockquote>
	</details>
</details>

---
## 🚀 Getting Started

### ☑️ Prerequisites

Before getting started with AI-Powered-Assessment-Wizard.git, ensure your runtime environment meets the following requirements:

- **Programming Language:** Python


### ⚙️ Installation

Install AI-Powered-Assessment-Wizard.git using one of the following methods:

**Build from source:**

1. Clone the AI-Powered-Assessment-Wizard.git repository:
```sh
❯ git clone https://github.com/ronak-create/AI-Powered-Assessment-Wizard.git
```

2. Navigate to the project directory:
```sh
❯ cd AI-Powered-Assessment-Wizard.git
```

3. Install the project dependencies:

echo 'INSERT-INSTALL-COMMAND-HERE'



### 🤖 Usage
Run AI-Powered-Assessment-Wizard.git using the following command:
echo 'INSERT-RUN-COMMAND-HERE'

### 🧪 Testing
Run the test suite using the following command:
echo 'INSERT-TEST-COMMAND-HERE'

---
## 📌 Project Roadmap

- [X] **`Task 1`**: <strike>Implement feature one.</strike>
- [ ] **`Task 2`**: Implement feature two.
- [ ] **`Task 3`**: Implement feature three.

---

## 🔰 Contributing

- **💬 [Join the Discussions](https://github.com/ronak-create/AI-Powered-Assessment-Wizard.git/discussions)**: Share your insights, provide feedback, or ask questions.
- **🐛 [Report Issues](https://github.com/ronak-create/AI-Powered-Assessment-Wizard.git/issues)**: Submit bugs found or log feature requests for the `AI-Powered-Assessment-Wizard.git` project.
- **💡 [Submit Pull Requests](https://github.com/ronak-create/AI-Powered-Assessment-Wizard.git/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/ronak-create/AI-Powered-Assessment-Wizard.git
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="left">
   <a href="https://github.com{/ronak-create/AI-Powered-Assessment-Wizard.git/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=ronak-create/AI-Powered-Assessment-Wizard.git">
   </a>
</p>
</details>

---

## 🎗 License

This project is protected under the [SELECT-A-LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

## 🙌 Acknowledgments

- List any resources, contributors, inspiration, etc. here.

---
