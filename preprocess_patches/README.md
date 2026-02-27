# Preprocess Patches for LSM Foundation Model Pretraining



## Datasets


### Allen connection projection

#### Code
- [./scripts/allen_connection_projection_get_patches_job_array.sh](./scripts/allen_connection_projection_get_patches_job_array.sh)

#### Summary

**Links**
- Data: [https://knowledge.brain-map.org/data/VJGWTBZLG77YG5NKLKI](https://knowledge.brain-map.org/data/VJGWTBZLG77YG5NKLKI)
- Only 2 LSM images: [https://download.brainimagelibrary.org/8c/13/8c13b57a7ae01f75/](https://download.brainimagelibrary.org/8c/13/8c13b57a7ae01f75/)

**Title**: Viral sparse labeling of connectionally-unique projection neurons for morphological assessment

**Description**

"To assess the morphological features of connectionally unique projection neurons in the hippocampus, G-deleted rabies virus was injected into the amygdala and accumbens to backlabel hippocampal neurons with distinct project targets. Following SHIELD-processing of whole brains or thick brain sections, volumetric image stacks were acquired using either a lightsheet or confocal microscope at 10x or 30x magnification."

"Viral tracers are used to sparsely label connectionally-unique projection neurons to assess their morphological characteristics. Following SHIELD-processing of whole brains, volumetric image stacks are acquired using a lightsheet microscope at 15x magnification."

**Note**: Data has 3 channels: 525, 600, 680. It is unclear from metadata what was labeled in each channel. 


### Allen developing mouse

#### Code
- [./scripts/allen_developing_mouse_get_images_job.sh](./scripts/allen_developing_mouse_get_images_job.sh) - To get images from website
- [./scripts/allen_developing_mouse_get_patches_job_array.sh](./scripts/allen_developing_mouse_get_patches_job_array.sh) - To get patches from downloaded images

#### Summary

**Links**
- [https://knowledge.brain-map.org/data/NUM7DTHI95ECV27X5RV](https://knowledge.brain-map.org/data/NUM7DTHI95ECV27X5RV)

**Stains**
- Neurotrace = Stains Nissl substance in neurons (composed of rRNA in rough endoplasmic reticulum and dendrites of neurons and glial cells). 
- Neurofilament = Stains neurofilaments (intermediate filament proteins)
- PV = Parvalbumin (calcium-binding protein)
- SST = Somatostatin (neuropeptide and marker for inhibitory GABAergic interneurons in cerebral cortex)
- ChAT = Choline acetyltransferase (identifies cholinergic neurons, responsible for syntehsizing the neurotransmitter acetylcholine)
- VIP = Vasoactive intestinal polypeptide 
- GAD2 = Glutamate decarboxylase 2 (stains GABAergic neurons which use gamma-aminobutyric acid as primary neurotransmitter)
- Lectin = Highlight specific carbohydrate structures on cell surfaces and in the extracellular matrix (ECM)

**Patch Selection**
Selected 10 patches from each stain
- Selected multiple patches from each image if fewer than 10 images total
- Randomly selected images for patch selection if > 10 images total


### Allen human

#### Code
- [./src/allen_human_get_patches_nifti.py](./src/allen_human_get_patches_nifti.py)
- [./scripts/allen_human_get_patches_nifti_job_array.sh](./scripts/allen_human_get_patches_nifti_job_array.sh)

#### Summary

**Links**
- [https://dandiarchive.org/dandiset/000108/](https://dandiarchive.org/dandiset/000108/)

**Stains**
- CR (Congo red) -> amyloid plaques
- LEC (Lectin) -> Blood vessels
- NN (Anti-NeuN antibody) -> Rhodamine Red-X secondary antibody
- NPY (Neuropeptide Y) -> NPY neurons
- YO (YOYO1) -> Nuclei

**Patch Selection**
1. Used random number generator (seed: 100) to generate 3 lists of numbers from available brain labels ->
Set 1: [157, 30, 88, 153, 109, 39, 103, 92, 160, 101]  
Set 2: [159, 164, 30, 73, 167, 128, 40, 124, 117, 34]  
Set 3: [153, 157, 147, 39, 113, 90, 128, 108, 28, 120]  
2. Use Set 1 for LEC, Set 2 for NN, Set 3 for YO. Take all from CR and NPY since fewer than 10 total samples
3. For each sample, take chunks in increasing order 1-10. Take multiple chunks from each image if stain has fewer than 10 total images. 
4. Use subsequent chunk or brain if no foreground in selected


### Allen human 2

#### Code
- [./scripts/allen_human2_get_images_job.sh](./scripts/allen_human2_get_images_job.sh)

#### Summary

**Links**
- [https://dandiarchive.org/dandiset/000026/draft/files?location=](https://dandiarchive.org/dandiset/000026/draft/files?location=)

**Patch Selection**
- 138: Downloaded a random sample of 10 images for each stain. Took 3-4 patches from each S. 
- 145: Downloaded a random sample of 10 images from each stain
- 146: Downloaded a random sample of 10 images with annotations (randomly selected 5 from Left and 5 from right); Downloaded 1 image from each stain for each S
- 148: Did not download patches from 148 since image quality was poor - A lot of striping in z-dimension. 



### Mesospim

#### Code
- [./scripts/mesospim_get_patches_job.sh](./scripts/mesospim_get_patches_job.sh)

### Summary

**Links**
 - [https://idr.openmicroscopy.org/webclient/?show=project-851](https://idr.openmicroscopy.org/webclient/?show=project-851) = VIP (vasoactive intestinal polypeptide) stain. 2 images, 1 with ASLM (axially scanned light-sheet microscopy) on and 1 with ASLM off. 
 - [https://idr.openmicroscopy.org/webclient/?show=project-853](https://idr.openmicroscopy.org/webclient/?show=project-853) = TPH2 (Tryptophan hydroxylase 2) stain. 

 **Data download**
 To download data across ftp:
1. Connect to server from either login node
2. Change into correct directory where want to save the data: cd `/path/to/directory` 
3. Connect to ftp: `ftp ftp.ebi.ac.uk`
4. Use name `anonymous`
5. Change into directory with data: `cd /pub/databases/IDR/idr0066-voigt-mesospim`
6. Use `ls` to list folders/files
7. Use `get <filename>` to download individual files, use `mget <filenames>` to download multiple files
8. Disconnect from ftp: `bye`

### Selma3D

#### Code
- [./src/selma3d_get_patches_nifti.py](./src/selma3d_get_patches_nifti.py) - To get patches in nifti format
- [./scripts/selma3d_get_patches_nifti_job_array.sh](./scripts/selma3d_get_patches_nifti_job_array.sh) - To get patches in nifti format
- [./src/selma3d_get_patches.py](./src/selma3d_get_patches.py) - To get patches as tiffs
- [./scripts/selma3d_get_patches_job_array.sh](./scripts/selma3d_get_patches_job_array.sh) - To get patches as tiffs

#### Summary

| Structure | Stain | Num images | Notes |
| --------- | ----- | ---------- | ----- |
| Amyloid-beta plaques | Congo red | 4 | Same as SELMA2024 |
| Astrocytes | mMslgG2a-GFAP | 1 | Same from Wu lab |
| Cell nuclei | PI ( Propidium Iodide = red fluorescent nuclear and chromosome counterstain) | 4 | Same as SELMA2024 |
| Cfos | cfos | 18 | Same as SELMA2024 |
| Chondrocytes | Collagen II | 1 | New from Shotar lab |
| Chondrogenic cells | Sox9 | 1 | New from Shotar lab |
| Dopaminergic neurons | mRb-TH | 1 | Same from Wu lab | 


### Wu

#### Code
- [./src/ng2nii.py](./src/ng2nii.py) - To download patches from neuroglancer as nifti
- [./scripts/wu_ng2nii_array.sh](./scripts/wu_ng2nii_array.sh) - To download patches from Wu brains as nifti

#### Summary

## UP TO HERE - make table


### Other

#### Code

Data downloading/extraction:

- [./src/tif_stack_get_patches.py](./src/tif_stack_get_patches.py) - To get patches from tif stack
- [./src/tif_stack_get_patches_multichannel.py](./src/tif_stack_get_patches_multichannel.py) - To get patches from tif stack with multiple channels
- [./src/tif_patches_functions.py](./src/tif_patches_functions.py) - Functions used by [./src/tif_stack_get_patches.py](./src/tif_stack_get_patches.py) and [./src/tif_stack_get_patches_multichannel.py](./src/tif_stack_get_patches_multichannel.py)

- [./src/tif_volume_get_patches.py](./src/tif_volume_get_patches.py) - To get patches from a volumetric tif image

Data conversion:

- [./src/tif2nii.py](./src/tif2nii.py) - To convert tif volumes to nifti  
- [./scripts/tif2nii_job.sh](./scripts/tif2nii_job.sh) - To convert tif volumes to nifti  

Data visualization:

- [./src/selma3d_visualization_functions.py](./src/selma3d_visualization_functions.py) - Functions used by other scripts, to visualize Selma3D data
- [./src/wu_visualization_functions.py](./src/wu_visualization_functions.py) - Functions used by other scripts, to visualize Wu data


_Last updated: 02/27/2026_ 
