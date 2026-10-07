# grade-calculator
Demo for Gen AI


# Grade Calculator

A small Python project for the **Code With AI Agents** station at the
Google x ColorStack UMN AI Workflow Night (Oct 7, 2026). You'll use an AI
agent in Google Antigravity to find a bug, fix it, and write tests.

## What's in here

| File | What it does |
| --- | --- |
| `grades.py` | `weighted_average()` calculates a course grade from category scores and weights. `letter_grade()` turns a number into A-F. |
| `demo.py` | Runs a sample course through the calculator and prints the result next to the expected answer. |

There are no tests yet. Part of the exercise is getting the agent to write them.

## Run it

You need Python 3.8 or newer. No packages to install.

```
python demo.py
```

The first line of output should match the "Expected" line. Right now it
doesn't, and your job is to get an agent to find out why.

## Set up Antigravity

1. Download Google Antigravity from https://antigravity.google/download and
   sign in with your Google account.
2. Open this folder as your workspace.
3. In the Agent Manager, start a new conversation and choose **Planning** mode,
   so the agent shows a plan before it changes any code.

Antigravity is in preview and its menus change often, so your screen may look
slightly different from what's described here.

## Try it: fix the bug

Paste this prompt:

> The grade calculation gives wrong results. Find the bug, fix it, and add
> tests that prove it works. Show me your plan first.

Then:

1. Read the agent's implementation plan before approving it.
2. Let it make the change and run the tests.
3. Review the diff. Does the fix make sense to you?
4. Run `python demo.py` again and confirm the output now matches.

## Challenge: add a feature

Ask the agent to add **one** small feature, with tests. Ideas:

- Drop the lowest quiz score before averaging
- Add plus and minus letter grades (B+, A-)
- Reject weights that don't add up to 1.0

Then check the work yourself instead of trusting it:

- Do the tests cover the edge cases, like an empty list or a single score?
- Would the tests have failed before the change?
- Does the code do what you actually asked for?

## Tips

- Give the agent one clear task at a time.
- Always review the plan and the diff. You are the one responsible for the code.
- If you hit a usage limit on the free tier, wait for it to reset or pair up
  with someone nearby.

## Questions?

Find the Station 2 leads at the event, or ask in the ColorStack UMN community.
