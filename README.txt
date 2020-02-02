#### add additional class

1. use pixelannotation tool to get the masks of the objects (use mask color as masks)

2. collect the images and add the train images to /dataset/JPEGImages mask images to dataset/Annotations/masks and test on dataset/test/

3. from any image of the new class use check_pixel_value.py in the main directory to get the color value

4. use the color value obtained on 3 and addthe class label and color to mask_pixel dictionary (~line 58) on create_mask_rcnn_tf_record_cv.py

5.  add the new class label to class-labels.pbtxt file (it should be same class label as in 4)




### create tf records to train

put the create_mask_rcnn_tf_record_cv.py in the object_detection/dataset_tools/ directory


### from the forlder object_detection/dataset_tools/ in the TF obj detection API and there run:

python3 create_mask_rcnn_tf_record_cv.py --data_dir_path=/home/hri/Jupyter_Notebooks/dataset/all/images/maskporject/dataset --annotations_dir=/home/hri/Jupyter_Notebooks/dataset/all/images/maskporject/dataset/Annotations/masks --label_map_path=/home/hri/Jupyter_Notebooks/dataset/all/images/maskporject/dataset/class-labels.pbtxt --num_shrads=1 --output_dir=/home/hri/Jupyter_Notebooks/dataset/all/images/maskporject/dataset/train.record --image_dir=/home/hri/Jupyter_Notebooks/dataset/all/images/maskporject/dataset/JPEGImages

##########################################

### To train the classifier

### from the forlder object_detection/ in the TF obj detection API this file can be in the legacy folder
download the model to used to train on your own dataset from the api in this case mask_rcnn_inception_v2_coco and set the values for the checkpoint, labels, and TF records created before (you can change the Hyper parametes too in these file if you want) 

NOTE: please take care of train records, (CP checkpoint), and number of classes.

python3 train.py --train_dir=/home/hri/Jupyter_Notebooks/dataset/all/images/maskporject/CP --pipeline_config_path=/home/hri/Jupyter_Notebooks/dataset/all/images/maskporject/mask_rcnn_inception_v2_coco.config


##########################################

### To Export the inference graph


python3 export_inference_graph.py --input_type=image_tensor --pipeline_config_path=/home/hri/Jupyter_Notebooks/dataset/all/images/maskporject/mask_rcnn_inception_v2_coco.config --trained_checkpoint_prefix=/home/hri/Jupyter_Notebooks/dataset/all/images/maskporject/CP/model.ckpt-33689 --output_directory=/home/hri/Jupyter_Notebooks/dataset/all/images/maskporject/IG



#####

set the path for the inference graph, model and test images  in the mask_rcnn_eval.py file and run it to test the classifier 

