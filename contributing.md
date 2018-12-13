# Contribution guidelines

First of all, thanks for thinking of contributing to this project. :smile:


- If a relevant issue already exists, discuss on the issue and get it assigned to yourself on GitHub.
- If no relevant issue exists, open a new issue and get it assigned to yourself on GitHub.

 Before contributing please contact us and so that we can make sure that no one is working on that what you are planning to do.You can contact us on the gitter group: https://gitter.im/facebook-User-Information/Lobby?utm_source=share-link&utm_medium=link&utm_campaign=share-link or on relevant issues itself. We welcome any contribution that could enhance app's functionality. Kindly follow the simple steps below to submit a Pull Request.

# Development

1) Fork this repo and clone the forked repo locally.
2) Install with

    ```sh
    git clone https://github.com/ujjaldas132/facebook-User-Information.git
    cd facebook-User-Information
    git remote set-url upstream https://github.com/ujjaldas132/facebook-User-Information.git
    git remote set-url origin https://github.com/ujjaldas132/facebook-User-Information.git
    sudo chmod a+x run.sh # only for the first time
    ```

3) Make a seperate branch with a descriptive name (that could explain the purpose of the PR) such as `awesome_feature` and switch to it by running `git checkout -b your_branch(here, awesome_feature)` in the terminal.

4) Add/Modify the code and do `git add files_involved` to add your changes.

5) Commit your changes using `git commit -am "your_message"`. Please refer to [commit message guidelines](https://chris.beams.io/posts/git-commit/) to write better commit messages. It will help in an easier review process.

6) Do `git pull upstream master` to sync with this repo.

7) Do `git push origin your_branch(here, awesome_feature)` to push code into your branch.

8) Finally, create a PR by clicking on the `New pull request` button [here](https://github.com/ujjaldas132/facebook-User-Information/pulls). Make sure your PR is compliant with the following checklist.
