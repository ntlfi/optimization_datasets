### Problem A (Knapsack)

Assume that we can only ship health commodities from USA to supported countries directly (no transfer station) by air. We also assume that the cost of shipping is proportional to the weight of the items and the US government has a limited budget for shipping (in total). The US government wants to maximize the total value of the items that can be carried.

We have the following data: We are using **Boeing 747-8F** to ship the items. The maximum takeoff weight of a Boeing 747-8F is **442,000 kg**. The cost of shipping per kilogram is **\$6**. We assume that the total budget for shipping is **\$1,000,000**.

Please determine the maximum total value of the items that can be carried to supported countries.

### Problem B (Minimum Spinning Tree)

Assume that we now are allowed to ship health commodities from USA to supported countries by using any of airports as transfer stations. We also assume the CO2 emissions of the flights are proportional to the distance between the airports. Assume that we are going to ship health commodities to all supported countries on the same day, and the each airplanes used has enough capacity for the commodities shipped. The US government wants to minimize the CO2 emissions of the flights. 

We have the following data: the CO2 emissions of a Boeing 747-8F is **53.3 kg/mile**. 

Please determine the minimum CO2 emissions of the flights.


### Problem C (Integer Programming)

Assume that we now are allowed to ship health commodities from USA to supported countries by using any of airports as transfer stations, but we have to follow some specific routes. In particular, 
[TO-DO: Add the routes]
- We can only use the following routes: 
    - **Route 1**: USA -> Canada -> Supported Countries
    - **Route 2**: USA -> Mexico -> Supported Countries
    - **Route 3**: USA -> Brazil -> Supported Countries. 

Assume that we are going to ship health commodities to all supported countries on the same day. For each route, we can schedule multiple flights on the same day. Each airplane only has limited capacity for the commodities shipped (due to other shipment duties). The US government wants to ship all commodities to supported countries with the minimum number of flights.

Please determine the minimum number of flights needed to ship all commodities to supported countries.