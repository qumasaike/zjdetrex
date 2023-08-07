import json
from pycocotools.coco import COCO
import pickle
import os

save_dir0 = 'results/labels'
id = 0
save_dir = save_dir0 + str(id)
while(os.path.exists(save_dir)):
    print(save_dir + " exists")
    save_dir = save_dir0 + str(id)
    id+=1
os.makedirs(save_dir)
results = json.load(open('output/dino_swin_large_384_4scale_36ep/coco_instances_results.json'))
coco = COCO("datasets/argoverse/annotations/instances_test2017.json")
val_file = pickle.load(open('/home/zjlab/data2/wsq/av2/test_file.pkl', 'rb'))
# val_file = pickle.load(open('./val_file.pkl', 'rb'))
image_id_pre = 0
for result in results:
    image_id = result['image_id']
    image_path = coco.loadImgs(image_id)[0]['file_name']
    image_name = image_path.split('/')[-1]
    if image_name not in val_file.keys():
        print(image_name, " not in val file")
        continue
    if image_id != image_id_pre:
        print(image_id)
        image_id_pre = image_id
    # txt_path = os.path.join(save_dir, image_name.replace('.jpg','.txt'))
    txt_path = os.path.join(save_dir, val_file[image_name].replace('.jpg','.txt'))
    category_id = result['category_id']
    bbox = result['bbox']
    bbox[2] += bbox[0]
    bbox[3] += bbox[1]
    bbox = " ".join([str(_) for _ in bbox])
    score = result['score']
    line = str(category_id) + " " + bbox + " " + str(score) + "\n"
    with open(txt_path, 'a+') as f:
        f.writelines(line)