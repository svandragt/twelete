# Twelete
Delete your tweets older than 4 weeks. Tweets are temporary messages, and thus should be deleted.


## Setup

1. Install using poetry: `poetry install`
2. Create a `.env` file with the following contents. Fill in the values after [creating a Twitter App](https://developer.twitter.com/en/apps):
```
twelete_consumer_key=""
twelete_consumer_secret=""
twelete_access_key=""
twelete_access_secret=""
```
3. Run `poetry run python ./twelete.py`. It will dry-run, displaying deletable tweets over 28 days old.
4. Add the following items to the `.env` file to tweak the cutoff date and to enable deletion:
```
twelete_days_to_keep=28
twelete_dry_run=0
```
