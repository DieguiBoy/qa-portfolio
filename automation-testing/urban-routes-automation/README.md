# Urban Routes – Automation Testing

## Project Description
This project contains automated end-to-end tests for the **Urban Routes web application**.  
The goal of this project is to validate the main user flow of the application using browser automation.

The automation framework was built using **Python**, **Selenium**, and **Pytest**, following a basic **Page Object Model (POM)** structure.

---

## Test Scope

The automated tests validate the main functionality of the application, including:

- Navigation through the application
- Form interactions
- Data validation
- User flow verification

---

## Tools Used

- Python
- Selenium WebDriver
- Pytest
- Git
- Visual Studio Code

---

## Project Structure


automation-testing/urban-routes-automation

* tests/ → Contains automated test cases
* data/ → Test data used in the tests
* utils/ → Helper functions
* requirements.txt → Project dependencies
* README.md → Project documentation


---

## Installation

Clone the repository:


git clone https://github.com/yourusername/qa-portfolio.git


Navigate to the project folder:


cd automation-testing/urban-routes-automation


Install dependencies:


pip install -r requirements.txt


---

## Running the Tests

To execute the test suite run:


pytest


---

## Test Approach

The project follows the **Page Object Model (POM)** design pattern to improve code readability and maintainability.

Each page of the application is represented as a class containing:

- UI locators
- Page interactions
- Methods used by the tests

---

## Author

QA Portfolio Project  
Automation testing practice using **Selenium and Pytest**.