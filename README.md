# Chaotic-Phasors

This project is a simulation of a system of phasors (rotating vectors) organized in multiple circles. Each circle contains a set number of phasors with their own initial angles and angular speeds. The phasors can collide both within their own circle and with phasors from other circles "cross-fire" style.  Can perfectly re-run in microseconds, but would take many universes to brute force/reverse without the starting key. 

This method can be used to create a quantum-resistant means of encryption. Simulation output (sum of phasors at a randomly sampled set of T**) is  public key.  These public keys (right side on below image) can be easily verified in a deterministic way given private-key starting conditions (phasors, including momentum and location, and other data such as collisions numbers). 

Image from run on Python App
<img width="1134" alt="image" src="https://github.com/jconorgrogan/Chaotic-Phasors/assets/130090573/e413c786-fc01-476c-8538-854be16284c4">

Image from run on HTML/Java

<img width="822" alt="image" src="https://github.com/jconorgrogan/Chaotic-Phasors/assets/130090573/a9097e10-4c4f-4fbe-a7e6-5a23c4c1fad0">


# Complexity Estimation of Brute-Forcing a Private Key.

Estimations from above images and code; TLDR, state space is  ![4^40 x 10^1920 x 780^{10,000}](https://latex.codecogs.com/gif.latex?4%5E%7B40%7D%20%5Ctimes%2010%5E%7B1920%7D%20%5Ctimes%20780%5E%7B10%2C000%7D)

### Assumptions

1. **4 Circles:** Each with 10 phasors (nodes), totaling 40 phasors. Can optionally scale up phasors, circles, and other elements for added complexity.
2. **Precision:** Each phasor has a position and an angle, both with up to 16 decimal places of precision.
3. **Collision Events:** Expected number of collisions is 10,000 in a given run.
4. **Friction:** The friction introduced during a collision can take up to \(10^{16}\) different values.

### Logic

#### Position, Speed, and Friction

- For a single phasor, the possible states due to position and speed, and friction would be: 
  ![4x10^48](https://latex.codecogs.com/gif.latex?4%20%5Ctimes%2010%5E%7B48%7D)

#### All Phasors

- For all 40 phasors, the total possible states become: 
  ![4^40 x 10^1920](https://latex.codecogs.com/gif.latex?4%5E%7B40%7D%20%5Ctimes%2010%5E%7B1920%7D)

#### Collision Events

- For each collision event, it could occur between any two of the 40 phasors. The total number of combinations of 2 phasors is \({{40}\choose{2}} = 780\). For 10,000 collision events, the number of possible combinations becomes: 
  ![780^{10,000}](https://latex.codecogs.com/gif.latex?780%5E%7B10%2C000%7D)

#### Total States

- Combining the states due to phasors and collision events: 
  ![4^40 x 10^1920 x 780^{10,000}](https://latex.codecogs.com/gif.latex?4%5E%7B40%7D%20%5Ctimes%2010%5E%7B1920%7D%20%5Ctimes%20780%5E%7B10%2C000%7D)

### Brute-Force Calculation

- Using the computational power of the world's fastest supercomputer, Fugaku, which operates at \(442.01 \times 10^{15}\) FLOP/s, the time required to crack the system would be: 
  ![10^{7926}](https://latex.codecogs.com/gif.latex?10%5E%7B7926%7D) seconds.

For context, the estimated age of the universe is about \(4.3 \times 10^{17}\) seconds.  

**Note: "Signiture" can not be continous data as it will open up reversal-type attacks. Propose mixing disperate sections of T while also mapping integers,
