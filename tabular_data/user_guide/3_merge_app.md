# 3. Setting up the Column Merge App (Intermediate)

The Column Merge app has been produced to allow you to combine columns from across different sheets of the output, without needing to engage in complex Excel formulae or running much code. This is useful when your requirements are more complex than have been accounted for in the default output data.

Follow the steps below to set up and run the column merge app on Mac, Windows, or Linux (steps 1–6 are shared with the Processor, as below).

## 1. Clone the Repository

Clone the repository to your local machine using git, or download the repository directly.

## 2. Open a Terminal or Command Prompt

Navigate to the `tabular_data` directory in your terminal (Mac/Linux) or Command Prompt/PowerShell (Windows), or open a new Terminal/Command Prompt window at that directory.

## 3. Check Python and pip Installation

In the Terminal or Command Prompt, run the following commands to make sure that Python 3 and pip are installed:

Mac/Linux:

	python3 --version
 
	pip3 --version

Windows:

	python --version
 
	pip --version

If Python is not installed, download Python from https://www.python.org/downloads/

## 4. Create a Virtual Environment

Run the following commands to create a virtual environment:

Mac/Linux:

	python3 -m venv .venv

Windows:

	python -m venv .venv

## 5. Activate the Virtual Environment

Mac/Linux:

	source .venv/bin/activate

Windows (Command Prompt):

	.venv\Scripts\activate.bat

Windows (PowerShell):

	.venv\Scripts\Activate.ps1

## 6. Install Dependencies

Once the virtual environment is active, install the required Python packages:

 pip install -r requirements.txt

## 7. Run the Web Application

Start the web server with:

  python column_merge.py
  
You should see the following output:

	Starting server at http://127.0.0.1:5000/
 
	Press CTRL+C to quit.

## 8. Access the App

To access and use the app, open your web browser and go to:

  http://127.0.0.1:5000/

## 9. Use the App

Follow the instructions on each page to perform the merge and download the resulting file. For worked examples, see below.

## 10. Stop the Server

To stop the app, return to the terminal and press:

    Control + C
