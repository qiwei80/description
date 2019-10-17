#!bin/sh
bash makedata.sh
cat ./temp/data/train* > ./temp/data/train.csv
python3 combine.py ./temp/data/train.csv ./temp/data/train_ok.csv
sort ./temp/data/train_ok.csv |uniq > ./data/train.csv
python3 split.py
python3 shuffer.py
mv ./data/src_r.csv ./data/src_coat_train.csv
mv ./data/tgt_r.csv ./data/tgt_coat_train.csv
onmt-build-vocab --size 50000 --save_vocab src-vocab.txt src_coat_train.csv
onmt-build-vocab --size 50000 --save_vocab tgt-vocab.txt tgt_coat_train.csv
onmt-main train_and_eval --model_type NMTSmall --config ./config/opennmt-defaults.yml ./config/default.yml
