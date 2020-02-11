# shopping-cart project

[Project Description](https://github.com/prof-rossetti/intro-to-python/blob/master/projects/shopping-cart/README.md)

## Installation

Clone or download from [GitHub Source](https://github.com/kristyyip/shopping-cart) onto your computer, choosing a familiar download location like the Desktop. 

Then navigate into the project repository from the command-line:

```sh
cd ~/Desktop/shopping-cart
```

## Setup

Create and activate a new Anaconda virtual environment from the command-line:

```sh
conda create -n shopping-env python=3.7 # (first time only)
conda activate shopping-env
```

From inside the virtual environment, install package dependencies:

```sh
pip install python-dotenv
pip install sendgrid==6.0.5
```

## Usage

Run the program:

```sh
python shopping_cart.py
```