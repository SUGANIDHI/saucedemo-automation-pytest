# 🧪 Automated Web Testing: SauceDemo with Selenium & Pytest

This project showcases **data-driven test automation** for the [SauceDemo](https://www.saucedemo.com/) web application using **Selenium**, **Pytest**, and **Excel**. It validates login scenarios, simulates a complete purchase flow, and generates detailed HTML reports with screenshots.

---

## 📁 Project Structure

```
PROJECT-1/
├── main_test.py              # Main test script using Pytest & Selenium
├── generate_buyers.py        # Script to generate 'buyers.xlsx' with test users
├── buyers.xlsx               # Excel file with test data (auto-generated)
├── requirements.txt          # Python dependencies
├── report.html               # Pytest HTML test report
├── screenshots/              # Screenshots captured during test runs
└── README.md                 # Project documentation
```

---

## ⚙️ Tech Stack

- **Language**: Python 3.12  
- **Framework**: Pytest  
- **Automation**: Selenium WebDriver  
- **Reporting**: pytest-html  
- **Data Source**: pandas + openpyxl  
- **Browser**: Google Chrome (Headless mode supported)

---

## ✅ Features

- 🔐 Validates login with multiple user types via Excel
- 🛒 Automates full product purchase workflow
- 📊 Uses Excel (`buyers.xlsx`) for data-driven testing
- 📷 Captures screenshots during key test steps
- 📄 Generates professional HTML reports

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/PROJECT-1.git
cd PROJECT-1
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Generate Test Data

```bash
python generate_buyers.py
```

This creates `buyers.xlsx` with predefined test users.

### 4. Run the Tests

```bash
pytest main_test.py --html=report.html --self-contained-html
```

### 5. View the Report

Open `report.html` in your browser to view the test results.

---

## 📂 Sample Excel Format (`buyers.xlsx`)

| username          | password      |
|-------------------|---------------|
| standard_user     | secret_sauce  |
| locked_out_user   | secret_sauce  |
| problem_user      | secret_sauce  |

---

## 📸 Screenshots

Screenshots are saved in the `screenshots/` directory after key actions like login and order completion.

---

## 🧪 Sample Test Flow

1. Open SauceDemo homepage  
2. Read username & password from Excel  
3. Attempt login and validate outcome  
4. Add product to cart and proceed to checkout  
5. Capture screenshot after order completion  

---

## 🛡️ Best Practices Followed

- ✅ Headless browser for faster execution
- ✅ Parametrized tests using `@pytest.mark.parametrize`
- ✅ Clear assertions with descriptive error messages
- ✅ Separation of test logic and test data
- ✅ Modular code and organized folder structure

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to open an issue or submit a pull request.

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙋‍♀️ Author

**Suganidhi Baskar**  
Feel free to connect on [LinkedIn](https://www.linkedin.com/in/suganidhi-baskar-10090a256/) for collaborations or questions.

