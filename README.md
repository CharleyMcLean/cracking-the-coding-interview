# Fun with Random.org

Random.org is a web front-end to an atmospheric noise sensor, which can give us pretty good random numbers. It's the reverse from a noise cancelling filter, since it cancels everything BUT the noise. Weather conditions, solar flares, a full-moon can have little impact on this, since it focuses on getting the purest white noise possible from their hardware sensors. 

Completed:  Use the HTTP API for [random.org](https://www.random.org/clients/http/) to get truly random numbers. Look out for the guidelines, or you may get banned!

Future tasks:  Using these random numbers create the following:

- An RGB bitmap picture of 128x128 pixels

- A white noise WAV sound sample of 3 seconds

- An RSA key pair

## <a name="technologies"></a>Technologies
Tech Stack: Python<br/>
APIs: Random.org<br/>

## <a name="features"></a>Features

Generate a list of random numbers using Random.org API.
<!-- ![](https://github.com/CharleyMcLean/Believe/blob/master/static/img/screenshot-landing-page.png?raw=true) -->


## <a name="install"></a>Installation

To run the random number generator:

Clone or fork this repo:

```
https://github.com/CharleyMcLean/random-number-generator.git
```

Create and activate a virtual environment inside your Believe directory:

```
virtualenv env
source env/bin/activate
```

Install the dependencies:

```
pip install -r requirements.txt
```

Run the app:

```
python -i random.py
```
