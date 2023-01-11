export CUDA_VISIBLE_DEVICES=1


python3 -u run.py \
  --is_training 1 \
  --root_path ./dataset/Nasa/ \
  --data_path train.csv \
  --model_id weather_96_96 \
  --model Autoformer \
  --data custom \
  --features M \
  --seq_len 30 \
  --label_len 30 \
  --pred_len 30 \
  --e_layers 2 \
  --d_layers 1 \
  --factor 3 \
  --enc_in 15 \
  --dec_in 15 \
  --c_out 15 \
  --des 'Exp' \
  --itr 1 \
  --train_epochs 1

