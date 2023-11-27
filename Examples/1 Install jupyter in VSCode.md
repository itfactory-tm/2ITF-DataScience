# Setup your IDE

In this tutorial we'll guide you through installing your development environment with Python Jupyter notebooks. 

## Step 1: Python and VSCode

Install Python and Visual Studio Code. Use the following links:

- [Python](https://www.python.org/downloads/)
- [Visual Studio Code](https://code.visualstudio.com/download)

## Step 2: Create a virtual environment

- Open a folder in VSCode. Make sure it's the folder where you'll be keeping all your notebooks. You can make subfolders in this folder later on.
- Open a terminal in VSCode.
- Run the following command:

```Shell
python -m venv venv
./venv/Scripts/activate
```

Your prompt will have changed to "(venv) PS c:\...". This means you're in the virtual environment. Test it by running a Python-script.

- Create "hello_world.py" containing a Python print-statement.
- Run the file. (This should print whatever it was you printed.)

## Step 3: 

From now on we're basically following [this](https://code.visualstudio.com/docs/datascience/jupyter-notebooks).

- Install the Jupyter package using the following command (in the prompt that is preceded by "(venv)"):

```Shell
pip install jupyter
```

- When installed, create a new Jupyter notebook.
    - Ctrl-Shift-P and select "Jupyter: Create new Jupyter notebook"
    - Create a file with the ".ipynb" extension
    - Add the following blocks:

```Python
# code block:
print("Hello")
a = 17

# text block:
# some text

# code block:
print(a)
```
Running would lead to the following:

![](2022-02-15-16-17-05.png)

Congratulations, you can now create and run Jupyter notebooks on your system. Work through the rest of the [Microsoft document](https://code.visualstudio.com/docs/datascience/jupyter-notebooks) to see how you can debug in Jupyter notebooks.