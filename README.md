# url-to-mobi-kindle

This python script uses https://ebook.online-convert.com/convert-to-mobi/ to convert a webpage, PDF, etc. from URL to MOBI. The script is made to be Python 2.7 compatible and only uses built-in libraries that come with Kindle python so it can be directly run on a Kindle using a terminal emulator.

## Pre-requisites

- A [jailbroken](https://wiki.mobileread.com/wiki/5_x_Jailbreak) Kindle (do your research first!).
- [KUAL](https://www.mobileread.com/forums/showthread.php?t=203326) installed on Kindle.
- [Python 2.7](https://wiki.mobileread.com/wiki/Python_on_Kindle#Stage_1_-_Install_Python) installed on Kindle.
- [kterm](https://github.com/bfabiszewski/kterm) or any other terminal emulator installed on your Kindle.

## Usage

We need to first download the code on Kindle, open kterm on your kindle (or optionally [SSH to your kindle](https://www.mobileread.com/forums/showthread.php?t=204942)) and run:

### Push to Kindle (via https://pushtokindle.fivefilters.org/)
```
[kterm]# cd /mnt/us/
[us]# curl https://raw.githubusercontent.com/ritiek/url-to-kindle/master/pushtokindle.py -o pushtokindle.py
```

Modify the values for `TO` and `FROM` in `pushtokindle.py` to mimic your approved Kindle personal documents e-mail.

Now for example, to download https://www.joelonsoftware.com/2005/12/29/the-perils-of-javaschools-2/ to your Kindle
via PushToKindle service:
```
[us]# python pushtokindle.py https://www.joelonsoftware.com/2005/12/29/the-perils-of-javaschools-2/
```
The webpage should appear as a document on your Kindle homescreen shortly after running the command.

This script will push the document to your Kindle device irrespective of the device the script is run on.

### URL to MOBI (via https://ebook.online-convert.com/)
```
[kterm]# cd /mnt/us/
[us]# curl https://raw.githubusercontent.com/ritiek/url-to-kindle/master/urltomobi.py -o urltomobi.py
[us]# python urltomobi.py -h
usage: urltomobi.py [-h] -f FILENAME [-t TITLE] [-a AUTHOR] URL

Convert a webpage from URL to MOBI via ebook.online-convert.com, designed for
(jailbroken) Kindles

positional arguments:
  URL                   webpage url to download as MOBI

optional arguments:
  -h, --help            show this help message and exit
  -f FILENAME, --filename FILENAME
                        download MOBI to this path (default: None)
  -t TITLE, --title TITLE
                        set title of the book (default: )
  -a AUTHOR, --author AUTHOR
                        set author of the book (default: )
```

For example, to download https://medium.com/@abhishekj/an-intro-to-git-and-github-1a0e2c7e3a2f as MOBI, run:
```
[us]# python urltomobi.py -f /mnt/us/documents/learn_git.mobi https://medium.com/@abhishekj/an-intro-to-git-and-github-1a0e2c7e3a2f
Create Job:
{"id":"541f4fd5-eb99-43ca-80f3-d74f96d878f9","token":"149adda449dec8b0ebdee8d81020fb61","upload_url":"https:\/\/www38.online-convert.com\/dl\/web2\/upload-file\/541f4fd5-eb99-43ca-80f3-d74f96d878f9","server":"https:\/\/www38.online-convert.com\/dl\/web2","conversion":[{"id":"eaa14601-a801-49b8-ba56-2d84ab88b909","target":"mobi","category":"ebook","options":{"reader":null,"download_password":null,"allow_multiple_outputs":false,"preset":null,"title":null,"author":null,"border":null,"encoding":null,"ascii":false,"enable_heuristics":false,"base_font_size":null},"metadata":[],"output_target":[]}]}

Add Job:
{"id":"f9107488-1a06-415d-a565-c2d903bbd1ca","type":"remote","source":"https:\/\/medium.com\/@abhishekj\/an-intro-to-git-and-github-1a0e2c7e3a2f","filename":"","size":0,"hash":"","checksum":"","content_type":"","created_at":"2018-11-16T10:54:57","modified_at":"2018-11-16T10:54:57","parameters":[],"metadata":[]}

Starting Job..

Server status: downloading
Server status: downloading
Server status: downloading
Server status: downloading
Server status: processing
Server status: processing
Server status: processing
Server status: processing
Server status: completed

Fetching download link:
https://www.online-convert.com/downloadFile/541f4fd5-eb99-43ca-80f3-d74f96d878f9/4ed76d5b-afef-4c62-b37c-e3225491d71f

Saving as /mnt/us/documents/learn_git.mobi ...
```

The downloaded book should appear on your homescreen. This is how it looks on my Kindle Paperwhite 3:

<img src="https://i.imgur.com/GHMf2lQ.png" width="310"><img src="https://i.imgur.com/qiI9G2X.png" width="310">
