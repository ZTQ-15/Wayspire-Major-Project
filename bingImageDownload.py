from bing_image_downloader import downloader
downloader.download("cat pictures", limit=30,  output_dir='dataset', 
adult_filter_off=True, force_replace=False, timeout=60)

downloader.download("dog pictures", limit=30,  output_dir='dataset', 
adult_filter_off=True, force_replace=False, timeout=60)