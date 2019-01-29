# Illumina Software Developer Apprentice Test

This git repository contains a test for applicants to the Illumina apprenticeship program, focussed on problem solving for computing-based technical roles. 

## Instructions

- The actual task is outlined below
- You can use any tools you have on your computer and anything you can find on the internet to help you - this is how you would be working in real life, so this is how you can work in the test!
- Please return your answer within 2 days (48 hours) of receiving the test. Within that limit, you can spend as long as you like on the test but we would expect you to spend around half an hour. 
- You answer should be sent to the person who Emailed you the test. Include the following:
  - The answer to the task
  - A set of instructions for how you completed the task, so another person attempting the test would know exactly what to do
  - Any code you end up writing can be included as a file attachment in the Email
  - How long it took you to complete the test

## Task

This git repository contains a Python script. To complete the task, you need to provide the output from the script.

## General information about the task

The most obvious way to complete this task is to download the Python script contained within this git repository and execute it. It should produce a single line of output which is the "answer" to this test. An alternative is to try to figure out what the script does and then reproduce the output in another way - this is a less satisfying solution, but is still not "cheating" :)

This task involves interacting with a number of computing technologies including git, Python and the operating system on the computer you are using. Understanding and using technologies like these together is a core skill for a programmer or bioinformatician. You may not have come across all these technologies before or know in detail how to use them - figuring out these new technologies, even if you've never seen them before, is also a core skill for a programmer or bioinformatician. If there are technologies you don't understand, where do you think you might find information on how to get these working?


## Hints

These hints apply if you're attempting the "obvious" solution - to download and run the script.

- You will need to download the script from the git repository. There are a number of ways to do this, including downloading and unpacking a zip archive, using a git installation on your computer or even downloading just the file.

- You will also need a working Python installation on the computer you're using. Does one exist already? If not, you should be able to download and install one.

- How do you run the script in the test with your Python install? Can you find some instructions online about how to do this? 

---

## Extensions (for extra credit)

If you manage to complete the main task in the allocated time, you can move on to this section which provides a number of extensions to improve the script found in this git repository. You can attempt as many of the extensions as you wish in any order.

### Extension 1: configurable input string

The script has a hard-coded string that it uses as input. Rewrite the script to take a string from the user instead. You can do this using a command line argument ([sys.argv](https://www.pythonforbeginners.com/system/python-sys-argv)), or via a library like [argparse](https://docs.python.org/3/howto/argparse.html) or you can use the Python [raw_input()](https://www.cyberciti.biz/faq/python-raw_input-examples/) function.

- Hint: if you want to combine this extension with the others, better to use the argparse module, which will make it easier to add more options later.

### Extension 2: configurable encoding 

The script only supports one type of encoding for the input string - base64. However, the [underlying Python module](https://docs.python.org/3.7/library/base64.html) supports a number of other encodings, including base16 and base32. Rewrite the script to take a command-line argument `--encoding` which can be one of `base16`, `base32` and `base64`. Then encode and output the string using the chosen encoding.

### Extension 3: optional file output

The script currently prints the result of the encoding to the console. However, it might be useful to allow an (optional) output to a file. Add a command-line argument `--output-file` that allows the user to specify an output file. Then write the result of this encoding into this file instead of the console. Perhaps also provide a friendly error message should it be impossible to create this file.
