import os
from huggingface_hub import snapshot_download,hf_hub_download

os.system("export HF_HUB_ENABLE_HF_TRANSFER=1")

REPO_ID = "lambdalabs/sd-image-variations-diffusers"
LOCAL_DIR = "echomimic_v2/pretrained_weights/sd-image-variations-diffusers"
FILE_NAME = None

if FILE_NAME != None:
    hf_hub_download(repo_id=REPO_ID, filename=FILE_NAME,local_dir=LOCAL_DIR)
else:
    snapshot_download(repo_id=REPO_ID,local_dir=LOCAL_DIR)