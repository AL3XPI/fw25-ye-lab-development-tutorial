# Fall/Winter 2025 - Ye Lab Development Tutorial

Welcome!

You’ve already completed your **development environment setup** (VS Code, Python 3.10.11, virtual environment, GitHub account, etc.). This repository is the follow-up GitHub + Python intro task, where you will familiarize yourself with these tools and put your development environment to use.

This tutorial reinforces 4 core skills:
 - Writing Python modules
 - Running Jupyter/Python notebooks locally
 - Using `pytest` for basic testing
 - Working with GitHub branches and Pull Requests (PRs)

I realize that using generative AI tools can make this a 10-second task, and I'll have no way of knowing, but it would be great if you could try to follow along yourself. It's important to understand these tasks for our work, and learning the "mechanics" of mastering these techniques can make you a super-contributor as you progress here and beyond.


 ### Your responsibilities:
 - Create a folder in the submissions folder, with the same name as your GitHub username: **`submissions/<your-github-username>`**
 - All of your work for this task goes *inside that folder only.*
 - Please do not change any other aspect of this repo; the only files you're being asked to change are labeled "TODO" within the task files of your submissions folder.
 
#### Step 1: Create a new folder named "python-github-intro" inside of your **ye-lab** folder.


#### Step 2: Within your terminal/command line, navigate into your python-github-intro folder using "cd" (change diretory). 
Note: If you're unsure of how to find your new folder, you can find its "path", and simply enter "cd *copied-path*. The path should end in "/ye-lab/python-github-intro".
- To copy a file path on a Mac, Control-click or right-click the file, hold the Option key on your keyboard, and then select "Copy [File Name] as Pathname" to copy the full path to your clipboard. 
- On Windows, select the file in File Explorer, go to the Home tab in the ribbon, and click the Copy Path button.


#### Step 3: Once inside your new folder via terminal, clone this repo.
`git clone https://github.com/btmlnsn/fw25-ye-lab-development-tutorial`
Next, you'll want to enter the new folder created by cloning this repo:
`cd fw25-ye-lab-development-tutorial`


#### Step 4: Create and activate a virtual environment
Creating a virtual environment will keep your dependencies for this project isolated from other projects.
`python3 -m venv .venv`

Next, we will activate it.
On macOS: `source .venv/bin/activate`
On Windows: `.venv\Scripts\activate`

You should now see (.venv) appear at the start of your terminal prompt
When you run code within this project, make sure you activate the .venv in terminal before running any code. 

When you've finished running code, simply typing and entering "deactivate" in the terminal will deactivate the virtual environment. It can be relaunched using the same activate command above.


#### Step 5: Install dependencies
Now that your virtual environment is active, you will install the packages required for this project.
`pip install -r requirements.txt`
To confirm installation: `pip list`


#### Step 6: Create your Submission folder
Inside the 'submissions/' folder of this repo, create a new folder named exactly after your GitHub username. Copy and paste each of the files inside 'submissions/__TEMPLATE__' into your submissions folder.
Example:
    submissions/
    └── btmlnsn/
        ├── task1.py
        ├── task2.ipynb
        └── task2.py


#### Step 5: Complete the tasks
There are a total of 8 "TODO" statements, split across 2 tasks, that need attention. Please do not import any new modules. Any editing outside of these 8 TODO statements will not be necessary.
- Task 1: Python Basics
    Implement simple Python functions such as mean, moving average ,etc.
    Edit 'submissions/<your-github-username>/task1.py' using the provided template. There are 3 TODO statements to complete within your task1.py.

- Task2: Data Analysis with Pandas
    Load and analyze the provided dataset 'data/animals.csv'.
    Implement the functions described in 'submissions/<your-github-username>/task2.py', such as load_data, count_by_species, etc. There are 4 TODO statements that require code to be edited.
    Next, as your final TODO, you will run the provided cells within 'submissions/<your-github-username>/task2.ipynb' as-is, and ensure that they are all executed without error, and generate any intended output.


#### Step 6: Run Tests
Once you've written your code, in the terminal, run the automated tests with your activated .venv from the repo root:
`pytest -k <your-first-name-here>`
The test script is configured to work for the names Alex, Myra, Alisa, and Bobby.
If any tests fail, pytest will show an error message describing what went wrong.


#### Task 3: Writing and Submitting a Pull Request (PR)
Once your task 1 and task 2 code runs successfully and passes all tests, you'll practice making a **professional GitHub Pull Request (PR)** - the same process used in active development teams.

- 1. Create a new branch
    In your terminal, from the repo root:
   ```git checkout -b <your-first-name>-submission```
    Example:
    ```git checkout -b bobby-submission```

- 2. Stage and commit your work.
    Make sure your code is inside your own folder under 'submissions/'.
    Then commit:
    ```git add . ```
    ```git commit -m "Your message here" ```
    For your message, write a present-tense, descriptive yet concise message (e.g., 'Completed task1 and task2; good for review')

- 3. Push your branch
    ```git push origin <your-branch-name>```
    Example:
    ```git push origin bobby-submission```

    GitHub should give you a URL to "Open a Pull Request" - click it.

- 4. Create the Pull Request
    When writing your PR, it's important to carefully, concisely, and accurately document the changes to the repo you're proposing, the purpose, the benefits, and how they are implemented, all with an emphasis on readability. They should also be structured.

    - Title
        Your title should be something like:
        <Your-Name> - Task 1 & 2 Complete
        Feel free to choose whatever you'd like

    - PR Body
    Try to implement a structure that describes and organizes your PR. Choose any structure you'd like - this pull request is fairly straightforward, so it won't need much. A structure I personally use from time-to-time is:
        - Summary
        - Implementation (very brief for this PR - noting which files you've changed would be great)
        - Benefits (not necessary for this PR)
        - Notes (not necessary this time around probably, but useful to account for anything you'd like attention on that doesn't fit in the above categories - I tend to use this for file additions and new design patterns.)

- 5. Tag for Review
    Assign or mention: @btmlnsn
    Once submitted, I'll review your PR just like in a professional repository.

- 6. PR Review
    Please take a look at each of the other members' open PR's, review the files they've changed and are proposing, and leave a comment - it would be helpful to flag different solutions they've reached, but also describe any suggestions you have and commend others for their successes.

    I'll leave the PR's open for comments before merging and closing them so that everyone has a chance to take a look and double-check each others' work.

#### Complete!

Thank you for taking a look at this tutorial. Please feel free to reach out via Slack or email if you have any trouble. This is the first iteration I've made of this tutorial, so I apologize if anything breaks or if I've forgotten to add some content. 

Thanks again! Best of luck :)