# White-balance-of-Hyperspectral-spectra
A simple white correction to Spectra csv files.

In the scoop of my masters thesis, We wanted to compare the spectra of different pigments when mixed with different binding media (blood, eggs, and butter).
<p  align="center">
  <img src="https://github.com/YasminaDjelil/White-balance-of-Hyperspectral-spectra/assets/97749412/5e0d25d0-ba0e-4932-a259-1a50ca08d499" width="40%" >
  <br></br>
  <img src="https://github.com/YasminaDjelil/White-balance-of-Hyperspectral-spectra/assets/97749412/cbef4621-6f81-42f2-98ae-bb2f366f72eb" width="40%" >
</p>

The figure shows the different measured samples measured and the map of the pigment mixes.

We used the LAMBDA 1050+ UV/Vis/NIR Spectrophotometer in the 250nm~2500nm range (UV to infrared).

the data white balance equation taking into account dark noise is given by:

$$
I_w(i, j) = \frac{I(i, j) - d(i, j)}{w(i, j) - d(i, j)}
$$

where $I_w(i, j)$ is the white-balanced intensity value, $I(i, j)$ is the original intensity value, $d(i, j)$ is the dark noise at pixel $(i, j)$, and $w(i, j)$ is the white balance coefficient at pixel $(i, j)$.

Example of resulting spectra : 
<p align="center">
  <img src="https://github.com/YasminaDjelil/White-balance-of-Hyperspectral-spectra/assets/97749412/ec4fa619-6d67-4ae9-a7ef-ca8077d461b0" width="40%" >
</p>
