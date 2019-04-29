# Bitly url shorterer

Shorten links via bit.ly and terminal.

Also, you can use it to count existing links.

## How to install

You have to get bitly GENERIC ACCESS TOKEN, [it may help](https://dev.bitly.com/get_started.html)

Create file .env in the root and write in it:

```
api_key=your key from bitly
```

Python3 must be already installed.

Should use virtual env for project isolation.

Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

## How to use

Run script in terminal
```
python shorten.py your_link
```

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).