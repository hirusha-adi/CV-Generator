# CV Website Generator

Generate a CV Website Easily

## Usage

If it's the first time, check if `data.json` is in the current working directory. If it does not exist, rename the `data.json.empty` file to `data.json`. use the command below if you are using linux/mac-os

```
mv data.json.empty data.json
```

Then, run the `maker.py` file to edit the data with a prompt or edit the `data.json` file manually. if you are using linux/mac-os, run the commands below

- Editing Data with Prompt

```
python3 maker.py
```

- Editing data manually (`data.json`)

```
nano data.json
```

- After you have filled `data.json` with the required data: You can start the web server
```
python3 cv.py
```

# Credits

<https://codepen.io/jlalovi/pen/NPeBqZ>
