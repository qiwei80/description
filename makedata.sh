#!bin/sh
num=0
for file in ./org_data/girls/pants/pants/*
do
	if test -f $file
	then
		python3 makedata.py $file ./temp/data/train$num.csv ガールズパンツ
	fi
	((num++))
done
for file in ./org_data/boys/pants/pants/*
do
	if test -f $file
	then
		python3 makedata.py $file ./temp/data/train$num.csv ボーイズパンツ
	fi
	((num++))

done
for file in ./org_data/girls/tops/t_shirt/*
do
	if test -f $file
	then
		python3 makedata.py $file ./temp/data/train$num.csv ガールズTシャツ
	fi
	((num++))
done
for file in ./org_data/boys/tops/t_shirt/*
do
	if test -f $file
	then
		python3 makedata.py $file ./temp/data/train$num.csv ボーイズTシャツ
	fi
	((num++))
done

for file in ./org_data/girls/tops/sweater/*
do
	if test -f $file
	then    
    		python3 makedata.py $file ./temp/data/train$num.csv ガールズセーター
	fi
	((num++))
done

for file in ./org_data/boys/tops/sweater/*
do
	if test -f $file
	then  
  		python3 makedata.py $file ./temp/data/train$num.csv ボーイズセーター
	fi
	((num++))
done

for file in ./org_data/girls/tops/polo/*
do
	if test -f $file
	then 
 		python3 makedata.py $file ./temp/data/train$num.csv ガールズポロシャツ
	fi
	((num++))
done

for file in ./org_data/boys/tops/polo/*
do
	if test -f $file
	then   
   		python3 makedata.py $file ./temp/data/train$num.csv ボーイズポロシャツ
	fi
	((num++))
done

for file in ./org_data/girls/tops/blouse/*
do
	if test -f $file
	then  
  		python3 makedata.py $file ./temp/data/train$num.csv ガールズブラウス
	fi
	((num++))
done

for file in ./org_data/boyss/tops/blouse/*
do
	if test -f $file
	then    
    		python3 makedata.py $file ./temp/data/train$num.csv ボーイズブラウス
	fi
	((num++))
done

for file in ./org_data/girls/tops/vest/*
do
	if test -f $file
	then    
    		python3 makedata.py $file ./temp/data/train$num.csv ガールズベスト
	fi
	((num++))
done

for file in ./org_data/boys/tops/vest/*
do
	if test -f $file
	then 
 		python3 makedata.py $file ./temp/data/train$num.csv ボーイズベスト
	fi
	((num++))
done
for file in ./org_data/female/pants/jeans/*
do
	if test -f $file
	then
		python3 makedata.py $file ./temp/data/train$num.csv レーディスジーンズ
	fi
	((num++))
done
for file in ./org_data/female/pants/long_pants/*
do	        
	if test -f $file	
	then
		python3 makedata.py $file ./temp/data/train$num.csv レーディスロングパンツ
	fi
	((num++))
done
for file in ./org_data/female/pants/short_pants/*
do	        
	if test -f $file	
	then
		python3 makedata.py $file ./temp/data/train$num.csv レーディスショートパンツ
	fi
	((num++))
done
for file in ./org_data/female/pants/capri/*
do	        
	if test -f $file	
	then
		python3 makedata.py $file ./temp/data/train$num.csv レーディスカプリ
	fi
	((num++))
done
for file in ./org_data/female/pants/culottes/*
do	        
	if test -f $file	
	then
		python3 makedata.py $file ./temp/data/train$num.csv レーディスキュロット
	fi
	((num++))
done
for file in ./org_data/female/tops/vest/*
do
	if test -f $file
	then    
    		python3 makedata.py $file ./temp/data/train$num.csv レーディスベスト
	fi
	((num++))                                               
done
for file in ./org_data/female/tops/blouse/*
do
	if test -f $file
	then  
  		python3 makedata.py $file ./temp/data/train$num.csv レーディスブラウス
	fi
	((num++))
done
for file in ./org_data/female/tops/polo/*
do
	if test -f $file
	then 
 		python3 makedata.py $file ./temp/data/train$num.csv レーディスポロシャツ
	fi
	((num++))                                               
done
for file in ./org_data/female/tops/sweater/*
do
	if test -f $file
	then
		python3 makedata.py $file ./temp/data/train$num.csv レーディスセーター
	fi
	((num++))                                               
done
for file in ./org_data/female/tops/trainer/*
do
	if test -f $file
	then   
   		python3 makedata.py $file ./temp/data/train$num.csv レーディストレーナー
	fi
	((num++))                                               
done
for file in ./org_data/female/tops/t_shirt/*
do
	if test -f $file
	then
		python3 makedata.py $file ./temp/data/train$num.csv レーディスTシャツ
	fi
	((num++))                                               
done
for file in ./org_data/female/tops/cardigan/*
do
	if test -f $file
	then
		python3 makedata.py $file ./temp/data/train$num.csv レーディスカーディガン
	fi
	((num++))                                               
done
for file in ./org_data/female/tops/camisole/*
do
	if test -f $file
	then
		python3 makedata.py $file ./temp/data/train$num.csv レーディスキャミソール
	fi
	((num++))                                               
done
for file in ./org_data/female/tops/unsample/*
do
	if test -f $file
	then
		python3 makedata.py $file ./temp/data/train$num.csv レーディスアンサンプル
	fi
	((num++))                                               
done
for file in ./org_data/female/onepiece/onepiece/*
do
	if test -f $file
	then
		python3 makedata.py $file ./temp/data/train$num.csv レーディスワンピース
	fi
	((num++))                                               
done
for file in ./org_data/female/skirt/skirt/*
do
	if test -f $file
	then
		python3 makedata.py $file ./temp/data/train$num.csv レーディススカート
	fi
	((num++))                                               
done
for file in ./org_data/female/coat/coat/*
do
	if test -f $file
	then
		python3 makedata.py $file ./temp/data/train$num.csv レーディスコート
	fi
	((num++))                                               
done
for file in ./org_data/female/swim/bikini/*
do
	if test -f $file
	then
		python3 makedata.py $file ./temp/data/train$num.csv レーディスビキニ
	fi
	((num++))                                               
done
for file in ./org_data/female/swim/tankini/*
do
	if test -f $file
	then
		python3 makedata.py $file ./temp/data/train$num.csv レーディスタンキニ
	fi
	((num++))                                               
done
for file in ./org_data/female/swim/onepiece/*
do
	if test -f $file
	then
		python3 makedata.py $file ./temp/data/train$num.csv レーディス水着
	fi
	((num++))                                               
done
for file in ./org_data/female/activeware/pants/*
do
	if test -f $file
	then
		python3 makedata.py $file ./temp/data/train$num.csv レーディスアクティブパンツ
	fi
	((num++))                                               
done
for file in ./org_data/female/activeware/shirt/*
do
	if test -f $file
	then
		python3 makedata.py $file ./temp/data/train$num.csv レーディスアクティブシャツ
	fi
	((num++))                                               
done
for file in ./org_data/female/activeware/vest/*
do
	if test -f $file
	then
		python3 makedata.py $file ./temp/data/train$num.csv レーディスアクティブベスト
	fi
	((num++))                                               
done
for file in ./org_data/male/pants/jeans/*
do
	if test -f $file
	then 
 		python3 makedata.py $file ./temp/data/train$num.csv メンズジーンズ
	fi
	((num++))                                               
done
for file in ./org_data/male/pants/long_pants/*
do
	if test -f $file
	then 
 		python3 makedata.py $file ./temp/data/train$num.csv メンズロングパンツ
	fi
	((num++))                                               
done
for file in ./org_data/male/pants/short_pants/*
do
	if test -f $file
	then 
 		python3 makedata.py $file ./temp/data/train$num.csv メンズショートパンツ
	fi
	((num++))                                               
done
for file in ./org_data/male/pants/mid_pants/*
do
	if test -f $file
	then 
 		python3 makedata.py $file ./temp/data/train$num.csv メンズミディアムパンツ
	fi
	((num++))                                               
done
for file in ./org_data/male/pants/pants/*
do
	if test -f $file
	then
		python3 makedata.py $file ./temp/data/train$num.csv メンズパンツ
	fi
	((num++))
done
for file in ./org_data/male/tops/vest/*
do
	if test -f $file
	then 
 		python3 makedata.py $file ./temp/data/train$num.csv メンズベスト
	fi
	((num++))                                               
done
for file in ./org_data/male/tops/polo/*
do
	if test -f $file
	then                
		python3 makedata.py $file ./temp/data/train$num.csv メンズポロシャツ

	fi       
       	((num++))
done
for file in ./org_data/male/tops/sweater/*
do
	if test -f $file
	then                
		python3 makedata.py $file ./temp/data/train$num.csv メンズセーター
	fi  
  	((num++))
done
for file in ./org_data/male/tops/trainer/*
do
	if test -f $file 
 	then                
		python3 makedata.py $file ./temp/data/train$num.csv メンズトレーナー
	fi    
    	((num++))
done
for file in ./org_data/male/tops/t_shirt/*
do
	if test -f $file
	then                
		python3 makedata.py $file ./temp/data/train$num.csv メンズTシャツ
	fi  
  	((num++))
done
for file in ./org_data/male/tops/white_shirt/*
do
	if test -f $file        
	then                
		python3 makedata.py $file ./temp/data/train$num.csv メンズワイシャツ
	fi       
       	((num++))
done
for file in ./org_data/male/tops/cardigan/*
do
	if test -f $file        
	then                
		python3 makedata.py $file ./temp/data/train$num.csv カーディガン
	fi       
       	((num++))
done
for file in ./org_data/male/tops/tank_top/*
do
	if test -f $file        
	then                
		python3 makedata.py $file ./temp/data/train$num.csv メンズタンクトップ
	fi       
       	((num++))
done
for file in ./org_data/male/coat/coat/*
do
	if test -f $file        
	then                
		python3 makedata.py $file ./temp/data/train$num.csv メンズコート
	fi       
       	((num++))
done
for file in ./org_data/male/pajamas/pajamas/*
do
	if test -f $file        
	then                
		python3 makedata.py $file ./temp/data/train$num.csv メンズパジャマ
	fi       
       	((num++))
done