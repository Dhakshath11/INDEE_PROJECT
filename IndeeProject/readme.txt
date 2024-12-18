********************************************************* README *************************************************** @dhakshath
Framwork : BDD_FRAMEWORK + PyTest + POM 
===============================================================================
INDEE_PROJECT Demostarts following action items on Website (in-Brief)
    1. Sign-in
    2. Select video
    3. Video operations
    4. Sign-out

------------------------- Framework Overview -------------------------------------
Project is designed with both "BDD_FRAMEWORK STYLE" & "PYTEST" designed with "PAGE OF OBJECT (POM)" Straetgy

Project structure as follows:
    ->INDEE_PROJECT/features/steps : BDD Step definition file
    ->INDEE_PROJECT/features/ : Feature file 
    ->INDEE_PROJECT/features/ : Environment Configuration file
    ->INDEE_PROJECT/tests/pages : POM files
    ->INDEE_PROJECT/tests/py_test : Executable file from PYTEST
    ->INDEE_PROJECT/tests/utils : Utility file of Project
    ->INDEE_PROJECT/ : Other additional files (readme, chromedriver, requirements)

------------------------- To Run Project --------------------------------------
1. Navigate to root folder ./INDEEPROJECT & run : pip install -r requirements.txt

>>>>>> To RUN via PYTEST
A) Execute ./INDEE_PROJECT/tests/py_test/test_indee.py

>>>>>> To RUN via BDD behave
B) In CMD navigate to ./INDEE_PROJECT & send command : $ behave



=============================== SAMPLE OUTPUT of behave ================================

behave
Feature: Test Indee Video Player Functionality # features/indee.feature:2

DevTools listening on ws://127.0.0.1:50176/devtools/browser/9e065af9-a141-4f57-b6b4-506cae5bb054
----------** DRIVER INITIATED **------------

  Scenario: Verify user can play, pause, and interact with the video player  # features/indee.feature:4       
    Given I navigate to Indee Tv                                             # features/steps/test_steps.py:10
    When I sign in using the access code "WVMVHWBS"                          # features/steps/test_steps.py:17
    And I navigate to the video section                                      # features/steps/test_steps.py:22
Created TensorFlow Lite XNNPACK delegate for CPU.
Attempting to use a delegate that only supports static-sized tensors with a graph that has dynamic-sized tensors (tensor#58 is a dynamic-sized tensor).
    And I play the video for 10 seconds                                      # features/steps/test_steps.py:29
    Then I resume the video                                                  # features/steps/test_steps.py:34
    And I change the volume to 50%                                           # features/steps/test_steps.py:39
    And I set the resolution to "480p"                                       # features/steps/test_steps.py:44
    And I pause and exit the player                                          # features/steps/test_steps.py:49
    And I sign out                                                           # features/steps/test_steps.py:54
[12704:15096:1218/232738.770:ERROR:command_buffer_proxy_impl.cc(331)] GPU state invalid after WaitForGetOffsetInRange.
----------**  Browser closed **------------

1 feature passed, 0 failed, 0 skipped
1 scenario passed, 0 failed, 0 skipped
9 steps passed, 0 failed, 0 skipped, 0 undefined
Took 1m12.504s


=============================== SAMPLE OUTPUT of PyTest ================================

Running pytest with args: ['-p', 'vscode_pytest', '--rootdir=c:\\Users\\282384\\OneDrive - Resideo\\Documents\\dhaksh\\IndeeProject', 'c:\\Users\\282384\\OneDrive - Resideo\\Documents\\dhaksh\\IndeeProject\\tests\\py_test\\test_indee.py::test_indee']
============================= test session starts =============================
platform win32 -- Python 3.9.12, pytest-8.3.4, pluggy-1.5.0
rootdir: c:\Users\282384\OneDrive - Resideo\Documents\dhaksh\IndeeProject
collected 1 item

tests\py_test\test_indee.py .                                            [100%]

======================== 1 passed in 81.86s (0:01:21) =========================
Finished running tests!


=================================================================================
Reporting to be enhanced....

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Author: Dhakshath Amin 
Email: dhakshath.amin@gmail.com