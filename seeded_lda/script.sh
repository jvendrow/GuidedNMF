#!/usr/bin/env bash
for i in {1..9}; do
    SEEDFILE="seeds$i.txt"
    cp ../data/seeds$i.txt ../data/20news_seed_file
    cat 20news_seed_file
    ./a.out ../data/20news_config temp 'save'
    sed 's/.$//' SeededLDA_docTopicDist.txt > SeededLDA_docTopicDist_10_$i.txt
done
