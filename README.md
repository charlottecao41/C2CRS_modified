Embedding links are in run.txt
with the best model (best.pt, put under save_model)

# C2-CRS: Coarse-to-Fine Contrastive Learning for CRS- a modified version
The base code: [**"C2-CRS: Coarse-to-Fine Contrastive Learning for Conversational Recommender System"**](https://arxiv.org/abs/2201.02732)


## Requirements
* Python == 3.8
* Pytorch == 1.8.1
* CRSLab == 0.1.2

## Quick-Start
You can train the model.
```
sh script/redial/train/redial_rec_train.sh
sh script/redial/train/redial_conv_train.sh # remember to change --restore_path

sh script/tgredial/train/tgredial_rec_train.sh
sh script/tgredial/train/tgredial_conv_train.sh # remember to change --restore_path
```

You can also test the model has been saved by us.
```
sh script/redial/eval/redial_rec_eval.sh
sh script/redial/eval/redial_conv_eval.sh

sh script/tgredial/eval/tgredial_rec_eval.sh
sh script/tgredial/eval/tgredial_conv_eval.sh
```

## Modifications
Replaced its conversation detection module with BERT-like structure

Added mixture-of-experts for three modules to output detection scores

