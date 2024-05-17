# Cinemalytics - Create your own movie database

## About Cinemalytics
During lockdown I became quite obsessed with watching new films, with the sheer number of films I was watching I got curious...

- _Which actor had I seen the most?_
- _How many films have I seen this month?_
- _Have I ever seen a film released in 1980?_

Here came the idea for Cinemalytics, a place where you can keep a list of films you watch that stores every detail of each film. 
So you can get intricate data on your watching habbits.

## Requirements
Due to updates to the cinemagoer package, this must be run on python verison 3.10

You need to install these packages from the command prompt to run the code:
```
pip install cinemagoer matplotlib numpy
```
## How does it work?
Using the [**Cinemagoer** (formerly IMDBpy)](https://cinemagoer.readthedocs.io/en/latest/) Python module, Cinemalytics can fetch all relevant data on films. 
Such as:
- Cast
- Composer(s)
- Director(s)
- Release Year
- Genre(s)
- Runtimes
- IMDb rating

On top of this, more data is recorded on film entry like:
- Personal film ranking
- Date of entry
- Number of times watched 

All this data is stored in a datafile: 2020Vision.txt

## How to use
This program is based in the command-line, you will be prompted with menu options.
![Menu](https://github.com/RohanBilly/Cinemalytics/assets/92380601/be4f8417-2ec2-49d9-897e-1eca79d92ee9)

# Chronilogical and ranked list
As you add films, you'll build two lists:
![lists](https://github.com/RohanBilly/Cinemalytics/assets/92380601/bd38b01a-dfcd-47de-96f7-32e93ac18ce5)
- Your chronilogical list of films (sorted by the dates of entry)
- Your ranked list (sorted by your personal preference)

# Actors and Directors
The actors and directors of every film you watch are saved. So you can see your most frequent actors and directors.
![actor dir](https://github.com/RohanBilly/Cinemalytics/assets/92380601/eb8a478b-77cd-4949-8c99-e3e93890e1e2)

# Graphs
Some data such as entry dates can be graphed to show your watching habbits over time.
![graph](https://github.com/RohanBilly/Cinemalytics/assets/92380601/d4732f99-e366-4f30-8788-204754bf664f)


## It's down to you!
I've uploaded my data file if you want to explore the program with a filled database (2020Vision.txt). I'd recomend deleting this file when you understand how it works to start building your own database.

There are so many cool things you can discover, I'll let you explore and find them yourself.


If you have any issues, reach me at <strong>rohanvansanden@live.co.uk</strong> 







