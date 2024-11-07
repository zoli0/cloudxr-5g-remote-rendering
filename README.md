# Real time 3D object remote rendering in 5G

## Current system

HW: Virtual machine with NVIDIA Tesla V100 GPU used as a vGPU

OS: Windows Server 2022

Software:

- NVIDIA CloudXR SDK (4.0)
- NVIDIA Graphics Driver (451.48_grid_win10_server2016_server2019_64bit_international)
- Steam and SteamVR (latest, not required for `CloudXRServerSample.exe`)

## Usage

- Replace the `lucy.obj` file in `C:\Program Files\NVIDIA Corporation\CloudXR\VRDriver\CloudXRRemoteHMD\bin\win64\assets\models\` with your model of choice.
- Start `C:\Program Files\NVIDIA Corporation\CloudXR\VRDriver\CloudXRRemoteHMD\bin\win64\CloudXRServerSample.exe`.
- Connect the client to the server.

## Tested models

Models from Poly Haven should be downloaded as `.blend` files, you can export them to `.obj` files using Blender.

- lucy.obj (default)
- [coast_rocks_05_4k.obj](https://polyhaven.com/a/coast_rocks_05)
- [dutch_ship_large_01_4k.obj](https://polyhaven.com/a/dutch_ship_large_01)
