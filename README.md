# Chaotic-Phasors

This project is a simulation of a system of phasors (rotating vectors) organized in multiple circles. Each circle contains a set number of phasors with their own initial angles and angular speeds. The phasors can collide both within their own circle and with phasors from other circles "cross-fire" style.  Can perfectly re-run in microseconds (any starting position will produce same finishing position and interim conditions), but would take many universes to brute force/reverse without the starting key. 

This method can be used to create a quantum-resistant means of encryption. Simulation output (sum of phasors at a randomly sampled set of T**) is  public key.  These public keys (illustrative example of output below on righthand frame) can be easily verified in a deterministic way given private-key starting conditions (phasors, including momentum and location, and other data such as collisions numbers). An upper-bound estimate is the time required to crack the system is on the order of ![e^{66760.5}](https://latex.codecogs.com/gif.latex?e%5E%7B66760.5%7D) times the estimated age of the universe (![4.3 \times 10^{17}](https://latex.codecogs.com/gif.latex?4.3%20%5Ctimes%2010%5E%7B17%7D) seconds).


Example Gif of some of the first few frames from HTML app 
![Phasors_segment](https://github.com/jconorgrogan/Chaotic-Phasors-Encryption/assets/130090573/b42b94fe-d311-4638-8e09-77bf7ff0b66e)

A 1 bit change (0.000001 addition to velocity in one node) leads to a significant change

Original run. Finalize node position on left, Output ("Public Key") in middle, starting conditions(Private Key) on bottom, visualized on top right
<img width="1456" alt="Pasted Graphic 9" src="https://github.com/jconorgrogan/Chaotic-Phasors-Encryption/assets/130090573/48c93649-6bb1-42bf-9114-ff5a38079de2">

Run 2, with a 1 bit change to angular speed on the first phasor, all else the same
<img width="1456" alt="image" src="https://github.com/jconorgrogan/Chaotic-Phasors-Encryption/assets/130090573/b7275bee-557b-4724-8b04-33278684b836">



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

**Note: "Signiture" can not be continous data as it will open up reversal-type attacks. Propose mixing disperate sections of T while also mapping integers,
