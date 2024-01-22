# gpu-benchmarks



| Configuartion | Memory (MiB) | SDXL (Load) | SDXL 50 iter | SD2.1 (Load) | SD2.1 50 iter | Comments |
| -- | -- | -- | -- | -- | -- | -- |
| A10G (g5.2xlarge) | 23,028 | 5.1   | **16.7**   |  3.7   |  **7.0**  | |
| V100 (n8-standard) | | 9.0   | **14.7**   |  5.8  | **7.0** | | 
| V100-SXM2-16GB (p3.2xlarge) | 16,384 | 9.2 | **14.7** | | | `python==3.9` `pytorch==2.1.0`    `diffusers==0.25` |
| RTX 2070 (bare metal) | 8,192 | | | 10.5 | **13.6** | `python==3.11` `pytorch==2.1.0` `diffusers==0.25` | 
