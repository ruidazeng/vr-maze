>**If you have any questions regarding this repository, please contact Ruida Zeng at ruida dot zeng at vanderbilt dot edu**

## Cluster Analysis on Subject Data in Immersive Virtual Environments
This repository contains my work from the 2019 VUSE undergraduate summer research program, at the ***Learning in Virtual Environments (LIVE)*** research lab at [Vanderbilt University's School of Engineering](https://engineering.vanderbilt.edu). The graduate research assistant for this project is Richard Paris, who is responsible for the creation of the immersive virtual environments using Unity, and promptly conducted the experiments on around 200 subjects. The primary investigator for the project is [Dr. Bobby Bodenheimer](https://engineering.vanderbilt.edu/bio/robert-bodenheimer), associate professor at the [Department of Electrical Engineering and Computer Science](https://engineering.vanderbilt.edu/eecs/).

It mainly consists of 143 parsed `.csv` files in the "Parsed Data" sub-folder and several machine learning source codes with a detailed explanation on the methodology attempted. I also included an [appendix](#appendix), which contains useful information regarding the raw data and the parsed data.

**Note**: *Future research, either through a variety machine learning algorithms or otherwise, is encouraged on the 143, nicely parsed, `.csv` files containing information of the maze.*

***Python modules required to be installed: numpy, pandas, sklearn, matplotlib and their dependencies.***

### Parsed Data
The attributes of the parsed `.csv` files are `date/time`, `seconds since started`, `posX`, `posY`, `posZ`, `rotX`, `rotY`, `rotZ`, respectively. The raw tab-separated `.txt` files before parsing contained more unimportant attributes but was sliced.

#### `failed_km.py`
Failed attempt at k-means clustering all (posX, posZ) in tuple forms in a numpy array, from 5 distinct pandas dataframes which were imported from the first 5 parsed data alphabetically. Returned `ValueError: Found array with dim 3. Estimator expected <= 2`.

#### `km_linear.py`
Successful k-means clustering on (posX, posZ) tuples on a subject dataframe, imported from a singular parsed data file. In this example, I set the number of clusters to 8 for `AAAA.csv`, but they can be easily modified.

![k-means linear plot](/resources/km_linear.png)

#### `km_quadruple.py`
Traverse through all `.csv` files in the Parsed Data folder.
Successful k-means clustering on (posX, posZ) tuples on a subject dataframe, imported from a singular parsed data file. In this example, I set the number of clusters to 8 for `AAAA.csv`, but they can be easily modified.

![k-means quadruple plot](/resources/km_quadruple.png)

#### `km_vector.py`
Successful k-means clustering on (posX, posZ) tuples on a subject dataframe, imported from a singular parsed data file. In this example, I set the number of clusters to 8 for `AAAA.csv`, but they can be easily modified.

![k-means vector plot](/resources/km_vector.png)

#### `km_vector_more.py`
Successful k-means clustering on (posX, posZ) tuples on a subject dataframe, imported from a singular parsed data file. In this example, I set the number of clusters to 8 for `AAAA.csv`, but they can be easily modified.

![k-means vector more plot](/resources/km_vector_more.png)

#### `makecsv.py`
Successful k-means clustering on (posX, posZ) tuples on a subject dataframe, imported from a singular parsed data file. In this example, I set the number of clusters to 8 for `AAAA.csv`, but they can be easily modified.

#### `matplotlibfullalgo.py`
Successful k-means clustering on (posX, posZ) tuples on a subject dataframe, imported from a singular parsed data file. In this example, I set the number of clusters to 8 for `AAAA.csv`, but they can be easily modified.

This script will not compile currently as it is legacy code.

#### `quadruple.py`
Successful k-means clustering on (posX, posZ) tuples on a subject dataframe, imported from a singular parsed data file. In this example, I set the number of clusters to 8 for `AAAA.csv`, but they can be easily modified.

#### `subdir.py`
This is the code I applied on the original, raw, data in order to find the 10 minutes of useful data. However, since this piece of "find 10 min" algorithm his code does not work on all, I wrote this script

This script will not compile currently as it is legacy code.

#### `subdir_multiple.py`
This is a modification on the `subdir.py`, such that it will tell me which are the files that my "find 10 min" algorithm found ***two or more*** candidates.

This script will not compile currently as it is legacy code.

#### `subdir_unique.py`
This is a modification on the `subdir.py`, such that it will tell me which are the files that my "find 10 min" algorithm found ***only one*** candidate.

This script will not compile currently as it is legacy code.

#### `visual.py`

![visual plot](/resources/visual.png)

#### `turtle.py`

![turtle plot](/resources/turtle.png)

### Appendix
The following tables contain the manuever I had to apply based on the graphic representation given by applying `matplotfullalgo.py` to each individual raw data, which is significantly larger and is 

**`Y`** indicates that the data was parsed out perfectly, **`N`** indicates that I hardcoded a shift of 10 minutes because the visual gave us a visual representation of the training maze which procedes the learning maze, and **`X`** indicates throwing out the data completely because the visual made no sense even after hardcoded tinkering.

| Subject ID      | Status | Additional Notes | 
|-----------------|--------|------------------| 
| ***LABELED DATA***    |        |                  | 
| IZZO            | X      |                  | 
| SVBB            | X      |                  | 
| RCEH            | N      |                  | 
| VUUK            | X      |                  | 
| IXRA            | N      |                  | 
| FMVE Bad        | X      |                  | 
| CXIJ            | N      |                  | 
| DKAF            | X      |                  | 
| RTUG            | V      |                  | 
| CPSL            | V      |                  | 
| JHMW            | X      |                  | 
| NWTC            | X      |                  | 
| YBRX            | X      |                  | 
| MLOS            | X      |                  | 
| KMRY            | X      |                  | 
| CDYY            | X      |                  | 
| LQKJ            | V      |                  | 
| AOXY            | N      |                  | 
| WGNY            | V      |                  | 
| UVRZ            | N      |                  | 
| OGTB            | N      |                  | 
| BPPX            | N      |                  | 
| GJJJ            | N      |                  | 
| YFDE            | N      |                  | 
| RIKR            | N      |                  | 
| YJKM            | N      |                  | 
| XLLZ            | X      |                  | 
| UNWN            | X      |                  | 
| VPQA            | N      |                  | 
| MPOB            | N      |                  | 
| UPCV            | X      |                  | 
| OUWM            | N      |                  | 
| JBXP            | N      |                  | 
| VZYX            | N      |                  | 
| RSXQ            | X      |                  | 
| YPQL            | N      |                  | 
| WMKQ            | N      |                  | 
| HASK            | N      |                  | 
| UFNF            | N      |                  | 
| IHGX            | N      |                  | 
| TMPJ            | N      |                  | 
| ZTAL            | N      |                  | 
| VNWM            | N      |                  | 
| ODJH            | N      |                  | 
| SIUT            | N      |                  | 
| XLZQ            | X      |                  | 
| DRDQ            | N      |                  | 
| FXXV            | N      |                  | 
| EGRU            | N      |                  | 
| ZDGH            | N      |                  | 
| TEYQ            | N      |                  | 
| VKPD            | N      |                  | 
| TYJR            | N      |                  | 
| YNRZ            | N      |                  | 
| RGYJ            | N      |                  | 
| ANAV            | N      |                  | 
| URXR            | N      |                  | 
| NGVO            | N      |                  | 
| QQTV            | N      |                  | 
| RTBV            | N      |                  | 
| OWHE            | N      |                  | 
| QVFJ            | N      |                  | 
| CGWN            | N      |                  | 
| LAWW            | N      |                  | 
| BVEH            | N      |                  | 
| DXJP            | N      |                  | 
| PGBB            | N      |                  | 
| MRPD            | N      |                  | 
| JVRV            | N      |                  | 
| MTXB            | N      |                  | 
| KSQU            | N      | 2 candidates     | 
| NUAO            | N      |                  | 
| FWPA            | V      | 2 candidates     | 
| CXQX            | N      |                  | 
| EOPT            | N      |                  | 
| OGBK            | N      |                  | 
| WTIY            | N      |                  | 
| GZTO            | N      |                  | 
| EUDK            | N      |                  | 
| GQYU            | X      | 2 candidates     | 
| UPGW            | N      |                  | 
| SSNK            | N      | 2 candidates     | 
| IQMQ            | N      |                  | 
| GGWU            | N      |                  | 
| DBQH            | N      |                  | 
| ZDNA            | X      |                  | 
| YYTZ            | N      | 2 candidates     | 
| XQJO            | N      |                  | 
| UICN            | N      |                  | 
| HRGF            | N      |                  | 
| ONVA            | N      |                  | 
| TWJS            | X      | 2 candidates     | 
| WONG            | N      |                  | 
| MCCO            | N      |                  | 
| ***UNLABELED DATA*** |        |                  | 
| AAAA            | N      |                  | 
| ACGN            | N      |                  | 
| AELV            | N      |                  | 
| BBBB            | X      |                  | 
| BBHD            | V      |                  | 
| BFFT            | V      |                  | 
| BFJK            | N      |                  | 
| BPUF            | V      |                  | 
| BQHT            | N      |                  | 
| BWNF            | V      |                  | 
| BYOU            | N      |                  | 
| CBDG            | N      |                  | 
| CFLN            | X      |                  | 
| CXYL            | V      |                  | 
| DIJR            | V      |                  | 
| EMBJ            | N      |                  | 
| FAFH            | V      |                  | 
| FGTV            | N      | 2 candidates     | 
| FIVC            | N      |                  | 
| FJAJ            | X      |                  | 
| FJEB            | V      |                  | 
| FMKJ            | N      |                  | 
| FMRE            | N      |                  | 
| FPIT            | N      |                  | 
| FQGS            | N      |                  | 
| FQMM            | V      |                  | 
| FVZI            | V      |                  | 
| FWVY            | V      |                  | 
| GCIV            | V      |                  | 
| GGMO            | N      |                  | 
| HCWV            | V      |                  | 
| HDNQ            | V      |                  | 
| HIXM            | V      |                  | 
| HTLW            | N      |                  | 
| IAHA            | X      |                  | 
| IIMV            | V      |                  | 
| ITCT            | V      |                  | 
| JKOY            | V      |                  | 
| JYVB            | V      |                  | 
| KRKM            | N      |                  | 
| KXKS            | N      |                  | 
| LCPU            | V      |                  | 
| LFWZ            | N      |                  | 
| LMUU            | V      |                  | 
| LVEY            | V      |                  | 
| MEPW            | X      |                  | 
| MHGM            | V      |                  | 
| NEQV            | X      |                  | 
| OVOW            | N      |                  | 
| PGJC            | N      |                  | 
| QHTL            | N      |                  | 
| QKVF            | X      |                  | 
| QMGI            | N      |                  | 
| QMUX            | V      |                  | 
| QZPJ            | V      |                  | 
| RRSK            | V      |                  | 
| RVQO            | N      |                  | 
| SFUG            | N      |                  | 
| SGLD            | N      |                  | 
| SSXP            | V      |                  | 
| test            | ROFL   |                  | 
| TRTT            | V      |                  | 
| TRUK            | V      |                  | 
| TWBG            | V      |                  | 
| UING            | N      |                  | 
| UREH            | N      |                  | 
| UZMT            | N      |                  | 
| VAGY            | V      |                  | 
| VCVG            | V      |                  | 
| VJGB            | V      |                  | 
| WFKT            | V      |                  | 
| WJJU            | N      |                  | 
| WOKD            | N      |                  | 
| WRED            | V      |                  | 
| WTYX            | X      |                  | 
| XBCP            | V      |                  | 
| XKAL            | N      |                  | 
| XPRU            | N      |                  | 
| YDJH            | X      |                  | 
| YLTR            | V      |                  | 
| YPGZ            | N      |                  | 
