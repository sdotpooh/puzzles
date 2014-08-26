https://www.codeeval.com/open_challenges/145/

You're planning your party's campaign strategy to win the Presidency of the United States.

To win, your candidate will have to navigate many controversial issues which influence voters like healthcare, immigration, education, energy independence, jobs, taxes and the environment etc. Each of these is important but also expensive to address.

Since the United States presidential election is determined by states casting votes in the Electoral College, you will need a minimum of 270 out of the total of 538 Electoral College votes to win.

While not completely accurate, for this challenge we will use the following criteria:

States may or may not value an issue.
States value each issue differently.
Winning 51% of any state gives you all of that state's votes.If you have less than 51 % you won't receive any votes
Your goal is to put together a winning strategy by identifying the fewest issues you must address to win 270 votes.

INPUT SAMPLE:

Your program should accept as its first argument a path to a file name. The file contents would be the following:

Social issues: 9
Healthcare: 33995797
Immigration: 2089699
Education: 37182280
Energy independence: 1344134
...
Wealth inequality: 99237127
Increase military spending: 44066575
Mississippi
Votes: 6
Creating jobs: 1
Jobs: 0
...
Increase military spending: 0
Education: 1
Energy independence: 0
Oklahoma
Votes: 7
Creating jobs: 1
Jobs: 2
...
Increase military spending: 0
Education: 1
Energy independence: 2
...
Maine
Votes: 4
Creating jobs: 0
Jobs: 0
...
Increase military spending: 0
Education: 1
Energy independence: 3


The first line states the total number of potential issues. After that is information about costs for each program and after that goes information about each state, separated by spacing. Each state has a Name, Number of votes it has and a list of the issues that you can choose in each state. Each of the issues are valued based on the number of votes it can affect for each state. Remember, you must gain the majority of votes in each state to win it.

OUTPUT SAMPLE:

Print out the list of issues you want to cover in you electoral program in alphabetical order. E.g.

Energy independence
Healthcare
Immigration
Increase military spending

Remember that your goal is to create a program with fewest number of issues. If there are several variants of program with fewest number of issues, then you need to choose program with minimum costs.
