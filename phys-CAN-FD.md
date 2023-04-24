# The physical layer of CAN FD

Daniel Štanc, Jakub Jíra

Measured: 18.4.2023, Documented: 19.4.2023

repository: [japawBlob/B3M38ASE-labs](https://github.com/japawBlob/B3M38ASE-labs)

## Introduction

CAN networks have been deployed in cars and trucks for decades. Physical layer bus topology, which is assumed here, is rarely implemented in cars. This is due to the limited possibilities of wiring harnesses, but also to save the length (weight and volume) of the wiring. The CAN FD variant, which has been used in the last ten years, is particularly sensitive to faulty physical layer topology because it allows communication at higher data rates. The shorter bit time entails higher requirements for transient settling of the transient transients caused by reflections at the impedance jump points.

## Objectives

### Measure delay of Tx-CAN and CAN-Rx

We connected an oscilloscope to test point 4, marked as J7, to get the CAN signal. For Tx and Rx signals, we connected an oscilloscope to test points 5 and 6, respectively.

Our measured delay of Tx->CAN is **60 ns**, and the delay of CAN->Rx is **62 ns**

### Measure the characteristic impedance of the twisted pair

We measured characteristic impedance by observing signal on oscilloscope and tweaking included trimmer to minimalize reflection. 

Measured resistivity of our tweaked trimmer was 114.1 $\Omega$

### Simulate various schemes and observe cause of longlasting reflections

During first simulation we connected low impedance node to our transiver and reflections were minimal, since low impedance responded to the impedance of the twisted pair. The simulated signal cen be seen on the following picture:

![Low_impedance](/img/low_impedance.png)

When connected to the high impedance node, the reflections were more noticible. It is wisible on following picture:

![High_impedance](/img/high_impedance.png)

The impedance of transceiver did not have noticible impact on the reflection when compared to the impact created by the receiver. 

When the distance from high impedance receiver is increased, the reflections are more severe and more noticible. When the distance from low impedance reveiver is increased, the difference on the signal is hardly noticible apart from longer travel time of the signal. 

These findings were also observed on circuits that were of the star type. Impedance of the tranciever is not significant and high impedance of receiver node causes big reflections, which are more significant the more distance there is, between the tranciever and receiver. 

Because of other issues we encountered during lab measurements, we weren't able to create worst case scenarion and measure maximal feasible transmition speed. However from our knowledge, we know, that these hybrid-star networks are in use in production, where distances between nodes can be up to 20 meters and for that the maximum CAN speed is lowered from 1Mb/s to only 0.5Mb/s. 

## Conclusion

In this excercise we got acquainted with physical layer of CAN. We measured delay of the CAN controller, resistivity of used twisted pair conductor and simulated several CAN networks. On these simulations we measured the amout of reflection based on the distance of the tranciever and receiver nodes, their impedance and topology. We weren't able to complete the task of measuring maximal possible speed, but we at least enclosed an observation from production.