# The Ultimate Keyboard Genetic Algorithm

This repository contains the code to simulate a genetic algorithm that finds an optimal keyboard based on a purely distance metric. It allows the user to configure the size of populations as well as the number of generations. The default text that it tests the keyboards with can also be manipulated. In addition, these keyboards can also use different typing styles to get various versions of a keyboard for similar sample data.

#### Table of Contents

1. [ Install ](#install)
2. [ Introduction ](#introduction)
3. [ Usage ](#usage)
4. [ Conclusion ](#conclusion)
5. [ License ](#license)

## Install

First, clone the repository onto your computer with the following command: 

```bash
git clone https://codeberg.org/Inventor853/ultimate-keyboard.git --depth 1
```

After cloning the repository, you will want to change directories to complete the install.

```bash
cd ultimate-keyboard
```

Now create a virtual environment for your working directory.

If not done so already, install `venv` with the package manager [ pip ](https://pypi.org/project/pip/).

```bash
pip install virtualenv
```

Use `venv` to create a virtual environment in the folder `venv`.

```bash
python -m venv venv
```

Source into your virtual environment with the following command; it may be different for different shells.

```bash
source venv/bin/activate
```

Use the package manager `pip` to install the required libraries.

```bash
pip install -r requirements.txt
```

## Introduction

Before experimenting with the genetic algorithm, you can build the presentation for a brief overview on the program's functionality. To complete the following steps, you must first insure that [LaTeX](https://www.latex-project.org/) is installed on your computer. Also confirm that you have [latexmk](https://mg.readthedocs.io/latexmk.html) installed to make the presentation.

```bash
cd presentation/
latexmk -xelatex presentation.tex 
latexmk -c
```

## Usage

To run the genetic algorithm simply use the following command:

```bash
python main.py
```

For more information on how to configure the genetic algorithm use this command:

```bash
python main.py --help
```

Once the code has run it will print the name of the json file that contains all of the data from the run. This file will be stored under the `outputs/` folder. These files can be visualized later with the following command:

```bash
python display.py <file-name> <display-mode>
```

In this command, `<file-name>` should be replaced with the relative path to the json file from the main repository directory. Additionally, `<display-mode>` should be replaced with a `0` for showing only the final results of the program or a `1` to show each generation of the program iteratively. 

## Conclusion

This program illustrates the ability of a genetic algorithm to tackle a seamingly complex topic into a generic stochastic approximation method. By defining a fitness test and a representation of a population, as well as the generation of a new generation with mutations, a genetic algorithm can search almost any defined set. In this case, the algorithm was simply a quicker way to search the set of all possible keyboards. This makes genetic algorithms a highly versatile tool for many topics. However, the main problem with them is that such approximation models are very highly based on chance. Since everything is random, one never knows when to stop the model, as a new mutation could trigger an advancement randomly. 

## License
This project uses a GNU General Public License v3. For more information, please look at the LICENSE file in this repository.

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

___

![Neovim](https://img.shields.io/badge/NeoVim-%2357A143.svg?&style=for-the-badge&logo=neovim&logoColor=white)
![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![JSON](https://img.shields.io/badge/json-5E5C5C?style=for-the-badge&logo=json&logoColor=white)
![Notion](https://img.shields.io/badge/Notion-000000?style=for-the-badge&logo=notion&logoColor=white)
[![Arch](https://img.shields.io/badge/Arch%20Linux-1793D1?logo=arch-linux&logoColor=fff&style=for-the-badge)](https://www.youtube.com/watch?v=dQw4w9WgXcQ)
