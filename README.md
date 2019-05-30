Simple spider for crawling products from the MrBricolage website.
Data collected is: product name, price, image url and characteristics.

SUGGESTION:
It is better to run this script into a virtualenv. 
the requirements.txt file includes all the necessery additional packages
needed for this project to run properly.


HOW TO RUN:
1. Open terminal.
2. Navigate to the folder where this project is downloaded.
3. Make sure that your exact location is where scrapy.cfg file is.
4. Enter the following command: scrapy crawl mr_bricolage -o data.json
5. After the process is finished, you can find the stored data in the
data.json file.
