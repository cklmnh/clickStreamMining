
---++ Dataset full description (README)

Dataset: ydata-ymessenger-user-communication-pattern-v1_0

Yahoo! Messenger user communication pattern over a month, involving a small subset of our total unique user population - version 1.0


=====================================================================
This dataset is provided as part of the Yahoo! Research Alliance
Webscope program, to be used for approved non-commercial research
purposes by recipients who have signed a Data Sharing Agreement with
Yahoo!. This dataset is not to be redistributed. No personally
identifying information is available in this dataset. More information
about the Yahoo! Research Alliance Webscope program is available at
http://research.yahoo.com
=====================================================================

Full description:

This dataset contains 28 text files (each file is separately gzipped):

ydata-ymessenger-user-communication-pattern-v1_0-d00.txt
ydata-ymessenger-user-communication-pattern-v1_0-d01.txt
...
ydata-ymessenger-user-communication-pattern-v1_0-d27.txt

each based on data generated by a small subset of Yahoo! Messenger users from 
different zip codes for 28 days starting from April 1st 2008, with some 
modifications and additions by Yahoo! Research. All user ids, zip codes, and
dates are anonymized. Fields in each data file are delimited with a single 
white space ("\b") character.

The content of each file is as follows:

=====================================================================
    "ydata-ymessenger-user-communication-pattern-v1_0-d**.txt" contains a small
    sample of Yahoo! Messenger users' first communication in a day, with the 
    following fields:

    DXX � anon date (report days will be D00, D01, � D27)
    MON � day of week (e.g., Monday)
    UXXXXX � anon yid
    ZXXXX � anon zip
    [-ny] � whether or not the recipient of the IM has the sender on his buddy list

    The training data contains 100,000 unique users (|U|) from 5649 unique zip codes (|Z|). 
    Each line in each file records the "first communication in day from unique locale" event 
    which signifies the first time any of the users in |U| (sender) sends an IM to any other 
    user in |U| (receiver) from a fresh zip code in |Z| (sender's locale). So if the sender 
    sends another IM in the day to the same receiver from the same sender zip code, this does 
    not get recorded. But for the same sender, if either the receiver, or the sender's zip code 
    changes (but are still within |U| and |Z| respectively), then that creates a new entry in 
    the daily log. Please note that no actual IM content gets recorded. Apart from this, for 
    each entry we also indicate (if known) a one-way buddy relationship between the sender and 
    receiver (whether sender is on receiver's buddy list).
 
Snippet:

D00-MON 00:00:00 U06579 Z3403 U80049 -
D00-MON 00:00:12 U04698 Z1459 U38053 y
D00-MON 00:00:16 U01214 Z1049 U77128 y
D00-MON 00:00:18 U15738 Z1372 U02534 y
D00-MON 00:00:19 U00478 Z2804 U50756 y
D00-MON 00:00:40 U45627 Z3584 U61546 y
D00-MON 00:00:58 U06579 Z3403 U89243 -
D00-MON 00:01:04 U27535 Z1097 U15587 y
D00-MON 00:01:19 U22087 Z0271 U03291 y
D00-MON 00:01:40 U15738 Z1372 U16576 y

=====================================================================
