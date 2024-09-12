# Problem Statement

**Child care**, also known as **day care**, is the care and supervision of one or more children, typically ranging from two weeks to 18 years old.[^1] It refers to the care of children especially as *a service while parents are working*.[^2] This service is important for children as they need professional care while their parents are working. 

Areas where there are too few licensed slots for the number of children who need care are known as **child care deserts**, and more than half of America’s children live in one.[^3] To address this issue, the government has announced substantial grants to help child care providers maintain their services and expand their operations. For example, **New York State** (NYS) identified **$100M** to build and expand child care capacity in areas with the least supply.[^4]

## Problem A
Let's assume the NYS government plan to eliminate **child care deserts** in New York State. In particular, an area $a$ is defined as a child care deserts *if* 
$$ s_a \geq \frac{1}{3}\, p_a $$
where $s_a$ denotes the available slots in this area and $p_a$ denotes the population of children ranging from two weeks to 18 years old.

To achieve this goal, the government plans to allocate an amount of money to *either* **build new child care facilities** *or* **expand existing ones**. To build a new facility, the government needs to spend $c_{new}$ per $s_{new}$-slot facility; to expand an existing facility, the government needs to spend $c_{slot}$ per slot expansion. The final total slots in area $a$ then can be calculated as:
$$ s_a = s_{existing} + \sum_{f \in F_a} s^f_{ext} + n_{new} \times s_{new} $$
where $F_a$ denotes the set of existing facilities in area $a$.

Please help the government to determine the **minimum amount of money** needed to eliminate child care deserts (i.e. $s_a \geq \frac{1}{3}\, p_a$ for each $a$) for each zipcode region in New York State, subject to the following constraints: 
- The maximum slot expansion for each facility is $1.5$ times of its current capacity.


## Problem B

Beyond eliminating the child care deserts, the government also wants to **maximize the number of children who can receive child care services**. To achieve this goal, the government plans to use a total budget of $B$ to build (extra) new child care facilities or expand (more) existing ones. 

Please help the government to determine the **maximum number of children** who can receive child care services subject to the **budget constraint** and the following constraints:
- The maximum slot expansion for each facility is $1.5$ times of its current capacity.

We assume all constants are the same as in Problem A. Note that you do not have to build new facilities or extend slots based on the solution of Problem A. In other words, you are maximizing the total capacity of child care services under the no-desert and budget constraints.


## Problem C

Now, if the (marginal) cost of extending a slot is a convex piecewise linear function of the number of existing slots, i.e., the more slots are extended, the more expensive it is to extend one more slot. The cost function is given as follows:


Please answer the Problem A and Problem B with the new cost function, while all other constants remain the same as in Problem A and Problem B.

[^1]: https://en.wikipedia.org/wiki/Child_care
[^2]: https://www.merriam-webster.com/dictionary/childcare
[^3]: https://www.americanprogress.org/series/child-care-deserts/
[^4]: https://ocfs.ny.gov/programs/childcare/deserts/#overview

