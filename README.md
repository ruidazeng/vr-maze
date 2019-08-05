>**If you have any questions regarding this repository, please contact Ruida Zeng at ruida dot zeng at vanderbilt dot edu**

## Cluster Analysis on Subject Data in Immersive Virtual Environments
This repository contains my work from the 2019 VUSE undergraduate summer research program, at the ***Learning in Virtual Environments (LIVE)*** research lab at [Vanderbilt University's School of Engineering](https://engineering.vanderbilt.edu). The graduate research assistant for this project is Richard Paris, who is responsible for the creation of the immersive virtual environments using Unity, and promptly conducted the experiments on around 200 subjects. The primary investigator for the project is [Dr. Bobby Bodenheimer](https://engineering.vanderbilt.edu/bio/robert-bodenheimer), associate professor at the [Department of Electrical Engineering and Computer Science](https://engineering.vanderbilt.edu/eecs/).

It mainly consists of 143 parsed `.csv` files in the "Parsed Data" sub-folder and several machine learning source codes with a detailed explanation on the methodology attempted. I also included an [appendix](#appendix), which contains useful information regarding the raw data and the parsed data.

**Note**: *Future research, either through a variety machine learning algorithms or otherwise, is encouraged on the 143, nicely parsed, `.csv` files containing information of the maze*.

### Parsed Data
The attributes of the parsed `.csv` files are `date/time`, `seconds since started`, `posX`, `posY`, `posZ`, `rotX`, `rotY`, `rotZ`, respectively. The raw tab-separated files before parsing contained more unimportant attributes but was sliced.

### `awslabel.py`
Given that the frames are in folders by subject in an S3 bucket, this can take the images from each folder and relocate them to the file structure Data/Training/Label/File on the S3 bucket. I did this so I could batch upload the frames by subject and camera angle and then worry about labeling them later. It is worth noting that when I extracted the frames, I used the naming convention [subject number][camera number][frame number].jpg so that I could easily parse all this data from the file name for labeling purposes.

### `clean.py`
The single function in this file deletes all files in a given directory. I used it when I was testing locally to save space each time I tried running label scripts.

### `count.py`
This is another file for local testing that takes a single subject and splits each of its procedures into test, validation, and training data.

### `ec2.py`
This script just automates the SSH process. So you can log in, run tasks, and get the outputs into Python. It has some potential to make scripts but I never played with it much. It was just when I thought I would need to interface more directly with EC2 from within Python.

### `label.py`
Takes the procedure files from `spiltdata.py` and the frames from an extracted video and puts them in the corresponding procedure folder (label) in the corresponding subset's folder

### `resizer.py`
This script downloads a file from S3, converts it to dimensions 224x224, uploads the new version as a copy to S3, and then deletes it off the hard drive. I did this so that I could save the EC2 instance the time and processing power (and money) to convert them while the code is running.

### `splitdata.py`
This script takes the csv output from a .xslx file and outputs the procedure, start frame and end frame to its own file in folder framecsv. All procedures are also given their own csv with start and end frames in Data/ALL. To make them all uniform, I created a second row that has all of the names of the procedures where they are capitalized throughout. That means that the label is actually row 1 and not row 0. This basically creates the files I used to label all the frames in the other scripts.

### `tfimage.py`
Loads the image data into TensorFlow and runs a simple neural network.

### `tfimagetemp.py`
This is an attempt to set up an LSTM in the same tfimage.py code from above.

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
