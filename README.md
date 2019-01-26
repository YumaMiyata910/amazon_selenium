# Amazon Selenium

## 事前準備

### seleniumのインストール
---
pipでseleniumをインストール
```bash
$ pip3 install selenium
```

### ChromeDriverのインストール
---
今回はver2.45のバイナリをダウンロード。　　

[ChromeDriver](https://chromedriver.storage.googleapis.com/index.html?path=2.45/)  

各々のOSにあったzipファイルを解凍後、  
PATHを通す or 通っているディレクトリへ配置。
```bash
# /usr/local/binにPATHが通っていたため、その配下に配置
$ mv {chromedriverのあるパス}/chromedriver /usr/local/bin/

# PATHが通っているか確認
$ chromedriver
```

### sampleで動作確認
---
```bash
$ python3 selenium_sample.py
```