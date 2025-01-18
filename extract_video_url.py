import os
import zipfile
import xml.etree.ElementTree as ET

def extract_video_urls_from_pptx(pptx_dir):
    video_urls = {}

    # Iterate through all .pptx files in the given directory
    for file_name in os.listdir(pptx_dir):
        if file_name.endswith('.pptx'):
            pptx_path = os.path.join(pptx_dir, file_name)
            print(f"Processing: {file_name}")

            try:
                with zipfile.ZipFile(pptx_path, 'r') as pptx_zip:
                    rels_dir = "ppt/slides/_rels/"
                    slide_dir = "ppt/slides/"

                    # Extract slide relationships and find video URLs
                    for rel_file in pptx_zip.namelist():
                        if rel_file.startswith(rels_dir) and rel_file.endswith(".xml.rels"):
                            slide_num = os.path.basename(rel_file).replace("slide", "").replace(".xml.rels", "")

                            # Parse the relationships file
                            with pptx_zip.open(rel_file) as rel_content:
                                rel_tree = ET.parse(rel_content)
                                rel_root = rel_tree.getroot()

                                # Namespace for relationships
                                ns = {'r': 'http://schemas.openxmlformats.org/package/2006/relationships'}

                                for rel in rel_root.findall("r:Relationship", ns):
                                    if rel.get("Type") == "http://schemas.openxmlformats.org/officeDocument/2006/relationships/video" and rel.get("TargetMode") == "External":
                                        video_url = rel.get("Target")
                                        slide_file = f"{slide_dir}slide{slide_num}.xml"
                                        video_urls.setdefault(file_name, []).append((slide_file, video_url))

            except Exception as e:
                print(f"Error processing {file_name}: {e}")

    return video_urls


# Directory containing PPTX files
pptx_directory = "ppt"

# Extract video URLs
extracted_video_urls = extract_video_urls_from_pptx(pptx_directory)

# Display extracted video URLs
for ppt_file, urls in extracted_video_urls.items():
    print(f"\nFile: {ppt_file}")
    for slide, url in urls:
        print(f"  Slide: {slide} -> Video URL: {url}")