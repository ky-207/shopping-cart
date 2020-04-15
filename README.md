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

### SendGrid / Email Capabilities
Additionally, take a moment to [create an API Key](https://app.sendgrid.com/settings/api_keys) with "full access permissions on SendGrid. You may need to sign up for an account if you haven't done so already.

After obtaining an API Key, update the contents of the ".env" file to specify your real API Key in an environment variable:

    SENDGRID_API="abc123"

You will also need to update the contents of the ".env" file to specify your email address that is associated with your SendGrid account in an enviornment variable:
    
    MY_EMAIL="abc123@gmail.com"

## Usage

Run the program:

```sh
python shopping_cart.py
```

## Testing

Install the `pytest` package, perhaps within a virtual environment:

```sh
pip install pytest
```

Run tests:

```py
pytest