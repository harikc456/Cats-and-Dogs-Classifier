from keras.preprocessing.image import array_to_img, img_to_array, load_img
import numpy as np
import os
import piexif
cla=-1
num_of_classes=2
l= os.walk('data')
for i in l:
    li = i[1]
    break
ii=[]
jj=[]

for i in li:
    print (i)
    cla+=1
    l=os.walk('data/'+i)
    for j in l:
        for k in j[2]:
            try:
                piexif.remove('data/'+i+'/'+k)
                img = load_img('data/'+i+'/'+k,target_size=(64,64),grayscale=True)
                x = img_to_array(img)
                label = np.zeros(num_of_classes)
                label[cla] = 1
                jj.append(label)
                ii.append(x)
            except:
                continue
f=open('dataset.npz','wb')
arr=np.arange(len(ii))
np.random.shuffle(arr)
ii=[ii[i] for i in arr]
jj=[jj[i] for i in arr]
np.savez(f,np.array(ii),np.array(jj))
f.close()
