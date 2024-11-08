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


## Download HTML pages

TODO: 1_crawl_site.ipynb

Shortcut : Using wget

`wget --recursive --level=1  --adjust-extension https://thealliance.ai/`
