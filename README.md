# About The Project
The progam is used to prepare tidal data for input into [Pythagoras](http://www.cetaecoresearch.com/research-software-pythagoras.html), a theodolite tradking software used for Cetacean Monitoring.

Tidal data can be found on Hong Kong Observatory website. It is usually formatted in http://www.hko.gov.hk/tide/cCLKtext2019.html 

# Get Started
You should have python installed. [Installation guide](https://www.anaconda.com/download/) and [Run Pyton in Anaconda Prompt](https://medium.com/@tranngocminhcdn/running-python-scripts-by-using-anaconda-prompt-da2870d86fd0)

Assumed Chrome is used.
1. Download the program and unzip to local directory
2. Go to the tidal data website
3. Right click on the data and click inspect
4. You will see all the data in the "Fency" toolbox
5. Copy and save it as data.txt in the same directory of the program
6. Change the year and file name in the scrapAndParse.py
7. Run it

# What the Progam Does?
The data in the website is concated along the columns. We want to concat the data along the rows.

After we do this, we just sort and output a csv

# Excel Template
If you really don't like program, I have also prepare an excel template which does the same things.

# Discovery
* Just found that [Data.gov.hk pubish](https://data.gov.hk/en-datasets/search/tidal) predict tide
