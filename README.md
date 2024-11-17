# Real time 3D object remote rendering in 5G

## Tested systems

### TMIT VKE4

HW: Virtual machine with NVIDIA Tesla V100 GPU used as a vGPU

OS: Windows Server 2022

Software:

- NVIDIA CloudXR SDK (4.0)
- NVIDIA Graphics Driver (451.48_grid_win10_server2016_server2019_64bit_international)
- Steam and SteamVR (latest, not required for `CloudXRServerSample.exe`)

### Desktop computer

HW: NVIDIA GeForce RTX 3050

OS: Windows 11

Software:

- NVIDIA CloudXR SDK (4.0.1)
- NVIDIA Graphics Driver (32.0.15.6094)
  - This is the default driver, that was installed through Windows Update, no other configuration was needed
- Steam and SteamVR

I want to thank Simonyi Károly Collegium for providing this extra hardware for testing.

## Usage

- Replace the `lucy.obj` file in `C:\Program Files\NVIDIA Corporation\CloudXR\VRDriver\CloudXRRemoteHMD\bin\win64\assets\models\` with your model of choice.
- Start `C:\Program Files\NVIDIA Corporation\CloudXR\VRDriver\CloudXRRemoteHMD\bin\win64\CloudXRServerSample.exe`.
- Connect the client to the server.

## Tested models

Models from Poly Haven should be downloaded as `.blend` files, you can export them to `.obj` files using Blender.

- lucy.obj (default)
- [coast_rocks_05_4k.obj](https://polyhaven.com/a/coast_rocks_05)
- [dutch_ship_large_01_4k.obj](https://polyhaven.com/a/dutch_ship_large_01)
