
# CONCERTS DATABASE


  ## Project Overview

This application is a Concerts Database System. It allows users to manage concerts, bands, and venues through a set of functions that inserts and manages concert data. The application does operations such as retrieving concert details, adding bands and venues, and tracking performances at specific venues on certain dates.

### Features

1. Adds and manages information about bands including their name and hometown.
2. Adds and manages information about venues including their name and location.
3.  Adds and manages venue information such as name and city.
4. Adds and manages concert information including the date, venue, and band.
5. Retrieves concert details by date, venue, or band.
6. Tracks performances at specific venues on certain dates.
7. Schedules concerts by associating bands with venues and dates.
8. Retrieves concerts for a specific band or venue.
9. Gets details of bands performing at specific venues.
10. Checks if a concert is taking place in the band's hometown.
11. Tracks which band has performed the most concerts.
12. Identifies the most frequent band at a particular venue.

## Technologies Used
*Python*

*SQLite*

*Tables*

- The application consists of the following tables:

1. Bands:
id (Primary Key)
name (String)
hometown (String)

2. Venues:
id (Primary Key)
title (String)
city (String)

3. Concerts:
-id (Primary Key)

band_id (Foreign Key from bands)

venue_id (Foreign Key from venues)

date (String representing the concert date)

## Prerequisites

You will need the following installed to run this project:

* Python 3.x

* SQLite3 or PostgreSQL

* sqlite3 library (built into Python) or psycopg2 for - - PostgreSQL

* A text editor capable of running Python such as Visual Studio Code.

## Installation

#### Alternative One

* To use this repo, follow these steps:

* Open the terminal/CLI on your computer.

* Clone this repository by running the following command:

 * git clone  git@github.com:Junnita/Phase-3-Code-Challenge-3.git
Change directory to the repo folder:

 * cd Phase-3-Code-Challenge-3

* Open it in your Text Editor by running the command:

 * code .

#### Alternative Two

* On the top right corner of this page there is a button labelled Fork.

* Click on Fork to create a copy of the repository to your github account.

 ###### Follow the process described in Alternative One above.

* Set up the database

* Using SQLite

* Creates the SQLite database and tables by running the provided migration script:

 * python concerts_database.py

 * This script will create the bands, venues, and concerts tables in an SQLite database named concerts_database.db.

# Author

* JUNNE WANJA 
