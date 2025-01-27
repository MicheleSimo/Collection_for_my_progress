import kagglehub

# Download latest version
path = kagglehub.dataset_download("ankushpanday1/heart-attack-in-youth-vs-adult-in-germany")

print("Path to dataset files:", path)
