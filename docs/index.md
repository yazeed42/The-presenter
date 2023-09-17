# Documentation

Purpose of each folder and file in the project structure:

---

### `The-Presenter/`

The root directory of your project, named after your project. All of your project files, documents, and sub-directories should be contained within this directory.

---

### `config/`

Stores configuration files and environment variables. Separates configuration from code and makes it easier to manage settings across different environments (development, staging, production).

- **`settings.ini`**: A file to store general settings like paths, API keys, or any other constants your project needs.

---

### `docs/`

Stores your project's documentation.

- **`index.md`**: The main documentation file that can serve as a starting point to navigate to other documentation.

---

### `src/`

The source code for your project.

- **`__init__.py`**: An empty file to indicate that the directory should be considered a Python package.
- **`main.py`**: The main application script where execution begins.
  
  - **`utils/`**: Utility scripts and helper functions.
    - **`__init__.py`**: An empty file to indicate that this is a Python package.
    
  - **`presentation/`**: Code related to converting presentations into videos.
    - **`__init__.py`**: An empty file to indicate that this is a Python package.
    
  - **`notes/`**: Code related to generating notes from videos or presentations.
    - **`__init__.py`**: An empty file to indicate that this is a Python package.

---


### Other important files:

- **`.gitignore`**: Lists files and directories that should not be tracked by Git.
- **`README.md`**: A markdown file containing information about the project and how to use it.
- **`CONTRIBUTING.md`**: Guidelines for how to contribute to the project.
- **`LICENSE`**: Contains license information.
- **`requirements.txt`**: Lists all Python dependencies required by the project.
- **`setup.py`**: Script for setting up the project environment.

---

### `laterstage/`

Contains folders for possible later stage of the project. Mainly for finetuning models and ML purposes. Also unit testing will come at a later stage.

---

### `laterstage/data/`

Contains the data sets that your project will use.

- **`raw/`**: Original, immutable data. This can include datasets you've downloaded or collected.
- **`processed/`**: Data that has been cleaned or transformed and is ready for analysis or model training.

---

### `laterstage/tests/`

Contains unit tests for your code to ensure that functions behave as expected.

- **`test_main.py`**: Unit tests for the main application logic.

---

### `laterstage/scripts/`

Standalone scripts that perform various tasks like data preprocessing or model evaluation.

- **`preprocess_data.py`**: A script to preprocess raw data and save it in a format ready for training.
- **`evaluate_model.py`**: A script to evaluate your trained model and generate performance metrics.

---

### `laterstage/models/`

Stores saved machine learning models.

---

### `laterstage/notebooks/`

Contains Jupyter notebooks for data analysis, prototyping, and other exploratory work.

---