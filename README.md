# trgn_assignment3b

# extract_phonenum.py

## Usage

- `python3 extract_phonenum.py mytextfile.txt`

## Description

Extracts every phone numbers from a text file and print them as a list. Use regex `re.findall(r'\(?0\d{2,3}[)-]?\d{7,8}')`. 

- #(? represents it could find phonenumber with or without Parenthese "(".
- #0\d{2,3} represents Region number 0XX one to two times.
- #[)-? represents it could or could not follow ")"," ","-" after Region number.
- #\d{7,8} represents 7 or 8 digit number.

It could find phone number in format (0XX) 7 or 8 digit number,0XX- 7 or 8 digit number and 0XX 7 or 8 digit number.

## Known issues

None

# ensg2hugo.py

## Usage

python3 ensg2hugo.py [-f][0-9] [file]

## Description

- Read the Homo_sapiens.GRCh37.75.gtf to create a dictionary.
- Convert the Ensembl name to HUGO names in input file.
- "-f[1-9]" means usc the No.n column , in this Unit test file , you should use -f2 to pick the second column.
- `git clone` the test file expres.anal.csv。

## Known Issues

If you want to do this conversion successfully, you should know the right column to use -f[n].

# Histogram.py

## Usage

`python3 histogram.py [-f][0-9] [file]`

## Description

- Creates a histogram as a png from a csv file using the specified column in a tab delimited file.
- "-f[n] means you should the nth column to draw this histogram.
- The test file is "addresses.csv" and the histogram obtained is "histogram.png"

## Know Issues

none
