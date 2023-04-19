 The physical layer of CAN FD

  Daniel Štanc, Jakub Jíra

  Measured: 18.4.2023, Documented: 19.4.2023

  repository: japawBlob/B3M38ASE-labs https://github.com/japawBlob/B3M38ASE-labs

  ## Introduction

  CAN networks have been deployed in cars and trucks for decades. Physical layer bus topology, which
  is assumed here, is rarely implemented in cars. This is due to the limited possibilities of wiring
  harnesses, but also to save the length (weight and volume) of the wiring. The CAN FD variant,
  which has been used in the last ten years, is particularly sensitive to faulty physical layer
  topology because it allows communication at higher data rates. The shorter bit time entails higher
  requirements for transient settling of the transient transients caused by reflections at the
  impedance jump points.

  ## Objectives

  ### Measure delay of Tx-CAN and CAN-Rx

  We connected an oscilloscope to test point 4, marked as J7, to get the CAN signal. For Tx and Rx
  signals, we connected an oscilloscope to test points 5 and 6, respectively.

  We measured delay Tx->CAN of 60ns and CAN->Rx

  Our measured delay of Tx->CAN is 60 ns, and the delay of CAN->Rx is 62 ns

  ### Measure the characteristic impedance of the twisted pair

  We measured characteristic impedance by

  ## Conclusion