# README

## Framework: BDD_FRAMEWORK + PyTest + POM

---

### **Project Overview**

The **INDEE_PROJECT** demonstrates the following actions on the website:
1. **Sign-in**
2. **Select a video**
3. **Perform video operations**
4. **Sign-out**

---

### **Framework Overview**

The project is designed using both **BDD Framework Style** and **PyTest**, implementing the **Page Object Model (POM)** strategy.

#### **Project Structure**

```
INDEE_PROJECT/
├── features/
│   ├── steps/                # BDD Step definition files
│   ├── feature/              # Feature files
│   └── environment.py        # Environment Configuration file
├── tests/
│   ├── pages/                # POM files
│   ├── py_test/              # PyTest executable files
│   └── utils/                # Utility files for the project
├── chromedriver              # WebDriver for browser automation
├── requirements.txt          # Dependencies file
├── README.md                 # Project description and instructions
```

---

### **How to Run the Project**

1. Navigate to the root folder `./INDEEPROJECT`.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

#### **Running Tests via PyTest**
Execute the PyTest file:
```bash
python ./INDEE_PROJECT/tests/py_test/test_indee.py
```

#### **Running Tests via Behave (BDD)**
Navigate to the project root folder and run the following command:
```bash
behave
```

---

### **Sample Output (Behave)**

```bash
$ behave
Feature: Test Indee Video Player Functionality # features/indee.feature:2

DevTools listening on ws://127.0.0.1:50176/devtools/browser/9e065af9-a141-4f57-b6b4-506cae5bb054
----------** DRIVER INITIATED **------------

  Scenario: Verify user can play, pause, and interact with the video player  # features/indee.feature:4       
    Given I navigate to Indee Tv                                             # features/steps/test_steps.py:10
    When I sign in using the access code "WVMVHWBS"                          # features/steps/test_steps.py:17
    And I navigate to the video section                                      # features/steps/test_steps.py:22
    And I play the video for 10 seconds                                      # features/steps/test_steps.py:29
    Then I resume the video                                                  # features/steps/test_steps.py:34
    And I change the volume to 50%                                           # features/steps/test_steps.py:39
    And I set the resolution to "480p"                                       # features/steps/test_steps.py:44
    And I pause and exit the player                                          # features/steps/test_steps.py:49
    And I sign out                                                           # features/steps/test_steps.py:54
----------**  Browser closed **------------

1 feature passed, 0 failed, 0 skipped
1 scenario passed, 0 failed, 0 skipped
9 steps passed, 0 failed, 0 skipped, 0 undefined
Took 1m12.504s
```

---

### **Sample Output (PyTest)**

```bash
$ pytest ./INDEE_PROJECT/tests/py_test/test_indee.py
============================= test session starts =============================
platform win32 -- Python 3.9.12, pytest-8.3.4, pluggy-1.5.0
rootdir: c:\Users\282384\OneDrive - Resideo\Documents\dhaksh\IndeeProject
collected 1 item

tests\py_test\test_indee.py .                                            [100%]

======================== 1 passed in 81.86s (0:01:21) =========================
Finished running tests!
```

---

### **Enhancements**
- Reporting functionality is yet to be improved for both **Behave** and **PyTest** outputs.

---

### **Author**
**Dhakshath Amin**  
Email: dhakshath.amin@gmail.com

