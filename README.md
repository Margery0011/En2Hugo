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


#ensg2hugo.py

## Usage

python3 ensg2hugo.py [-f][0-9] [file]

## Description

- Read the Homo_sapiens.GRCh37.75.gtf to create a dictionary.
- Convert the Ensembl name to HUGO names in input file.
- "-f[1-9]" means usc the No.n column , in this Unit test file , you should use -f2 to pick the second column.
- `git clone` the test file expres.anal.csv。

