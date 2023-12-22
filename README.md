# Import your DayOne journal to Obsidian daily notes

This is a quick script to import a DayOne journal to Obsidian.

Here is a quick run-book to get the data imported:

1. Export a journal to JSON in the DayOne app
1. Add it to this folder and call it `data.json`
1. Optional: Create a Python virtual environment for the dependencies: `python -m venv .venv`
1. Install dependencies: `pip install -r requirements.txt`

Now you are ready to import, and feel free to adjust the templates before starting the process.

The bundled templates create entries compatible with the [Obsidian Memos](https://github.com/Quorafind/Obsidian-Memos) plugin, which is a simple way of adding journal entries to your daily note.

A rendered entry could look like this:
```
## Journal
- 12:27 Day one entry title
        The contents here.

        Location: [Baden, Switzerland](geo:47.474361419677734,8.306922912597656)
```

The Memos plugin needs to have the full entry in a single bullet point, which is why the template contains `<br>` instead of newlines. If you just want the text and don't care about Memos, adjust this to get the raw text.

Once you are ready to start the import process, run:

```python
python main.py
```

**Note**: Run this in a separate folder and copy/paste the files into your vault, for safety.
