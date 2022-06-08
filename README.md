# GuidedNMF
This is the repository for the paper 

> **On a Guided Nonnegative Matrix Factorization** <br>
> by Joshua Vendrow, Jamie Haddock, Elizaveta Rebrova, and Deanna Needell,
> published in IEEE ICASSP 2021.
> 
> **Abstract:** Fully unsupervised topic models have found fantastic success in document clustering and classification. However, these models often suffer from the tendency to learn less-than-meaningful or even redundant topics when the data is biased towards a set of features. For this reason, we propose an approach based upon the nonnegative matrix factorization (NMF) model, deemed \textit{Guided NMF}, that incorporates user-designed seed word supervision. Our experimental results demonstrate the promise of this model and illustrate that it is competitive with other methods of this ilk with only very little supervision information.


### Included Files
The format of the repository is as follows:  
-`Newsgroup.ipynb` contains the experiments on the 20 Newsgroup data set.  
-`Twitter.ipynb` contains the experiments on a Twitter political data set.  
-`Ablation.ipynb` contains the comparison between GuidedNMF and SeededLDA.  
-`seeded_lda` is a folder containing helper scripts for running SeededLDA, as well as the results of the ablation experiment.  
-`read_tweets.py` contains a script to generate the twitter data set (access to this data requires a Twitter Developer account).  

### Instructions for Running SeededLDA.
The authors of the SeededLDA method have an official repository for the paper at https://github.com/bsou/cl2_project/tree/master/SeededLDA. To run SeededLDA, clone this repository and follow these instructions in addition tho those provided by the authors:

1. Prior to any runs, change the file paths for any provided scripts in seeded_lda, as well as lines 1028 and 1029 of `src/SeededLDA_M1.cpp`.

2. To compile, run `c++ -I../libc SeededLDA_M1.cpp` inside of the src folder.

3. Place `seeded_lda/script.sh` into the `SeededLDA/src` directory, and place all the remaining foles from `seeded_lda` into the `SeededLDA/data` directory.

4. Inside of the `SeededLDA/data` directory, run `python3 create_seeds.py` to create the a seperate file for each amount of with seeds words.

5. To run the experiments, use the command `./scipt.sh`. You may need to first run `chmod u+x script.sh`.

6. This script runs experiments at a given rank. To change the rank, change line 4 in `20news_config` to "iNoTopics N" where N is the desired rank and change line 7 of `script.sh`, setting the name "SeededLDA_docTopicDist_N_$i.txt" where N is the desired rank.

<br />
<p align="left">
<img width="600px" src="https://github.com/jvendrow/GuidedNMF/blob/main/Figures/Table_4.png" alt="table_4">
</p>
<br />

### Quick Dependency Note
The codebase for Guided NMF depends on verssion version `0.0.2` of the `ssnmf` package. We make this requirement explicit in the `requirements.txt` file and restate it here due to issues raised by others using this repository. In order to install the correct version of `ssnmf` using pip, run the following command:
```
$ pip install ssnmf==0.0.2
```
Alternatively, all of the requirements for the repository can be installed with the following command:
```
$ pip install -r requirements.txt
```

