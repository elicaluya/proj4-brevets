# Project 4:  Brevet time calculator with Ajax

Reimplement the RUSA ACP controle time calculator with flask and ajax

Author: Elijah Caluya

## ACP controle times

That's "controle" with an 'e', because it's French, although "control"
is also accepted.  Controls are points where   
a rider must obtain proof of passage, and control[e] times are the
minimum and maximum times by which the rider must  
arrive at the location.

The algorithm for calculating controle times is described at
https://rusa.org/octime_alg.html . 
  

## AJAX and Flask reimplementation

The calculator takes in any amount of miles or km and then returns the open
and close times from the start date and time. The user can change the start
date and time and thus change the open and close times.  

## Testing

Testing is done through a nosetest suite that checks the functions in acp_times.py
and compares them to the predicted output. I used the online calculator from
https://rusa.org/octime_acp.html to compare the outputs and see if they are correct.
