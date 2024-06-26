# import necessary libraries
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

# import and create folders/files
imp_path = '/content/drive/MyDrive/Thesis/pigment lab/405'
output_path = '/content/drive/MyDrive/Thesis/pigment lab/405-corrected'
os.makedirs(output_path, exist_ok=True)

# extract the data from white and black balance files
w_ref_path = os.path.join(imp_path, '100% or 0 Absorbance Baseline.Correction.Raw.csv')
b_ref_path = os.path.join(imp_path, '0% or Blocked Beam Baseline.Correction.Raw.csv')
w_ref = pd.read_csv(w_ref_path)
b_ref = pd.read_csv(b_ref_path)
w_ref_np = w_ref[' %R'].to_numpy()
b_ref_np = b_ref[' %R'].to_numpy()

# white balance function
def apply_white_balance(file_path, white_ref_np, black_ref_np, output_directory):
    hsi_data = pd.read_csv(file_path)

    nm_column = hsi_data['nm'].to_numpy()  # in our case the wavelength
    hsi_data_np = hsi_data[' %R'].to_numpy()  # in our case the intensity

    min_rows = min(len(hsi_data_np), len(white_ref_np), len(black_ref_np))
    hsi_data_np = hsi_data_np[:min_rows]
    white_ref_np = white_ref_np[:min_rows]
    black_ref_np = black_ref_np[:min_rows]
    nm_column = nm_column[:min_rows]

    corrected_data_np = (hsi_data_np - black_ref_np) / (white_ref_np - black_ref_np)
    
    # corrected DataFrame
    corrected_data = pd.DataFrame({
        'nm': nm_column,
        ' %R': corrected_data_np
    })

    # save
    file_name = os.path.basename(file_path)
    corrected_file_path = os.path.join(output_directory, file_name)
    corrected_data.to_csv(corrected_file_path, index=False)

    print(f"White balance correction applied and saved to '{corrected_file_path}'")

# plot function
def plot_spectra(output):
    plt.figure(figsize=(15, 10))
    folder_name = os.path.basename(output)

    for file_name in os.listdir(output):
        if file_name.endswith('.csv'):
            file_path = os.path.join(output, file_name)
            data = pd.read_csv(file_path)
            plt.plot(data['nm'], data[' %R'], label=f'{file_name}')
  
    plt.title(f'Spectra of pigment {folder_name} mixed with different binding media')
    plt.xlabel('Wavelength')
    plt.ylabel('R%')
    plt.legend(loc='upper right', bbox_to_anchor=(1.2, 1))
    plt.show()

#################################################################################

# perform white balance
for file_name in os.listdir(imp_path):
    if file_name.endswith('.csv') and '100% or 0 Absorbance Baseline.Correction.Raw' not in file_name and '0% or Blocked Beam Baseline.Correction.Raw' not in file_name:
        file_path = os.path.join(imp_path, file_name)
        apply_white_balance(file_path, w_ref_np, b_ref_np, output_path)

print("All HSI files have been processed and corrected.")

# plot spectra
plot_spectra(output_path)
