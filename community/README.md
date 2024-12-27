# community

## Installation

### Prerequisites


## Getting started with Talon

1. `help active` displays commands available in the active (frontmost) application.
   - Available commands can change by application, or even the window title.
   - Navigate help by voice using the displayed numbers (e.g., `help one one` or `help eleven` to open the item numbered 11), or by speaking button titles that don't start with numbers (e.g., `help next` to see the next page of contexts).
   - Help-related commands are defined in [help.talon](core/help/help.talon) and [help_open.talon](core/help/help_open.talon).
2. Search for commands by saying `help search <phrase>`. For example, `help search tab` displays all tab-related commands, and `help search help` displays all help-related commands.
3. Jump immediately to help for a particular help context with the name displayed the in help window (based on the name of the .talon file), e.g. `help context symbols` or `help context visual studio`
5. `command history` toggles display of recent voice commands.


### Formatters

Formatter names (snake, dubstring) are defined [here](core/text/formatters.py#L245). Formatter-related commands are defined in [text.talon](core/text/text.talon#L8).


## Additional commands

There are other commands not described fully within this file. As an overview:

- The core folder has various commands described [here](core/README.md)
- The lang folder has commands for writing [programming languages](#programming-languages)
- The plugin folder has various commands described [here](plugin/README.md)
- The tags folder has various other commands, such as using a browser, navigating a filesystem in terminal, and managing multiple cursors

# Collaborators

This repository is now officially a team effort. The following contributors have direct access:

- @dwiel
- @fidgetingbits
- @knausj85
- @rntz
- @splondike
- @pokey

Collaborators will reply to issues and pull requests as time and health permits. Please be patient.

## Guidelines for collaborators

1. Collaborators prioritize their health and their personal/professional needs first. Their time commitment to this effort is limited.
2. For "minor" fixes and improvements/bugs/new apps, collaborators are free to contribute without any review
3. For "significant" new development and refactors, collaborators should seek appropriate input and reviews from each-other. Collaborators are encouraged to open a discussion before committing their time to any major effort.

# Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for our guidelines for contributors

## Automatic formatting/linters

This repository uses [`pre-commit`](https://pre-commit.com/) to run and manage its formatters/linters. Running these yourself is optional. If you wish to do so, first [install](https://pre-commit.com/#install) `pre-commit`:

```bash
$ pip install pre-commit
```

You then have a few options as to when to run it:

- Run yourself at any time on your locally changed files: `pre-commit run`
- Run yourself on all files in the repository: `pre-commit run --all-files`
- Run automatically on your PRs (fixes will be pushed automatically to your branch):
  - Visit https://pre-commit.ci/ and authorize the app to connect to your `community` fork.
- Set up an editor hook to run on save:
  - You could follow the instructions for [Black](https://black.readthedocs.io/en/stable/integrations/editors.html), which are well written; simply replace `black <path>` with `pre-commit run --files <file>`.
  - It's more performant to only reformat the specific file you're editing, rather than all changed files.
- Install a git pre-commit hook with `pre-commit install` (optional)
  - This essentially runs `pre-commit run` automatically before creating local commits, applying formatters/linters on all changed files. If it "fails", the commit will be blocked.
  - Note that because many of the rules automatically apply fixes, typically you just need to stage the changes that they made, then reattempt your commit.
  - Whether to use the hook comes down to personal taste. If you like to make many small incremental "work" commits developing a feature, it may be too much overhead.

If you run into setup difficulty with `pre-commit`, you might want to ensure that you have a modern Python 3 local environment first. [pyenv](https://github.com/pyenv/pyenv) is good way to install such Python versions without affecting your system Python (recommend installing 3.9 to match Talon's current version). On macOS you can also `brew install pre-commit`.

## Automated tests

There are a number of automated unit tests in the repository. These are all run _outside_ of the Talon environment (e.g. we don't have access to Talon's window management APIs). These make use of a set of stubbed out Talon APIs in `test/stubs/` and a bit of class loader trickery in `conftest.py`.

To run the test suite you just need to install the `pytest` python package in to a non-Talon Python runtime you want to use for tests (i.e. don't install in the `~/.talon/.venv directory`). You can then just run the `pytest` command from the repository root to execute all the tests.

## Talon documentation

For official documentation on Talon's API and features, please visit https://talonvoice.com/docs/.

For community-generated documentation on Talon, please visit https://talon.wiki/.
