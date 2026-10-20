import os
import sys

# Ensure Python can find the src directory when running the script directly
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from invasive_identifier.server import (
    classify_botanical_image,
    check_invasive_status,
    generate_removal_protocol,
)

def run_pipeline_test():
    print("==================================================")
    print("🌿 Running Invasive Identifier Pipeline Test 🌿")
    print("==================================================\n")

    # 1. Test Image Classification Tool
    print("[1/3] Testing Botanical Image Classification...")
    dummy_image_path = "data/raw/sample_vine.jpg"
    
    # Create a dummy image file if it doesn't exist so the check passes
    os.makedirs("data/raw", exist_ok=True)
    if not os.path.exists(dummy_image_path):
        from PIL import Image
        img = Image.new("RGB", (224, 224), color="green")
        img.save(dummy_image_path)
        print(f" -> Created temporary sample image at {dummy_image_path}")

    class_result = classify_botanical_image(dummy_image_path)
    print("Result:", class_result)
    print("-" * 50)

    # 2. Test Regulatory Database Lookup Tool
    target_species = class_result.get("top_prediction", "celastrus orbiculatus")
    print(f"[2/3] Checking Invasive Status for: '{target_species}' in PA...")
    
    status_result = check_invasive_status(scientific_name=target_species, state_code="PA")
    print("Result:", status_result)
    print("-" * 50)

    # 3. Test Removal Protocol Rules Engine
    if status_result.get("is_invasive", False):
        print(f"[3/3] Generating Removal Protocol for invasive species...")
        protocol_result = generate_removal_protocol(scientific_name=target_species, severe_infestation=True)
        print("Result:", protocol_result)
    else:
        print(f"[3/3] Plant is not listed as invasive. Skipping removal protocol.")
        
    print("\n==================================================")
    print("✅ Pipeline Test Complete!")
    print("==================================================")

if __name__ == "__main__":
    run_pipeline_test()