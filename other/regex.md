
## Repetitions
#### `\w{1,4}\d{4,}`
- valid:<br> 
_**Hk13214354654654**_<br> 
_**Hack1021**_

## Grouping and Capturing
#### `\bcat\b`
assert position at a word boundary.
- valid: A _**cat**_
- invalid: Acat

#### `Ab*s`
zero or more
- valid:<br>
_**Abbbbs**_<br>
_**As**_

#### `Ab+s`
one or more
- valid: _**Abbbbs**_
- invalid: As

#### `It is (not)? your fault`
Parenthesis ( ) around a regular expression can group that part of regex together.
- valid:<br>
_**It is not your fault**_<br>
_**It is your fault**_

### `(and|AND|And)`
- valid:<br>
_**And**_ the award goes to<br>
A _**and**_ D Company

## Backreferences
#### `(\w)abc\1`
- valid: _**zabcz**_

#### `^\d{2}(\d{4}|-\d{2}-\d{2}-)\d{2}$`
- valid:<br>
_**12345678**_<br>
_**12-34-56-87**_
- invalid:<br>
1-234-56-78<br>
12-45-7810