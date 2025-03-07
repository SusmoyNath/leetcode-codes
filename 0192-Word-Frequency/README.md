Word Frequency Bash Script

Description

This repository contains a Bash script that calculates the frequency of each word in a given text file (words.txt). The output is sorted in descending order based on word frequency.

Assumptions

The input file words.txt contains only lowercase characters and space (' ') characters.

Each word consists of lowercase characters only.

Words are separated by one or more whitespace characters.

Each word's frequency count is unique, so no need to handle ties.

Example

Given the following content in words.txt:

the day is sunny the the
the sunny is is

The script should output:

the 4
is 3
sunny 2
day 1

Implementation

The script utilizes Unix pipes to achieve the desired result in a concise and efficient manner.

Usage

Run the following command in your terminal:

tr -s ' ' '\n' < words.txt | sort | uniq -c | sort -r | awk '{print $2, $1}'

Explanation

tr -s ' ' '\n' : Replaces spaces with newlines to separate words.

sort : Sorts the words alphabetically.

uniq -c : Counts the occurrences of each unique word.

sort -r : Sorts the output in descending order based on frequency.

awk '{print $2, $1}' : Formats the output to display word frequency.

License

This project is open-source and available for use under the MIT License.

Contributions

Feel free to fork this repository and submit pull requests with improvements or alternative implementations!

