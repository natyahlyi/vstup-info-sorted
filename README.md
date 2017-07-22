# `vstup.info` rating sorter by priority


## Requirements
Python 3.*

Python packages:
* `Click` 
* `beautifulsoup4` 

```
$ pip install -r requirements.txt
```

## Usage

```
$ python process.py --url <url of vstup info rating>
```

Will output `output.csv` file in current directory containing real rating position in the first column and other data from vstup.info in next columns:
* ``` 
    №,#,ПІБ,П,Σ,Д
    1,12,Ясінський Н. Р.,1,195.536,—
    2,40,Зьола О. П.,1,192.254,—
    3,52,Українець Н. В.,—,191.395,—
    4,62,Серівка М. В.,1,191.042,—
    5,88,Сало А. С.,1,188.921,—
    6,93,Берко Я. І.,1,188.466,—
    7,108,Коростенський Р. О.,1,187.658,—
  ```
You can open `.csv` file with (any text editor or Spread sheet redactor like MS Exel)
