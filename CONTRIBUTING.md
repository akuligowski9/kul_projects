#Projects Contribution Guidelines

Welcome to my Projects! These guidelines will give you a short overview over how we
handle issues and PRs in this repository. Note that they are preliminary and
still need proper phrasing - if you'd like to help - be sure to make a PR.

Please know that we do appreciate all contributions - bug reports as well as
Pull Requests.

## Filing Issues

When filing an issue, please use this template:

```
# Overview Description

# Steps to Reproduce

1.
2.
3.

# Actual Results

# Expected Results

# Reproducibility

# Additional Information:

```

## PR Merge Criteria

For a PR to be merged, the following statements must hold true:

- All CI services pass. (Windows build, linux build, sufficient test coverage.)
- All commits must have been reviewed and approved by a maintainer who is
  not the author of the PR. Commits shall comply to the "Good Commits" standards
  outlined below.


## Correcting PRs

Rebasing PRs is preferred over merging master into the source branches again
and again cluttering our history. If a reviewer has suggestions, the commit
shall be amended so the history is not cluttered by "fixup commits".

## Writing Good Commits

Please see
https://api.coala.io/en/latest/Developers/Writing_Good_Commits.html
for guidelines on how to write good commits and proper commit messages.
