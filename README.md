# GuidedNMF
This is the repository for the paper "Guided Nonnegative Matrix Factorization" by Joshua Vendrow, Jamie Haddock, Elizaveta Rebrova, and Deanna Needell.

### Included Files
The format of the repository is as follows:
-`Newsgroup.ipynb` contains the experiments on the 20 Newsgroup data set.
-`Twitter.ipynb` contains the experiments on a Twitter political data set.
-`Ablation.ipynb` contains the comparison between GuidedNMF and SeededLDA.
-`seeded_lda` is a folder containing helper scripts for running SeededLDA, as well as the results of the abolition experiment.

### Instructions for Running SeededLDA.
The authors of the SeededLDA method have an official repository for the paper at https://github.com/bsou/cl2_project/tree/master/SeededLDA. To run SeededLDA, clone this repository and follow these instructions in addition tho those provided by the authors:

1. Prior to any runs, change the file paths for any provided scripts in seeded_lda, as well as lines 1028 and 1029 of `src/SeededLDA_M1.cpp`.

2. To compile, run `c++ -I../libc SeededLDA_M1.cpp` inside of the src folder.

3. Place `seeded_lda/script.sh` into the `SeededLDA/src` directory, and place all the remaining foles from `seeded_lda` into the `SeededLDA/data` directory.

4. Inside of the `SeededLDA/data` directory, run `python3 create_seeds.py` to create the a seperate file for each amount of with seeds words.

5. To run the experiments, use the command `./scipt.sh`. You may need to first run `chmod u+x script.sh`.

6. This script runs experiments at a given rank. To change the rank, change line 4 in `20news_config` to "iNoTopics N" where N is the desired rank and change line 7 of `script.sh`, setting the name "SeededLDA_docTopicDist_N_$i.txt" where N is the desired rank.

