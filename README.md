# Study-Buddy

## Overview 

This project is an offline chatbot that runs locally with your own personal database. The project is tailored to students who want a focused and specific chatbot related to the subject they want to learn. The app personalizes its responses based on the files that you put in. 

This is the **public-facing mirror** of my project’s source code, which is primarily hosted and managed on **Azure DevOps**.

## Why Azure DevOps?
I use **Azure DevOps** for all code management, pull requests, and CI/CD pipelines, as it provides a robust and enterprise-level environment for development. I also am interested in DevOps and I feel like learning this tool will help in my growth. This GitHub repository is kept in sync with the Azure DevOps repository for public visibility and ease of access.

## Development Workflow
- All pull requests (PRs) are created and reviewed in **Azure DevOps**.
- CI/CD pipelines and automated builds are managed through **Azure Pipelines** (part of Azure DevOps).
- Wikis are also mirrored from **Azure DevOps**

If you would like to view the **Azure DevOps repository**, please contact me directly for access.

## Features

- **Personalized Chatbot**: Tailored responses based on uploaded class notes or documents.
- **Class Management**: Organize different subjects or classes within the app.
- **File Upload**: Upload files specific to each subject for better context during chatbot conversations.
- **Offline Mode**: Full functionality without the need for an internet connection.

## Technologies Used

### Front end

- **Tailwind CSS**: A utility-first CSS framework to build modern, responsive designs.
- **React**: A JavaScript library for building user interfaces.
- **React Router**: Declarative routing for React.
- **TypeScript**: A superset of JavaScript that adds static types.

### Back end

- **FastAPI (Python)**: A fast web framework for building APIs with Python 3.7+.
- **SQLite**: Local SQL database for offline storage.
- **FAISS**: A library for efficient similarity search and clustering of dense vectors, used for search capabilities in large datasets.
- **llama.cpp**: A library for running LLM (large language models), such as GPT-style models, for generating personalized chatbot responses.

## Testing Frameworks

This project uses the following testing frameworks to ensure the reliability and quality of the application.

### Frontend

- **Jest**: A JavaScript testing framework for running unit and integration tests.
    - To run the tests, use:
        ```bash
        npm run test
        ```
    - Or to run specifically Unit tests, Integration tests, etc.
        ```bash
        npm run test:jest:unit
        ```

### Backend

- **pytest**: A framework for Python to run tests and check the backend functionality.
    - To run the tests for the backend:
        ```bash
        pytest
        ```

## Steps to Run Locally 

## Usage

## License 
This project is licensed under MIT License
## Acknowledgements

## About