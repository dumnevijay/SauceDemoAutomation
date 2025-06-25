QA Assignment
Automation testing for login, adding items to cart, filling out forms, placing orders, and logout functionality on SauceDemo.
🚀 Project Overview
This test suite automates end-to-end scenarios using Selenium WebDriver in Python 3.13+ to validate key user journeys and functionality. It covers login authentication, cart operations, form validations, and checkout flow using a clean uv-managed environment.
📂 How to Clone the Repository

```bash
git clone https://github.com/dumnevijay/SauceDemoAutomation.git
```

```bash
cd qa-assignment
```


Replace your-username with your actual GitHub username.


🧰 Environment Setup Using pipx + uv
1. Install pipx

```bash
pip install pipx
```

```bash
python -m pipx ensurepath
```


You may need to restart your terminal for pipx to be recognized.

2. Use pipx to Install uv

```bash
pipx install uv
```

🧪 Running Tests
To run all Selenium test cases:

```bash
uv python login.py
```


Adjust the path and filename to match your actual test entry point.

🛠 Tech Stack
- Python ≥ 3.13
- Selenium ≥ 4.33.0
- WebDriver Manager ≥ 4.0.2
- HTMLTestRunner ≥ 1.2.1
- uv – Fast, modern Python environment manager
- pipx – Tool to install Python CLIs in isolated environments

```bash
📁 Suggested Project Structure
qa-assignment/
├── Locators/
│   └── locators.py
├── Pages/
│   └── homePage.py
│   └── loginPage.py
├── login.py
├── reports/
│   └── test_report.html
├── pyproject.toml
└── README.md
```

Youtube Video link: https://youtu.be/ZzI75QUtr-o




