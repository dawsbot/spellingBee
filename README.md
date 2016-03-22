# spellingBee

> :honeybee: :heavy_plus_sign: :octocat: correct spelling in readme files

<br>

## Install
```shell
  git clone https://github.com/dawsonbotsford/spellingBee.git
  cd spellingBee
  pip install -r requirements.txt
```

<br>

After installing, you need to set your environment variables for Github login information:

```shell
export GH_USERNAME='<your username here>'
export GH_PASSWORD='<your password here>'
```

For persistence across terminal sessions, consider adding both export statements to your `~/.bashrc`, `~/.zshrc`, etc.
You will need to `source ~/.bashrc`, or similar `rc` file in order to reload these export statements the first time you configure the environment variables.

<br>

## Usage

```shell
cd spellingBee
./main.py <username> <repo name>
```

In the case where a spelling correction can be found, a fork and pull request from the authorized account will be triggered upon execution of `./main.py`.

<br>

#### Train the spelling even further

The spellingBee is packaged with an optional `-t` training flag in order to allow you to find and train mispelled words.

```shell
cd spellingBee
./main.py <username> <repo name> -t
```

<br>

#### Full example
If I wanted to correct spelling on `dawsonbotsford`'s `inf` repo, I would run the command:

```shell
./main.py dawsonbotsford inf
```

<br>

## About

The **spellingBee** is your new favorite tool to provide **bangin' spell corrections for your GitHub READMEs**. Upon finding a mapped correction in  ```words/words.txt```, the **Spelling Bee** pull requests your repo with the spelling errors corrected!

If the corrections suck, let the **Spelling Bee** know by posting an issue [here](https://github.com/dawsonbotsford/spellingBee/issues), and if it reveals a spelling error useful to you, merge that shit! And then star the repo, it goes a long way to help me see my efforts are useful.

```words/words.txt``` is where all of the corrections are mapped. Feel free to pull request improvements to this file if you have a good mapping to add.

Credit to [holdenk](https://github.com/holdenk) for the origin implementation in Perl available [here](https://github.com/holdenk/holdensmagicalunicorn)

<br>

## License

MIT © [Dawson Botsford](http://dawsonbotsford.com)
