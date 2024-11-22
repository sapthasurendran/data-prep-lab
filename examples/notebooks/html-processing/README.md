# Using Data Prep Kit to Process HTML files

## Step-1: Setup Python Env

See [project README](../../../README.md#create-a-virtual-environment).

Here is a quick setup guide

```bash
conda create -n dpk-html-processing-py311  python=3.11

conda activate dpk-html-processing-py311
```

If on linux do this

```bash
conda install -y gcc_linux-64
conda install -y gxx_linux-64
```

Install modules

```bash
pip install -r requirements.txt 
```


## Step-2: Crawl a website

This step will crawl a site and download HTML files in `output/1-html2parquet` directory

[1_crawl_site.ipynb](1_crawl_site.ipynb)

or use `wget`

`wget --recursive --level=1  --adjust-extension https://thealliance.ai/`

## Step-3: Process HTML files

We will process downloaded HTML files and extract the text as markdown.  The output will be saved in `output/2-markdown` directory

[2_process_html_python.ipynb](2_process_html_python.ipynb)