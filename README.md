# TimeCard

Entering time records is a pain. This script does it for me.


## Prerequisites

| dependency | version |
| ---        | ---     |
| Python3    | >=3.11  |
| pip        | >=23.0  |
| homebrew   | >=1.3.0 |

## Installation

This project uses STRTA to mange dependencies

```sh
script/bootstrap
```

## Usage

See env.sample for the environment variables you need to set.

```sh
bin/copy # copies the previous week
```

```sh
bin/submit m8t8w8r8f8 # submits the provided hours to the timecard for the current week
```

### Automate

Save yourself even more effort by loading the script on a cron job.

```sh
crontab -e
# set it up to run weekly at 10 am on Fridays
0 10 * * 7 /path/to/bin/copy
```
