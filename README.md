# EPL
 An algorithm to get the standing of the EPL after certain rounds  or till a certain Date
using graph representaion 




### Diagram of our represenation

![Diagram](https://i.imgur.com/2FxYQrw.jpg)

### Algorithm Steps
1. Take input from csv file (standings.csv in this case)
2. data is represented in Round/Date Objects to traverse either by round number / date
3. in case of round number we traverse to the round number then to the dates its played in then in matches in each date
4. in case of date we do the same but starting from date ...
5. then output is displayed to the screen using tk lib.


### Algorithm Complexity: 
 #### O(M) Where M is the number of matches
