# Twelete
Delete your tweets older than 4 weeks. Tweets are temporary messages, and thus should be deleted.


## Setup

1. Install using poetry: `poetry install`. (I created [PyShed](https://github.com/svandragt/pyshed) if you don't have poetry and python setup).
2. Create a `.env` file with the following contents. Fill in the values after [creating a Twitter App](https://developer.twitter.com/en/apps):
```
twelete_consumer_key=""
twelete_consumer_secret=""
twelete_access_key=""
twelete_access_secret=""
```
3. Run `poetry run python ./twelete.py`. It will dry-run, displaying deletable tweets over 28 days old.

> Dry run. To delete: add "twelete_dry_run=0" to .env<br>
> Authenticated as: svandragt<br>
> Deleting 1284072013640982529: [2020-07-17 10:26:39] Just gave a sprint demo where I had Michael Jordan and Scotty Pippen joined the site as senior editor and author re… https://t.co/SvrEK99eum

4. Add the following items to the `.env` file to tweak the cutoff date and to enable deletion:
```
twelete_days_to_keep=28
twelete_dry_run=0
```

# Run periodically.

Run `crontab -e` and add the following line:
```
# Run at 5:15am every day
15 5 * * * cd $HOME/src/twelete && $HOME/.poetry/bin/poetry run python ./twelete.py | tee -a /var/log/twelete.log
```

Make sure the log file exists and is writable:
```
sudo touch /var/log/twelete.log
sudo chown $(whoami):adm /var/log/twelete.log
```
