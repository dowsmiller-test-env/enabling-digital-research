layout: page
title: "5. Using the Processor"
permalink: /5_processor_setup

# 5. Using the Processor (Intermediate)

If you want to run the processor on your own machine, either over the MMOL data or on another dataset, follow the steps below (steps 1 and 4–8 are shared with the Column Merge app, as above). These instructions can also be found in the `processor_setup_instructions.txt` file in the `tabular_data` directory.

## 1. Clone the Repository

Clone the repository to your local machine using git, or download the repository directly.

## 2. Update the Source Files (if required)

If you wish to run the processor over a subset of the MMOL data, or over any other dataset, you will need to change the data contained within the repository. Any .xml file found in the collection directory or its sub-directories will be treated as a file containing data about an individual manuscript unit. Any .xml file found in the root directory of the repository will be treated as authority files, and will be assumed to contain information on entities named in the collection files, linked using UIDs.

## 3. Modify the `_global_config.py` and Config Files (if required)

See the next section or the `read_me.txt` file in the `config` directory for further details.

## 4. Open a Terminal or Command Prompt

Navigate to the `tabular_data` directory in your terminal (Mac/Linux) or Command Prompt/PowerShell (Windows), or open a new Terminal/Command Prompt window at that directory.

## 5. Check Python and pip Installation

In the Terminal or Command Prompt, run the following commands to make sure that Python 3 and pip are installed:

Mac/Linux:

	python3 --version

    pip3 --version

Windows:

    python --version

    pip --version

If Python is not installed, download Python from https://www.python.org/downloads/

## 6. Create a Virtual Environment

Run the following commands to create a virtual environment:

Mac/Linux:

    python3 -m venv .venv

Windows:

    python -m venv .venv

## 7. Activate the Virtual Environment

Mac/Linux:

    source .venv/bin/activate

Windows (Command Prompt):

    .venv\Scripts\activate.bat

Windows (PowerShell):

    .venv\Scripts\Activate.ps1

## 8. Install Dependencies

Once the virtual environment is active, install the required Python packages:

    pip install -r requirements.txt

## 9. Run the Processor Script

Run the main script to process the data:

    python processor.py

## 10. Output

After processing is complete, the results will be saved in the `output` folder.
