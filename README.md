# memorable-password-generator
My attempt at re creating Apple's "generate memorable password" from the Keychain app.
This is a personal project I developed for fun, and you're welcome to use the code as you see fit under the MIT license. I received a lot of valuable external help during its creation, so feel free to make the most of it!

Since I don't really have any reference for how Apple's version worked and only had one generated password before the feature was taken away, I decided to just follow the rules that I could remember, which was a 13 letter word, followed by a 6 digit number, a special character, and an eight letter word with a capital letter. All while making those memorable words and numbers. It may not be the most secure way, but sometimes when generating passwords/passphrases you need something that can focus on memorability as well as security.
Due to limited references on Apple's previous feature and having generated only one password before the feature was discontinued, I tailored my memorable password generator based on the rules I remember. The format I adopted includes a 13-letter word, followed by a 6-digit number, a special character, and an eight-letter word that begins with a capital letter. This approach ensures that while the passwords are secure, they are also easy to remember. This principle guides the design of my password generator, making it both practical and effective for everyday use.

## Running the project
```./setup_and_run.sh```

## Stop the app
```^C```

Here is the source for [5000-more-common.txt](https://github.com/MichaelWehar/Public-Domain-Word-Lists/tree/master).