# hap_config.py
import os

def get_hap_params(custom_params=None):
    """
    Returns HAP parameters.
    If `custom_params` are provided (e.g., from a notebook), they override the defaults.
    """
    default_hap_params = {
        "model_name_or_path": "ibm-granite/granite-guardian-hap-38m",
        "annotation_column": "hap_score",
        "doc_text_column": "contents",  # Default column for documents
        "inference_engine": "CPU",
        "max_length": 512,
        "batch_size": 128,
    }

    # Merge custom_params into defaults, if provided
    if custom_params:
        default_hap_params.update(custom_params)

    print(f"Final HAP Parameters: {default_hap_params}")  # Debugging log
    return default_hap_params
