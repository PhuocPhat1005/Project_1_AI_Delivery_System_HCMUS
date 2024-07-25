***University of Science (HCMUS) - Introduction to Artificial Intelligence - CSC14003***
# Project 1. Searching (2024 / K22 CLC)
## Delivery System
### 1. Description
Thanks to the development of e-commerce, consumers can easily shop for products with just a smartphone from their  homes. In this context, the logistics industry plays an important role in ensuring efficient transportation of goods from sellers to buyers.
The most crucial strategy for logistics providers to compete effectively is to develop a system that finds the shortest paths. This system optimizes delivery routes, minimizes travel time, and saves fuel. Your team will be responsible for developing this system for HCMUS Logistic Co. LTD, utilizing search algorithms learned in the course CSC14003 - Introduction to Artificial Intelligence, **to find the path from the delivery vehicle to the customer**.
The city map has been modeled in 2D with n rows and m columns. The map consists of polygons to depict structures such as buildings, walls, etc., and these objects are unchanged on the map. 
**Figure 1** is an example of a city map modeled in the 2D world.

<center>
    <img src = "https://github.com/user-attachments/assets/8047a113-207d-4e7a-b76a-50a1bedce361" width="250" alt="Figure 1: 2D City map."/>
    <div style="text-align: center;"><b>Figure 1</b>: 2D City map.</div>
</center>

The map is technically represented as a **2D array**, each cell contains a value encoding some meaning. At a basic level, some values are predefined as follows:
* `0`: Space that the delivery vehicle can be moved into.
* `-1`: Impassable space, representing buildings, walls, and objects in the city.
* `S`: The **Starting location** of the delivery vehicle.
* `G`: The customer, also the **Goal location** of the delivery vehicle.

The delivery vehicle can move in four directions: **Up**, **Down**, **Left**, and **Right**, and no diagonally.
**Figure 2** describes the move directions of the delivery vehicle

<center>
    <img src = "https://github.com/user-attachments/assets/2b62332b-2f68-49e6-884c-102e4aadd380" width="250" alt="Figure 2: Move directions of the delivery vehicle."/>
    <div style="text-align: center;"><b>Figure 2</b>: Move directions of the delivery vehicle.</div>
</center>

### 2. Specifications
The project is divided into different levels, each of which offers increasing levels of difficulty to suit the diverse expectations of student groups. Detailed information will be provided below.

#### 2.1 Level 1 (Basic level)
In this level, find the path from the delivery vehicle (S) to the customer (G) with the information provided in ==*section 1*== and from the input file.
Students are required to, at a minimum, implement the following search algorithms:
* **Blind search methods**: Breadth-First Search, Depth-First Search, Uniform-Cost Search.
* **Heuristic search method**: Greedy Best First Search, A*.

Note that there may be cases where a path does not exist. Please test these cases as well.
#### 2.2 Level 2 (Time limitation)
The time to move between two adjacent cells is ++**1 minute**++. However, there are cells where a vehicle is required to stop for a[i, j] minutes to pay a road toll (a positive integer which is calculated according to the average waiting time of vehicles), called **Toll Booths** - illustrated by blue squares as shown in **Figure 3**.
![lev2](https://hackmd.io/_uploads/B1qmSqkYA.png "Figure 3: The blue squares are Toll Booths, and the lines are paths")
*++**Figure 3**++: The blue squares are Toll Booths, and the lines are paths*

The presence of toll booths increases the delivery time. To compete with other delivery services, your company has decided to commit to fast delivery within t minutes (provided in the input file). Please program a solution to find the shortest path that satisfies the condition of not exceeding
the committed delivery time.
As illustrated in **Figure 3**, with `t = 20`, it can be seen that:
* The <font style='color:red'>**red path**</font> is the shortest path (passing `13` cells), but it is not chosen because of overtime committed (`21` minutes of delivery).
* The <font style='color:green'>**green path**</font> and <font style='color:orange'>**orange path**</font> have the same delivery time (`17` minutes of delivery), but the <font style='color:green'>**green path**</font> is chosen because it is shorter (passing through `13` cells).

Note that **(at least) an algorithm** is required to be implemented at this level.
#### 2.3 Level 3 (Fuel limitation)
Any vehicle has a fuel tank capacity limit, and the company’s delivery vehicle is no different, with a capacity of f liters (provided in input). Each move to an adjacent cell consumes 1 liter of fuel. When the vehicle runs out of fuel, the delivery will be stopped. Therefore, gas stations are added to the map (illustrated by yellow squares in **==Figure 4==**) so that the delivery vehicle can refuel.
![lev3](https://hackmd.io/_uploads/SkrgO9ktA.png)
As illustrated in Figure 4, with f = 10, it can be seen that:
* The <font style='color:green'>**green path**</font> is the shortest path (passing through 13 cells, with 17 minutes of delivery), but it is not feasible because there is not enough gasoline right after leaving the toll booth.
* The <font style='color:yellow'>**yellow path**</font> is longer (passing through 15 cells, with 20 minutes of delivery), but it is feasible because the vehicle has refueled at the fuel station F (included 1 minute to refill).

++Note that:++
* Initially the delivery vehicle was always full of fuel.
* When passing through the fuel station, the delivery vehicle will be refueled to full capacity.
* When stationary at toll booths, the vehicle does not consume fuel.
* An algorithm is required to be implemented at this level.
#### 2.4 Level 4 (Multiple agents)

---
## Members of Team
| No. | Student ID | Full name       | Tasks | Completion |
|:---:|:----------:| --------------- | ----- |:----------:|
|  1  |  22127174  | Ngô Văn Khải    |       |   100 %    |
|  2  |  22127322  | Lê Phước Phát   |       |   100 %    |
|  3  |  22127388  | Tô Quốc Thanh   |       |   100 %    |
|  4  |  22127441  | Thái Huyễn Tùng |       |   100 %    |
