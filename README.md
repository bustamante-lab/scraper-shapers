# Scraper-shapers
Various scripts designed to intake and re-shape information from databases, websites, etc. (E.g. Processing PubMed bulk downloads)

# convert_medline.py

Command line: > python convert_medline.py [PubMed download file name]

Function: Reads in a file with bulk downloads from PubMed in MEDLINE format, produces a second file in working directory ('review_papers.txt'), a tab-delineated file with all article information, plus abstract.

Utility: When conducting a systematic review, one needs to screen a large number of abstracts. This script was developed to create an Excel-compatible file of PubMed bulk-downloaded citations and abstracts for swift and convenient review.
