# Contributing to TouchDown

We value your contribution. To keep everyone on the same track for contribution, here are some of the steps that are needed to be followed when contributing to the project.

## Pull Request Process

1. Direct merge to the master branch is neither permitted nor advised 
2. Ensure any install or build dependencies are removed before the end of the layer when doing a build.
3. Put comments on the lines of code you have added.
4. Update the requirements.txt file with the dependencies if you have added any.
5. Keep the code and data in separate folders.
6. While adding any new code to the repository, you are expected to test your code extensively. Pull requests with less code coverage are less likely to be merged.
7. Update the README.md with details of changes to the interface, this includes new environment variables, exposed ports, useful file locations and container parameters.
8. Increase the version numbers in any examples files and the README.md to the new version that this Pull Request would represent.
9. On opening a Pull Request, add team members(s) as reviwers.
10. Make necessary changes as per code review before merging the Pull request into Master branch.

## Branch Naming guideline
1. Feature development branch should begin with  name as "feature" eg: feature-punt-kickoff-addition
2. Each feature branch should have its own tests written
3. Bugs fixing branch should begin with "bugfix"
4. Patching branch should have "patch" in the name

## Code Design Guidelines
1. As far as possible follow DRY principles
2. Create seperate branch for each feature and each pull request should only merge only one feature
3. The code should strictly be placed in src folder and all the miscellanous activites should be outside of src branch
4. Delete commented code statements before commiting as a part of code cleanup


### You are contributing to this repository which is under MIT License: 
Please [LICENSE](https://github.com/himol7/American-Football-Analytics-Application/blob/master/LICENSE) for further details
