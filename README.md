# everyday_tools
My everyday tools scripts

## imageresize_and_save.py

  **Info**: 
  
  sript open all images from input directory path resize it (by ratio) and save in outpath directory
  
  this script help me while archiving dozens of image data or (imge) model results. 

  **Usage** (python3):
  
  python imageresize_and_save.py -i input_dir_path -o output_dir_path
  * for default image ratio 0.25 = images 4 times smaller
  
  or
  
  python imageresize_and_save.py -i input_dir_path -o output_dir_path -s 0.5
  * for image 2 times smaller (choose ratio between 0.01 and 0.99)
  
  **Loguru library** info:
  
  to install loguru (the simplest ever library for logging!!):
  * pip install loguru
  
  or just replace all logger.info() in code by print() - it will work well.
  
