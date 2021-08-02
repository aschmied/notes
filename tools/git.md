# Git

* Delete all unstaged files: `git clean -df`
* Stash with message: `git stash save "message"`
* Incremental stashing: `git stash -p`
* Temporarily ignore file: `git update-index --assume-unchanged <file>`
* Unignore temporarily ignored file: `git update-index --no-assume-unchanged <file>`
* Ignore a file: `git update-index --skip-worktree <file>`
* Unignore a file: `git update-index --no-skip-worktree <file>`
