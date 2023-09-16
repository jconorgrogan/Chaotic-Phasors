# Chaotic-Phasors

Utilizing a chaotic geometric system to craete "signitures" (sum of phasors at a randomly sampled set of T, right side) as a public key.  These public keys can be easily verified in a deterministic way given private-key starting conditions (phasors, including momentum and location, and other data such as collisions numbers), which can collide "cross-fire" stlye across overlapping circles. Can perfectly re-run in microseconds, but would take many universes to brute force. 

Python App
<img width="1134" alt="image" src="https://github.com/jconorgrogan/Chaotic-Phasors/assets/130090573/e413c786-fc01-476c-8538-854be16284c4">

HTML/Java

<img width="822" alt="image" src="https://github.com/jconorgrogan/Chaotic-Phasors/assets/130090573/a9097e10-4c4f-4fbe-a7e6-5a23c4c1fad0">
In these images, phasors race along the edge of these circles, preserving angular momentum. They can collide elastically, and also transfer their momentum to phasors on different circles. 

# Complexity Estimation of Brute-Forcing a Private Key.

Estimatins from above images and code; could also trivially increase complexity

1. **4 Circles**: Each with 10 phasors (nodes), totaling 40 phasors. Can optionally scale up phasors, circles, and other elements to make it even more mind-boggling complicated
2. **Precision**: Each phasor has a position and an angle, both to 16 decimal places.
3. **Collision Events**: Expected number of collisions is 10,000 in a given run.

## Complexity Estimation

1. **Position & Speed**: For each of the 40 phasors, there are \(2 \times 10^{16}\) possible starting positions and \(2 \times 10^{16}\) possible speeds (angular momenta) due to 16 decimal places of precision. This results in \((2 \times 10^{16})^2\) states for a single phasor.
2. **All Phasors**: For all 40 phasors, the total possible states become \((2 \times 10^{16})^{2 \times 40}\).
3. **Collision Events**: For each collision event, it could occur between any two of the 40 phasors. There are \({{40}\choose{2}} = 780\) combinations of 2 phasors. For 10,000 collision events, this becomes \(780^{10,000}\).
4. **Total States**: Combine the states due to phasors and collision events: \((2 \times 10^{16})^{2 \times 40} \times 780^{10,000}\).

## Brute-Force Calculation

Using the computational power of the world's fastest supercomputer, Fugaku, which operates at \(442.01 \times 10^{15}\) FLOP/s:

Time = \[\frac{(2 \times 10^{16})^{2 \times 40} \times 780^{10,000}}{442.01 \times 10^{15}}\] seconds

For simplification, consider just \(780^{10,000}\), which is already approximately \(10^{6000}\):

\[\frac{10^{6000}}{10^{16}} = 10^{5984}\] seconds

Even with the world's fastest supercomputer, cracking this system would take on the order of \(10^{5984}\) seconds. For context, the estimated age of the universe is about \(4.3 \times 10^{17}\) seconds.  


