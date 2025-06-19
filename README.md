# Real time 3D object remote rendering in 5G

## Tested systems

### TMIT VKE4

HW: Virtual machine with NVIDIA Tesla V100 GPU used as a vGPU

OS: Windows Server 2022

Software:

- NVIDIA CloudXR SDK (4.0)
- NVIDIA Graphics Driver (451.48_grid_win10_server2016_server2019_64bit_international)
- Steam and SteamVR (latest, not required for `CloudXRServerSample.exe`)

### Desktop computer (SZKO01)

HW: NVIDIA GeForce GTX 1660 Ti (orginally RTX 3050)

OS: Windows 11

Software:

- NVIDIA CloudXR SDK (4.0.1)
- NVIDIA Graphics Driver (32.0.15.6094)
  - This is the default driver, that was installed through Windows Update, no other configuration was needed
- Steam and SteamVR

I want to thank Simonyi Károly Collegium for providing this extra hardware for testing.

## Usage

- Replace the `.obj` file in `C:\Program Files\NVIDIA Corporation\CloudXR\VRDriver\CloudXRRemoteHMD\bin\win64\assets\models\` with your model of choice. (In 4.0 this is `lucy.obj` and in 4.0.1 this is `ship_large.obj`)
  - Alternatively you can symlink the new `.obj` by executing `New-Item -Path .\ship_large.obj -ItemType SymbolicLink -Value .\exported.obj`
- Start `C:\Program Files\NVIDIA Corporation\CloudXR\VRDriver\CloudXRRemoteHMD\bin\win64\CloudXRServerSample.exe`.
- Connect the client to the server.

## Tested models

All files in the `models` folder are either from CloudXR SDK or [Poly Haven](https://polyhaven.com/models), licensed under CC0 1.0. To view a copy of this license, visit <https://creativecommons.org/publicdomain/zero/1.0/>

Models from Poly Haven should be downloaded as `.blend` files, you can export them to `.obj` files using Blender.
You can also make more complex models using these models and export them into one `.obj` file.

Statistics are from Blender.

| Name | Verts | Faces | Tris |
| ---- | ----: | ----: | ---: |
| [coast_rocks_05_4k.obj](https://polyhaven.com/a/coast_rocks_05) | 386400 | 771702 | 771724 |
| [concrete_cat_statue_4k.obj](https://polyhaven.com/a/concrete_cat_statue) | 5977 | 6213 | 11950 |
| [dutch_ship_large_01_4k.obj](https://polyhaven.com/a/dutch_ship_large_01) | 64041 | 67095 | 110616 |
| [searsia_lucida_4k.obj](https://polyhaven.com/a/searsia_lucida) (multiple objects, statistics are only for the biggest one) | 102858 | 66730 | 113405 |
| lucy.obj (default in CloudXR 4.0, unknown license, not included in this repo) | 49987 | 99970 | 99970 |
| rock_cat_bush.obj (example complex model created from objects above) | 418008 | 794262 | 811375 |
| ship_large.obj (default in CloudXR 4.0.1) | 11749 | 9974 | 20636 |
| test2.obj (model used in my thesis, modified from rock_cat_bush.obj to have only a part of the model appear in the scene) | TODO | TODO | TODO |

## Android client modifications

The Android app used in my theis is based on the [NVIDIA hello_cloudxr_c sample](https://github.com/NVIDIA/cloudxr-arcore/tree/master/arcore-android-sdk/samples/hello_cloudxr_c).

TODO

## Log parsing and evaluation

TODO

## GPU Finder

I used [GPU Finder](https://github.com/doitintl/gpu-finder/) to find available GPUs to run CloudXR in Google Cloud.

The patches and the output can be found in the `gpu-finder` folder.
