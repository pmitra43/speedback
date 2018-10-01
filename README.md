# Speedback
A console app written in python, which can be used to drive a speed feedback session among a team of any size.
This will create pairs, and distribute them into rounds, making sure that everybody gets a chance to give and receive feedback from everyone else.

#### Requirements:
* Python v3.6
* pip3
* say

### How to run:
1. Clone this repository and get in: `git clone git@github.com:pmitra43/speedback.git && cd speedback`
2. Install dependencies: `pip3 install -r dependencies.txt`
3. Create a copy of **example-config.yml** and name it **config.yml**
4. Add name of all the team members in `members` of config.yml
5. Adjust the duration config:
    * `feedbackPreparationTimeInMinutes`: denotes the amount of time to provide to a pair to prepare for feedback. **It has to be an integer.**
    * `pairFeedbackTimeInMinutes`: denotes how much time each pair will get to share feedback between them. Every person in the pair will get half of this time to speak. **It has to be an integer.**
    * `pairSwitchTimeInSeconds`: denotes the amount of time required for team members to find their next pair when a round ends. This time is provided so that the members can refer to the grid and find their next pair. **It has to be an integer.**
6. Run app `./app.py`

/*test 3*/
