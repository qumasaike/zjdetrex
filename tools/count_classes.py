import os
gt_nums = {}
classes = ['1', '2', '3']
for c in classes:
    gt_nums[c] = 0
gt_dir = 'datasets/bevheight/labels'
for fil in os.listdir(gt_dir):
    lines = open(os.path.join(gt_dir,fil),'r').readlines()
    lines = [[float(_) for _ in l.strip().split()] for l in lines]
    for line in lines:
        label = classes[int(line[-1]) - 1]
        gt_nums[label] = gt_nums.get(label,0) + 1
for key, num in gt_nums.items():
    print(key, num)
    