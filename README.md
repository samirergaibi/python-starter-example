# Python - Get up to speed quickly

Long time since you coded in python? No problemo, here are some quick tips and reminders on how to start a project.

## How to pull and run this project

1. Clone the repo
2. Setup your virtual environment
3. Install the packages

The necessary information to follow these steps should be possible to deduce from this README.

## Virtual environment

It's a good idea to create a virtual environment so that your project is encapsulated from the global system scope.

There are two ways to do this as far as I know when writing this:

1. run the following terminal command in your project:

```bash
python3 -m venv <folder name>

# example
python3 -m venv .venv
```

This will create a folder with the necessary virtual environment stuff.

2. Create your project folder and open it then do the following in VSCode:

Open the command pallet in VSCode (⇧⌘P) and search for "Python: Create Environment" and then select Venv and then the interpreter you want to use.

## Installing packages

Great, now we have a virtual environment setup and we can install packages without polluting the global system scope.

To install a package let's run the following command:

```bash
python3 -m pip install <package name>
```

## FAQ

### Is the terminal not displaying the virtual environment?

Close and re-open the terminal and it should work.

### How do you handle package dependencies?

One way it to create a `requirements.txt` file that holds the packages and their versions. Look into the one that exists in this project for an example.

```bash
python3 -m pip install -r requirements.txt
```

### Is there an easier way to handle virtual environments and package dependencies?

There are third party solutions such as [Poetry](https://python-poetry.org/) that simplifies this problem.
