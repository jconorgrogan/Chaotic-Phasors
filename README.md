# Chaotic-Phasors

**Overview**

This project is a simulation of a system of phasors (rotating vectors) organized in multiple circles and attempt to harness a deterministic chaotic system to create a unique encryption system. In this project, each circle starts with a set number of phasors with their own initial angles and angular speeds. The phasors can collide both within their own circle and with phasors from other circles "cross-fire" style.  Can perfectly re-run in microseconds (any starting position will produce same finishing position and interim conditions).

Simulation output (sum of phasors at a randomly sampled set of T**; expect to make the output non-continuous, or map elements such as the collision # to state of each phasor) is the public key.  These public keys (illustrative example of output below) can be easily verified in a deterministic way given private-key starting conditions (phasors, including momentum and location, and other data such as collisions numbers). An (extremely low confidence)upper-bound estimate is the time required to crack the system is on the order of ![e^{66760.5}](https://latex.codecogs.com/gif.latex?e%5E%7B66760.5%7D) times the estimated age of the universe (![4.3 \times 10^{17}](https://latex.codecogs.com/gif.latex?4.3%20%5Ctimes%2010%5E%7B17%7D) seconds) but this needs peer review.

**Example Output**
Gif of some of the first few frames from HTML app (collision counter since fixed)
![Phasors_segment](https://github.com/jconorgrogan/Chaotic-Phasors-Encryption/assets/130090573/b42b94fe-d311-4638-8e09-77bf7ff0b66e)

Butterfly Effect: A 1 bit change (0.000001 addition to velocity in one node) leads to a significant change in the output

Run 1 with final node position on left, Output ("Public Key") in middle, starting conditions(Private Key) on bottom, visualized on top right
<img width="1456" alt="Pasted Graphic 9" src="https://github.com/jconorgrogan/Chaotic-Phasors-Encryption/assets/130090573/48c93649-6bb1-42bf-9114-ff5a38079de2">

Run 2, with a 1 bit change to angular speed on the first phasor, all else the same
<img width="1456" alt="image" src="https://github.com/jconorgrogan/Chaotic-Phasors-Encryption/assets/130090573/b7275bee-557b-4724-8b04-33278684b836">

**To-do: Establishing the NP-hardness of the problem. WIP and will invite any comments**
## Problem Identification

The problem involves recovering the private key \( I \) from a given sequence of time-states \( T = \{T_1, T_2, \ldots, T_n\} \) where each \( T_i \) represents the system state at a certain time or collision point. The deterministic chaotic system \( \mathcal{C} \) involves rotating phasors with specific dynamics and collision mechanics. 

## Problem Formalization

Given a deterministic chaotic system \( \mathcal{C} \), find the initial conditions \( I \) that lead to a known sequence of time-states \( T \) when evolved according to the dynamics of \( \mathcal{C} \).

### Parameters

- \( N \) phasors, each with initial angle \( \theta_i \) and angular speed \( \omega_i \)
- A finite set \( M \) of collisions, affecting two phasors' angular speeds based on predefined collision rules
- An evolution function \( E(S, t) \) that specifies how the state \( S \) changes over time \( t \) and upon collisions
- \( T = \{T_1, T_2, \ldots, T_n\} \), a sequence of system states at specific times or collision points

## Computational Complexity Hypothesis

The problem belongs to the NP-hard class. Given a proposed solution \( I \), we can verify it in polynomial time by evolving the system \( \mathcal{C} \) using \( E(S, t) \) to generate \( T \).

## Reduction to Known NP-hard Problem (Hamiltonian Path Problem)

### Hamiltonian Path Problem

Given a graph \( G = (V, E) \), find a path that visits each vertex in \( V \) exactly once.

### Reduction Steps

1. **Vertex to Phasor Mapping**: Each vertex \( v \in V \) is mapped to a unique phasor with specific initial conditions \( \theta_i, \omega_i \) in \( \mathcal{C} \). This mapping is a bijection and can be performed in polynomial time with respect to the size of \( V \).

2. **Edge to Collision Mapping**: Each edge \( e \in E \) is deterministically mapped to a collision event in \( M \). Collision rules mirror the structure of \( G \). This mapping is polynomial time in \( |E| \).

3. **Path to Time-States Mapping**: A Hamiltonian path \( P \) in \( G \) corresponds to a sequence of time-states \( T \) in \( \mathcal{C} \). This mapping is polynomial time and preserves problem difficulty. The difficulty preservation follows from the constraints of Hamiltonian pathing, which translate to the complexity of achieving the specified sequence \( T \).

4. **Algorithm Adaptation**: Algorithms solving Hamiltonian Path Problem in \( G \) can be adapted to find \( I \) in \( \mathcal{C} \), maintaining polynomial time complexity in \( |G| \).

### Formal Proofs

1. **Polynomial Time**: All mappings are polynomial in time, which is shown by demonstrating that each mapping can be performed in \( O(n^k) \) time, where \( n \) is the size of the input and \( k \) is a constant.
  
2. **Preserving Problem Difficulty**: Establishing this rigorously would involve showing that any algorithm solving \( G \) can be adapted to solve for \( T \) in \( \mathcal{C} \), and vice versa, without a significant increase in computational resources.

# Encryption Method #

## Key Modification
The initial few bits of data act as a modifier for the 'private key,' affecting how the phasor run is generated. This could be altering the speed, changing certain operations, or any other parameter that significantly affects the system's behavior.

## Message Encoding
The subsequent parts of the message are mapped onto features of this modified phasor run. For instance, the first bit could be encoded as the conditions at the first collision, the second bit as the conditions at the second collision, and so on.

## Transmission
The sender communicates this encoded message to the receiver.

## Decryption and Reading
The receiver applies the initial few bits of data to their synchronized private key, recreates the modified phasor run, and then decodes the message using the agreed-upon mapping.



# Upper Bound Complexity Estimation of Brute-Forcing a Private Key.

- **4 Circles, 10 Phasors Each**: The system consists of 4 circles, each containing 10 phasors, totaling 40 phasors.
- **Random Initialization**: Angles are initialized randomly between (0) and (2\pi), and speeds are initialized randomly between (-40) and (40).
- **Collision Mechanics**: Collisions are determined by a set size, and upon collision, phasors swap their angular momentum. There is additional "friction" added by the system during cross-circle collisions
- **Fixed Time Step**: A fixed time step of (0.001) is used for updating the phasors.

## Logic for Complexity Estimation

### Angles and Speeds

For one phasor, the complexity due to angles and speeds is calculated as:  
![\text{Single Phasor Complexity} = 2\pi \times 80 = 160\pi](https://latex.codecogs.com/gif.latex?%5Ctext%7BSingle%20Phasor%20Complexity%7D%20%3D%202%5Cpi%20%5Ctimes%2080%20%3D%20160%5Cpi)

For all 40 phasors, the total complexity becomes:  
![\text{Total Phasor Complexity} = (160\pi)^{40}](https://latex.codecogs.com/gif.latex?%5Ctext%7BTotal%20Phasor%20Complexity%7D%20%3D%20%28160%5Cpi%29%5E%7B40%7D)

### Collision Events

The number of distinct collision pairs is ![ \binom{40}{2} = 780 ](https://latex.codecogs.com/gif.latex?%20%5Cbinom%7B40%7D%7B2%7D%20%3D%20780%20).  
Assuming a set number of collisions (10,000), the complexity due to collision events is:  
![\text{Total Collision Complexity} = 780^{10,000}](https://latex.codecogs.com/gif.latex?%5Ctext%7BTotal%20Collision%20Complexity%7D%20%3D%20780%5E%7B10%2C000%7D)

## Total Complexity

The total complexity of the system is given by:  
![\text{Total Complexity} = \text{Total Phasor Complexity} \times \text{Total Collision Complexity}](https://latex.codecogs.com/gif.latex?%5Ctext%7BTotal%20Complexity%7D%20%3D%20%5Ctext%7BTotal%20Phasor%20Complexity%7D%20%5Ctimes%20%5Ctext%7BTotal%20Collision%20Complexity%7D)

Logarithmically, this is expressed as:  
![\log(\text{Total Complexity}) = 40 \log(160\pi) + 10,000 \log(780)](https://latex.codecogs.com/gif.latex?%5Clog%28%5Ctext%7BTotal%20Complexity%7D%29%20%3D%2040%20%5Clog%28160%5Cpi%29%20%2B%2010%2C000%20%5Clog%28780%29)

## Time to Crack

Using Fugaku's computational power of ![442.01 \times 10^{15}](https://latex.codecogs.com/gif.latex?442.01%20%5Ctimes%2010%5E%7B15%7D) FLOP/s, the logarithmic time required to crack the system is:  
![\log(\text{Time to Crack}) = \log(\text{Total Complexity}) - \log(\text{Fugaku Speed})](https://latex.codecogs.com/gif.latex?%5Clog%28%5Ctext%7BTime%20to%20Crack%7D%29%20%3D%20%5Clog%28%5Ctext%7BTotal%20Complexity%7D%29%20-%20%5Clog%28%5Ctext%7BFugaku%20Speed%7D%29)

The logarithmic time required to crack the system, when expressed in units of the estimated age of the universe, is approximately  
![\log(\text{Time to Crack}) \approx 66760.5](https://latex.codecogs.com/gif.latex?%5Clog%28%5Ctext%7BTime%20to%20Crack%7D%29%20%5Capprox%2066760.5).

This means that the time required to crack the system is on the order of ![e^{66760.5}](https://latex.codecogs.com/gif.latex?e%5E%7B66760.5%7D) times the estimated age of the universe (![4.3 \times 10^{17}](https://latex.codecogs.com/gif.latex?4.3%20%5Ctimes%2010%5E%7B17%7D) seconds).

**Note: "Public Key" can not be continous data as it will open up reversal-type attacks. Propose mixing disperate sections of T while also mapping integers,
