# mvrule.py

- version 1.0 (2019/04/27)

## 概要

- csvで定義されたルールに従って、ファイルを対象ディレクトリに移動する。
- ```mvrule.py```の配置されたディレクトリ以下を対象とする。
- 移動先ディレクトリが存在しない場合は作成する。
- 他のプロセスによって書き込み中のファイルについては対象外とし、エラー出力をする。
 - ファイルをrenameしてみることで他プロセスがファイルに書き込んでいるかを確認している。
 - 他プロセスが書き込み中かどうか簡単に判定できる方法があれば書き換えたい・・・。

## 入力

- exeファイルの配置されたフォルダ
- ファイル名(正規表現化)と移動先フォルダの書かれたcsv(mvrule.csv)

### 入力CSV サンプル (mvrule.csv)

```
#ファイル名,移動先ディレクトリ
./*_dir1_*.txt,./dir1/
./*_dir2_*.txt,./dir2/
./*_dir3_*.txt,./dir2/dir3/
./*_xxx_*.txt,./dir1/
```

(#始まりの行はコメントアウト)

### 入力ファイル サンプル

```
./
  |- test1_dir1_aaa.txt
  |- test2_dir1_bbb.txt
  |- test3_dir2_ccc.txt
  |- test4_dir2_ddd.txt
  |- test5_dir3_eee.txt
  |- test6_dir3_fff.txt
  |- test7_xxx_ggg.txt
```

## 出力

- ファイルの移動結果を表示する。
- 何かしらキーを押すとプロセスが終了するようにする。

### 出力 サンプル

```
move file from : .\test1_dir1_a.txt
move file to   :<dir> ./dir1/

move file from : .\test2_dir1_b.txt
move file to   :<dir> ./dir1/
```

### 実行結果 サンプル

```
./
  |- dir1/test1_dir1_aaa.txt
  |- dir1/test2_dir1_bbb.txt
  |- dir2/test3_dir2_ccc.txt
  |- dir2/test4_dir2_ddd.txt
  |- dir2/dir3/test5_dir3_eee.txt
  |- dir2/dir3/test6_dir3_fff.txt
  |- dir1/test7_xxx_ggg.txt
```
